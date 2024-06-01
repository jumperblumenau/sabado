import sqlite3
from datetime import datetime, timedelta
from tkinter import messagebox

import pytz
import random

# Configuração do banco de dados
conn = sqlite3.connect('banco_contas.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS contas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL,
    agencia TEXT NOT NULL,
    num_conta TEXT NOT NULL,
    saldo REAL DEFAULT 0,
    limite_conta REAL DEFAULT -1000,
    senha TEXT NOT NULL
)
''')
conn.commit()

cursor.execute('''
CREATE TABLE IF NOT EXISTS cartoes_credito (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero TEXT NOT NULL,
    titular TEXT NOT NULL,
    validade TEXT NOT NULL,
    cod_seguranca INTEGER NOT NULL,
    limite REAL DEFAULT 5000,
    limite_disponivel REAL DEFAULT 5000,
    conta_id INTEGER NOT NULL,
    FOREIGN KEY (conta_id) REFERENCES contas(id)
)
''')
conn.commit()
conn.close()

class ContaCorrente:
    def __init__(self, nome, cpf, agencia, num_conta, senha):
        self._nome = nome
        self._cpf = cpf
        self.saldo = 0
        self.limite_conta = -1000
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []
        self.senha = senha
        self.cartoes = []
        self.salvar_conta()

    def salvar_conta(self):
        conn = sqlite3.connect('banco_contas.db')
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO contas (nome, cpf, agencia, num_conta, saldo, limite_conta, senha)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (self._nome, self._cpf, self.agencia, self.num_conta, self.saldo, self.limite_conta, self.senha))
        conn.commit()
        conn.close()

    def __str__(self):
        return f'''
        Nome: {self._nome}
        Cpf: {self._cpf}
        Saldo: R${self.saldo:.2f}
        Agência: {self.agencia}
        Conta: {self.num_conta}
        Limite Conta: R${self.limite_conta:.2f}
        clear: {self.clear}
    '''

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')


    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))
        self.atualizar_saldo_banco()
        print(f"Você depositou R${valor:.2f}. Saldo atual: R${self.saldo:.2f}.")

    def sacar(self, valor):
        if self.saldo - valor < self.limite_conta:
            print("Você não tem dinheiro suficiente para realizar esta operação.")
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
            self.atualizar_saldo_banco()
            print(f"Você sacou R${valor:.2f}. Saldo atual: R${self.saldo:.2f}.")

    def consultar_saldo(self):
        print(f"O saldo atual da conta {self.num_conta} da agência {self.agencia} é: R${self.saldo:.2f}")

    def transferir(self, valor, conta_destino):
        if self.saldo - valor < self.limite_conta:
            print("Você não tem dinheiro suficiente para realizar esta operação.")
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
            conta_destino.saldo += valor
            conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))
            self.atualizar_saldo_banco()
            conta_destino.atualizar_saldo_banco()
            print(f"Você transferiu R${valor:.2f} para {conta_destino._nome}. Saldo atual: R${self.saldo:.2f}")

    def atualizar_saldo_banco(self):
        conn = sqlite3.connect('banco_contas.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE contas SET saldo = ? WHERE cpf = ?', (self.saldo, self._cpf))
        conn.commit()
        conn.close()

    def historico_transacoes(self):
        print("Histórico de Transações:")
        for transacao in self.transacoes:
            print(transacao)

    def sugerir_emprestimo(self, conta):
        if conta[5] >= 0:
            valor_emprestimo = abs(conta[5]) * 2
            messagebox.showinfo("Empréstimo", f"Você está elegível para um empréstimo de até R${valor_emprestimo:.2f}")
        else:
            messagebox.showinfo("Empréstimo", "Você não está elegível para um empréstimo no momento.")

    def gerar_cartao_credito(self):
        numero = CartaoCredito.gerar_numero_cartao()
        validade = CartaoCredito.gerar_validade()
        cod_seguranca = CartaoCredito.gerar_cod_seguranca()
        cartao = CartaoCredito(self._nome, self, numero, validade, cod_seguranca)
        return cartao

    def extrato(self):
        conn = sqlite3.connect('banco_contas.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transacoes WHERE conta_id = ?", (self.id,))
        transacoes = cursor.fetchall()
        conn.close()
        return transacoes


class CartaoCredito:
    def __init__(self, titular, conta_corrente, numero, validade, cod_seguranca, limite=5000):
        self.numero = numero
        self.titular = titular
        self.validade = validade
        self.cod_seguranca = cod_seguranca
        self.limite = limite
        self.limite_disponivel = limite
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @staticmethod
    def gerar_numero_cartao():
        return ' '.join([str(random.randint(1000, 9999)) for _ in range(4)])

    @staticmethod
    def gerar_validade():
        hoje = datetime.now()
        validade = hoje + timedelta(days=365*5)
        return validade.strftime('%m/%Y')

    @staticmethod
    def gerar_cod_seguranca():
        return random.randint(100, 999)

    def __str__(self):
        return f'''
        Titular: {self.titular}
        Número: {self.numero}
        Validade: {self.validade}
        Código de Segurança: {self.cod_seguranca}
        Limite: R${self.limite:.2f}
        Limite Disponível: R${self.limite_disponivel:.2f}
    '''

    def simular_compra(self, valor):
        if valor > self.limite_disponivel:
            print("Compra não aprovada. Limite insuficiente.")
        else:
            self.limite_disponivel -= valor
            self.conta_corrente.transacoes.append((-valor, self.conta_corrente.saldo, ContaCorrente._data_hora()))
            print(f"Compra de R${valor:.2f} aprovada. Limite disponível: R${self.limite_disponivel:.2f}")

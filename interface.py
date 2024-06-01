import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3
from banco import ContaCorrente


def consultar_contas():
    conn = sqlite3.connect('banco_contas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contas")
    contas = cursor.fetchall()
    conn.close()

    contas_str = "\n".join([f"Nome: {conta[1]}, CPF: {conta[2]}, Agência: {conta[3]}, Conta: {conta[4]}, Saldo: R${conta[5]:.2f}" for conta in contas])
    messagebox.showinfo("Contas Cadastradas", contas_str)


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Banco")
        self.root.geometry("800x700")
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        tk.Label(self.frame, text="Nome:").grid(row=0, column=0)
        self.nome_entry = tk.Entry(self.frame)
        self.nome_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="CPF:").grid(row=1, column=0)
        self.cpf_entry = tk.Entry(self.frame)
        self.cpf_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Agência:").grid(row=2, column=0)
        self.agencia_entry = tk.Entry(self.frame)
        self.agencia_entry.grid(row=2, column=1)

        tk.Label(self.frame, text="Conta:").grid(row=3, column=0)
        self.conta_entry = tk.Entry(self.frame)
        self.conta_entry.grid(row=3, column=1)

        tk.Label(self.frame, text="Senha:").grid(row=4, column=0)
        self.senha_entry = tk.Entry(self.frame, show="*")
        self.senha_entry.grid(row=4, column=1)

        self.cadastrar_button = tk.Button(self.frame, text="Cadastrar", command=self.cadastrar)
        self.cadastrar_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.entrar_button = tk.Button(self.frame, text="Entrar", command=self.entrar)
        self.entrar_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.consultar_contas_button = tk.Button(self.frame, text="Consultar Contas", command=consultar_contas)
        self.consultar_contas_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.consultar_cartao_button = tk.Button(self.frame, text="Consultar Cartão de Crédito", command=self.consultar_cartao)
        self.consultar_cartao_button.grid(row=8, column=0, columnspan=2, pady=10)

        self.extrato_button = tk.Button(self.frame, text="Ver Extrato", command=self.ver_extrato)
        self.extrato_button.grid(row=9, column=0, columnspan=2, pady=10)

        self.sair_button = tk.Button(self.frame, text="Sair", command=self.root.destroy)
        self.sair_button.grid(row=11, column=0, columnspan=2, pady=10)

        self.clear_button = tk.Button(self.frame, text="limpar", command=self.clear)
        self.clear_button.grid(row=10, column=0, columnspan=2, pady=10)

    def cadastrar(self):
        nome = self.nome_entry.get()
        cpf = self.cpf_entry.get()
        agencia = self.agencia_entry.get()
        conta = self.conta_entry.get()
        senha = self.senha_entry.get()

        if nome and cpf and agencia and conta and senha:
            ContaCorrente(nome, cpf, agencia, conta, senha)
            messagebox.showinfo("Sucesso", "Conta cadastrada com sucesso!")
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")

    def clear(self):
        self.nome_entry.delete(0, tk.END)
        self.cpf_entry.delete(0, tk.END)
        self.agencia_entry.delete(0, tk.END)
        self.conta_entry.delete(0, tk.END)
        self.senha_entry.delete(0, tk.END)
    def entrar(self):
        cpf = self.cpf_entry.get()
        senha = self.senha_entry.get()

        conn = sqlite3.connect('banco_contas.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contas WHERE cpf = ? AND senha = ?", (cpf, senha))
        conta = cursor.fetchone()
        conn.close()

        if conta:
            self.mostrar_opcoes(list(conta))  # Converte a tupla para lista
        else:
            messagebox.showerror("Erro", "CPF ou senha incorretos.")

    def mostrar_opcoes(self, conta):
        self.root = tk.Tk()
        self.root.geometry("800x600")
        for widget in self.frame.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"Bem-vindo, {conta[1]}!").pack(pady=100)

        tk.Button(self.root, text="Consultar Saldo", command=lambda: self.consultar_saldo(conta)).pack(pady=5)
        tk.Button(self.root, text="Depositar", command=lambda: self.depositar(conta)).pack(pady=5)
        tk.Button(self.root, text="Sacar", command=lambda: self.sacar(conta)).pack(pady=5)
        tk.Button(self.root, text="Transferir", command=lambda: self.transferir(conta)).pack(pady=5)
        tk.Button(self.root, text="Sugerir Empréstimo", command=lambda: self.sugerir_emprestimo(conta)).pack(pady=5)

        tk.Button(self.root, text="consultar cartão de crédito", command=lambda: self.consultar_cartao(conta)).pack(pady=5)

    def consultar_saldo(self, conta):
        conn = sqlite3.connect('banco_contas.db')
        cursor = conn.cursor()
        cursor.execute("SELECT saldo FROM contas WHERE id = ?", (conta[0],))
        saldo_atualizado = cursor.fetchone()[0]
        conn.close()
        messagebox.showinfo("Saldo", f"Saldo atual: R${saldo_atualizado:.2f}")

    def depositar(self, conta):
        valor = float(simpledialog.askstring("Depositar", "Valor:"))
        conn = sqlite3.connect('banco_contas.db')
        cursor = conn.cursor()
        novo_saldo = conta[5] + valor
        cursor.execute("UPDATE contas SET saldo = ? WHERE id = ?", (novo_saldo, conta[0]))
        conn.commit()
        conn.close()
        conta[5] = novo_saldo  # Atualiza o saldo no objeto em memória
        messagebox.showinfo("Sucesso", f"Você depositou R${valor:.2f}. Saldo atual: R${novo_saldo:.2f}")

    def sacar(self, conta):
        valor = float(simpledialog.askstring("Sacar", "Valor:"))
        if conta[5] - valor < conta[6]:
            messagebox.showerror("Erro", "Você não tem dinheiro suficiente para realizar esta operação.")
        else:
            conn = sqlite3.connect('banco_contas.db')
            cursor = conn.cursor()
            novo_saldo = conta[5] - valor
            cursor.execute("UPDATE contas SET saldo = ? WHERE id = ?", (novo_saldo, conta[0]))
            conn.commit()
            conn.close()
            conta[5] = novo_saldo  # Atualiza o saldo no objeto em memória
            messagebox.showinfo("Sucesso", f"Você sacou R${valor:.2f}. Saldo atual: R${novo_saldo:.2f}")

    def transferir(self, conta):
        conta_destino_num = simpledialog.askstring("Transferir", "Conta de destino:")
        valor = float(simpledialog.askstring("Transferir", "Valor:"))

        conn = sqlite3.connect('banco_contas.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contas WHERE num_conta = ?", (conta_destino_num,))
        conta_destino = cursor.fetchone()

        if conta_destino:
            if conta[5] - valor < conta[6]:
                messagebox.showerror("Erro", "Você não tem dinheiro suficiente para realizar esta operação.")
            else:
                novo_saldo = conta[5] - valor
                novo_saldo_destino = conta_destino[5] + valor
                cursor.execute("UPDATE contas SET saldo = ? WHERE id = ?", (novo_saldo, conta[0]))
                cursor.execute("UPDATE contas SET saldo = ? WHERE id = ?", (novo_saldo_destino, conta_destino[0]))
                conn.commit()
                conta[5] = novo_saldo  # Atualiza o saldo no objeto em memória
                messagebox.showinfo("Sucesso",
                                    f"Você transferiu R${valor:.2f} para a conta {conta_destino[4]}. Saldo atual: R${novo_saldo:.2f}")
                conn.close()
    def sugerir_emprestimo(self, conta):
        if conta[5] >= 0:
            valor_emprestimo = abs(conta[5]) * 2
            messagebox.showinfo("Empréstimo", f"Você está elegível para um empréstimo de até R${valor_emprestimo:.2f}")
        else:
            messagebox.showinfo("Empréstimo", "Você não está elegível para um empréstimo no momento.")

    def consultar_cartao(self):
        cartao = self.conta_corrente.gerar_cartao_credito()
        messagebox.showinfo("Cartão de Crédito", str(cartao))

    def ver_extrato(self):
        extrato = self.conta_corrente.extrato()
        extrato_str = "\n".join(
            [f"{transacao[2]}: {transacao[0]} - Saldo: R${transacao[1]:.2f}" for transacao in extrato])
        messagebox.showinfo("Extrato", extrato_str)

    def consultar_limite_disponivel(self):
        limite = self.conta_corrente.consultar_limite_disponivel()
        messagebox.showinfo("Limite Disponível", f"Limite Disponível: R${limite:.2f}")

    def consulltar_cartao(self):
        cartao = self.conta_corrente.consultar_cartao_credito()
        messagebox.showinfo("Cartão de Crédito", str(cartao))
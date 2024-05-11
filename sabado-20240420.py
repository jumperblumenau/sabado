from datetime import datetime
import pytz

class ContaCorrente():
    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []
        self.cartoes = []

    def __str__(self):
        return f'''
        Nome: {self._nome}
        Cpf: {self._cpf}
        Saldo: R${self.saldo:.2f}
        Agência: {self.agencia}
        Conta: {self.num_conta}
    '''

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def depositar(self, agencia, num_conta):
        dep = float(input('Quanto deseja depositar? '))
        self.saldo =+ dep
        self.transacoes.append((dep, self.saldo, ContaCorrente._data_hora()))
        print(f"Você depositou R${dep:.2f} na conta {self.num_conta} da agência {self.agencia} e seu saldo atual é {self.saldo}.")
        pass

    def sacar(self, agencia, num_conta):
        sac = float(input('Quanto deseja sacar? '))
        if self.saldo -sac < self._limite_conta():
            print("Voce não tem dinheiro suficiente para realizar esta operação.")
        else:
            self.saldo -= sac
            self.transacoes.append((-sac, self.saldo, ContaCorrente._data_hora()))
        print(f"Você sacou R${sac:.2f} na conta {self.num_conta} da agência {self.agencia} e seu saldo atual é {self.saldo}.")
        pass

    def consultar_saldo(self, agencia, num_conta):
        print(f"O saldo atual da conta {self.num_conta} da agência {self.agencia} é: R${self.saldo:.2f}")
        pass

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def transacao(self):
        print(f"Histórico de Transações")
        for transacao in self.transacoes:
            print(transacao)
        pass

    def transferir(self, agencia, conta_destino):
        tran = float(input('Quanto deseja transferir? '))
        if self.saldo - tran < self._limite_conta():
            print("Voce não tem dinheiro suficiente para realizar esta operação.")
        else:
            self.saldo -= tran
            self.transacoes.append((tran, self.saldo, ContaCorrente._data_hora()))
            conta_destino.saldo += tran
            conta_destino.transacoes.append((tran, conta_destino.saldo, ContaCorrente._data_hora()))
        print(f"Você transferiu R${tran:.2f} da conta {self.num_conta} da agência {self.agencia} para a {conta_destino._nome, conta_destino.num_conta}.")
        pass


class CartaoCredito():
    def __init__(self, titular, conta_corrente):
        self.numero = None
        self.titular = titular
        self.validade = None
        self.cod_seguranca = None
        self.limite = None
        self.contacorrente = conta_corrente
        conta_corrente.cartoes.append(self)

conta_rafaela = ContaCorrente('Rafaela', '001.205.671-33', "75-101", "94351")
conta_joel = ContaCorrente('Joel Reis', '123.205.789-43', "08-81", "56378")
cartao_joel = CartaoCredito('Joel Reis', conta_joel)
cartao_rafaela = CartaoCredito('Rafaela', conta_rafaela)
CartaoCredito.numero = "5124 7010 4001 8385"
CartaoCredito.numero = "1120 7555 4001 0917"

#saber se está conectado as classes
print(cartao_joel.contacorrente.num_conta)
print(conta_joel.cartoes)
class Conta:
    def __init__(self, numero, cliente, saldo, limite=1000):
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite

    @property
    def numero(self):
        return self._numero

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def limite(self):
        return self._limite

    def deposita(self, valor):
        if not isinstance(valor, int):
            print('Valor inválido.')
            return

        self._saldo += valor

    def saca(self, valor):
        if (self._saldo + self._limite) < valor:
            print('Saldo insuficiente')
            return

        self._saldo -= valor

    def extrato(self):
        print(f'Titular: {self._titular._nome}')
        print(f'Número da conta: {self._numero}')
        print(f'Saldo: R${self._saldo}')

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, saldo, limite=1000):
        super().__init__(numero, cliente, saldo, limite=limite)

    def atualiza(self, taxa):
        return super().atualiza(taxa) * 2

    def deposita(self, valor):
        return super().deposita(valor) - 0.10


class ContaPoupanca(Conta):
    def __init__(self, numero, cliente, saldo, limite=1000):
        super().__init__(numero, cliente, saldo, limite=limite)

    def atualiza(self, taxa):
        return super().atualiza(taxa) * 3


class Cliente:
    def __init__(self, nome, idade, cpf):
        self._nome = nome
        self._idade = idade
        self._cpf = cpf


class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def salario(self):
        return self._cpf

    def get_bonificacao(self):
        return self._salario * 0.10


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_funcionarios):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios

    @property
    def senha(self):
        return self._senha

    @property
    def qtd_funcionarios(self):
        return self._qtd_funcionarios

    def get_bonificacao(self):
        return self._salario * 0.15


class ControleDeBonificacoes:
    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes

    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes

    def registra(self, funcionario):
        self._total_bonificacoes += funcionario.get_bonificacao()


if __name__ == '__main__':
    cliente1 = Cliente('Lucin Santiago Santana', 21, '488.517.918-13')
    conta1 = ContaCorrente('123-4', cliente1, 1500)

    conta1.extrato()

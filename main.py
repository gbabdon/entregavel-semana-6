from abc import ABC, abstractmethod


class Conta(ABC):
    """Classe base para as contas bancarias."""

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, nome):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("O nome do titular nao pode ficar vazio.")
        self._titular = nome.strip()

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise ValueError("O saldo precisa ser um numero.")
        if valor < 0:
            raise ValueError("O saldo nao pode ser negativo.")
        self._saldo = float(valor)

    def depositar(self, valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise ValueError("O deposito precisa ser um numero.")
        if valor <= 0:
            raise ValueError("O deposito precisa ser maior que zero.")
        self._saldo += valor

    @abstractmethod
    def calcular_rendimento(self):
        """Calcula o rendimento da conta."""
        pass

    def __str__(self):
        return f"{self.__class__.__name__} de {self.titular}: R$ {self.saldo:.2f}"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(titular={self.titular!r}, saldo={self.saldo!r})"
        )

    def __eq__(self, outra):
        if not isinstance(outra, Conta):
            return NotImplemented
        return self.titular == outra.titular and self.saldo == outra.saldo

    def __lt__(self, outra):
        if not isinstance(outra, Conta):
            return NotImplemented
        return self.saldo < outra.saldo


class ContaCorrente(Conta):
    """Conta que cobra uma taxa para calcular o rendimento."""

    def __init__(self, titular, saldo=0, taxa=5):
        super().__init__(titular, saldo)
        self.taxa = taxa

    @property
    def taxa(self):
        return self._taxa

    @taxa.setter
    def taxa(self, valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise ValueError("A taxa precisa ser um numero.")
        if valor < 0:
            raise ValueError("A taxa nao pode ser negativa.")
        self._taxa = float(valor)

    def calcular_rendimento(self):
        rendimento = max(0, self.saldo * 0.01 - self.taxa)
        self._saldo += rendimento
        return rendimento

    def __str__(self):
        return f"{super().__str__()} | Taxa: R$ {self.taxa:.2f}"


class ContaPoupanca(Conta):
    """Conta que recebe rendimento de 1 por cento."""

    def __init__(self, titular, saldo=0, taxa_rendimento=0.01):
        super().__init__(titular, saldo)
        self.taxa_rendimento = taxa_rendimento

    @property
    def taxa_rendimento(self):
        return self._taxa_rendimento

    @taxa_rendimento.setter
    def taxa_rendimento(self, valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise ValueError("A taxa precisa ser um numero.")
        if not 0 <= valor <= 1:
            raise ValueError("A taxa deve ficar entre 0 e 1.")
        self._taxa_rendimento = float(valor)

    def calcular_rendimento(self):
        rendimento = self.saldo * self.taxa_rendimento
        self._saldo += rendimento
        return rendimento

    def __str__(self):
        return (
            f"{super().__str__()} | "
            f"Rendimento: {self.taxa_rendimento * 100:.1f}%"
        )


class Banco:
    """Classe que guarda e organiza as contas."""

    def __init__(self, nome, contas=None):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("O nome do banco nao pode ficar vazio.")
        self.nome = nome.strip()
        self.contas = []
        for conta in contas or []:
            self.adicionar_conta(conta)

    def adicionar_conta(self, conta):
        if not isinstance(conta, Conta):
            raise ValueError("So e possivel adicionar contas validas.")
        self.contas.append(conta)

    def __str__(self):
        return f"Banco {self.nome} - {len(self.contas)} contas"

    def __repr__(self):
        return f"Banco(nome={self.nome!r}, contas={self.contas!r})"


def main():
    banco = Banco("Banco Python")

    contas = [
        ContaCorrente("Ana", 1000),
        ContaPoupanca("Bruno", 1500),
        ContaCorrente("Carla", 800, 3),
        ContaPoupanca("Daniel", 2000),
        ContaCorrente("Eduarda", 500),
        ContaPoupanca("Felipe", 1200),
        ContaCorrente("Giovana", 900, 2),
        ContaPoupanca("Henrique", 3000),
        ContaCorrente("Isabela", 700),
        ContaPoupanca("Joao", 2500),
    ]

    for conta in contas:
        banco.adicionar_conta(conta)

    print(banco)
    print("\nContas cadastradas:")

    for conta in banco.contas:
        print(conta)

    print("\nCalculando rendimentos:")

    for conta in banco.contas:
        rendimento = conta.calcular_rendimento()
        print(f"{conta.titular}: rendimento de R$ {rendimento:.2f}")

    print("\nTestando erros:")

    try:
        ContaCorrente("Maria", -100)
    except ValueError as erro:
        print(f"Erro ao criar conta: {erro}")

    try:
        contas[0].depositar(-50)
    except ValueError as erro:
        print(f"Erro ao depositar: {erro}")

    try:
        contas[1].titular = ""
    except ValueError as erro:
        print(f"Erro no titular: {erro}")

    print("\nComparando saldos:")
    print(f"Maior saldo: {max(contas)}")

    print("\nRepresentacao tecnica:")
    print(repr(contas[0]))


if __name__ == "__main__":
    main()

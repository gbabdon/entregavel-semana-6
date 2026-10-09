# entregavel-semana-6

Sistema de Contas Bancárias em Python
Sobre o projeto

Esse projeto foi feito para a atividade da Semana 06. A ideia foi praticar os conceitos de programação orientada a objetos que aprendemos nas aulas de Python.

O programa simula um banco com contas correntes e contas poupança. É possível cadastrar contas, depositar dinheiro, calcular rendimentos e conferir os saldos.

Arquivos
main.py: código do sistema e testes das contas.
README.md: explicação do projeto.
Classes utilizadas
Conta: classe abstrata que serve de base para os tipos de conta.
ContaCorrente: representa uma conta corrente.
ContaPoupanca: representa uma conta poupança.
Banco: guarda e organiza as contas cadastradas.
Diagrama de classes
classDiagram
    class Conta {
        <<abstract>>
        titular
        saldo
        depositar()
        calcular_rendimento()
    }

    class ContaCorrente {
        taxa
        calcular_rendimento()
    }

    class ContaPoupanca {
        taxa_rendimento
        calcular_rendimento()
    }

    class Banco {
        nome
        contas
        adicionar_conta()
    }

    Conta <|-- ContaCorrente
    Conta <|-- ContaPoupanca
    Banco o-- Conta

O que foi usado

Usei herança porque a conta corrente e a poupança têm coisas em comum, como titular e saldo. Assim, elas aproveitam o código da classe Conta.

A classe Banco guarda várias contas, por isso ela tem uma lista de objetos de conta.

Também usei @property para impedir valores inválidos, como saldo negativo, nome vazio e taxas fora do permitido.

O método calcular_rendimento() funciona de forma diferente em cada tipo de conta. Isso é um exemplo de polimorfismo.

Como executar

É preciso ter o Python 3 instalado. Abra o terminal na pasta do projeto e execute:

python main.py


O programa cria dez contas, mostra os dados, calcula os rendimentos e testa alguns erros.

Conclusão

Com esse projeto, pratiquei classes, objetos, herança, encapsulamento, polimorfismo e tratamento de erros. Também aprendi a usar uma classe abstrata para definir um método que precisa ser implementado pelos outros tipos de conta.

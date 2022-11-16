#!/usr/bin/python3

# variaveis
saldo = 500

# funções
def sacar(valor):

    if saldo >= valor:
            print('valor sacado')
            print('retire o seu dinheiro na boca do caixa')

    print("Obrigado por ser nosso cliente, tenha um bom dia.")


def depositar(valor):
    saldo = 500 # tive q colocar com variavel local. acho q para alterar variavel global tem q ser dentro de uma lista (ou algum metodo)
    saldo += valor
    print(f'Foi depositado: {valor} /nAgora você tem: {saldo}')

sacar(100)
depositar(200)

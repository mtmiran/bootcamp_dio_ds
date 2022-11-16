#!/usr/bin/python3

nome = 'Mateus'
idade = 32
profissao = 'Programador'
linguagem = 'Python'

print('Nome: %s; Idade: %d' % (nome, idade))
print('Nome: {}; Idade: {}'.format(nome, idade))
print('Nome: {1}; Idade: {0}'.format(idade, nome))
print('Nome: {nome}; Idade: {idade}'.format(idade=idade, nome=nome))
print(f'Nome: {nome}; Idade: {idade}')

saldo = 45.435

print(f'Nome: {nome}; Idade: {idade}; Saldo: {saldo:.2f}')

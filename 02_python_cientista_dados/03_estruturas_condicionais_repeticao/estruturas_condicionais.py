#!/usr/bin/python3

MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input('Informe sua idade: '))

# apenas com if
if idade >= MAIOR_IDADE:
    print('Maior idade, pode tirar a CNH.')


# com else
if idade >= MAIOR_IDADE:
    print('Maior idade, pode tirar a CNH.')
else:
    print('Ainda não pode tirar a CNH.')


# com elif
if idade >= IDADE_ESPECIAL:
    print('Pode fazer aulas teóricas, mas não pode fazer aulas práticas.')
elif idade >= MAIOR_IDADE:
    print('Maior idade, pode tirar a CNH.')
else:
    print('Ainda não pode tirar a CNH.')

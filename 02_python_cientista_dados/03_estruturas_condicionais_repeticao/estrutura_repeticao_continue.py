#!/usr/bin/python3

while True:
    numero = int(input('Informe um número: '))

    # verifica se numero é par e pula
    if numero == 10:
        break
    elif numero % 2 == 0:
        continue

    print(numero)

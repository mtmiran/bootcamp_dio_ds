#!/usr/bin/python3

texto = input('Informe um texto: ')
VOGAIS = 'AEIOU'

# exemplo utilizando um iteravel
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")


# exemplo de range, tabuada de 5
for numero in range(0, 51, 5):
    print(numero, end=" ")

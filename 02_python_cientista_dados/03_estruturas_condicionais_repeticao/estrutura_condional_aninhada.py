#!/usr/bin/python3

conta_normal = False
conta_universitaria = True

saldo  = 2000
saque = 500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com uso do cheque especial!')
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    else:
        print('Saldo insuficiente!')
else:
    print('Sistema não reconheceu o tipo de conta, entre em contato com seu gerente.')

salario = 2000
lista = [1]


def salario_bonus(bonus):
    global salario

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f'listas aux={lista_aux}')
    salario += bonus
    return salario


saladio_com_bonus = salario_bonus(500)  # 2500
print(salario_bonus)
print(lista)

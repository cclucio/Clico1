# # valor_libro=[100, 200, 500, 1000, 1100]

# # for elemento in valor_libro:
# #     if elemento >= 1000:
# #         Elem= elemento*0.15
# #         print(Elem)

# # from typing import Tuple


# # lista1 = [100, 200, 300, 1000, 1500]


# # for x in lista1:
# #     if x >= 1000:
# #         y = x*0.15
# #         print('{0}'.format(y))
   

lista_compras= [100, 200]

def descuento_compras(lista_compras: list) -> tuple:
    
    suma_compra= 0

    for x in lista_compras:
        if x < 0:
            return "Ningun valor puede ser negativo "
        suma_compra += x
        if 500 < suma_compra <= 1000:
            descuento_compras = suma_compra*0.05
    
        elif 1000 < suma_compra <= 7000:
            descuento_compras = suma_compra*0.11
    
        elif 7000 < suma_compra <= 15000:
            descuento_compras = suma_compra*0.18
    
        elif suma_compra > 15000:
            descuento_compras = suma_compra*0.25

        else:
            descuento_compras = 0
                

    resultado = (int(descuento_compras), int(suma_compra), int(suma_compra-descuento_compras))
    return resultado

print(descuento_compras(lista_compras))
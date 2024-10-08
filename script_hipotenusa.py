#!/usr/bin/env python3
import sys

#Objetos para armazenar as entradas do usuario
aa = sys.argv[1]
bb = sys.argv[2]

#Função para validar as entradas 
def crivo(num):
    if num.isdigit():
        cat = int(num)
        if cat > 0 and cat < 500:
            return cat
    return None

#passar a entrada do user no crivo criado
a = crivo(aa)
b = crivo(bb)

#Confirma se a entrada passou no crivo
if a is None or b is None:
    print("Erro: Valores fora do parametro\nForneça valores inteiros, positivos e inferiores a 500")
    sys.exit(1)

#realiza o calculo com os valores finais e apresenta para o usuario
c2 = a**2 + b**2
print(f"O quadrado da hipotenusa para o triangulo retângulo com lados {a} e {b}, é {c2}")

#!/usr/bin/env python3
import sys
#Biblioteca de variaveis utilizadas
gdna = sys.argv[1].upper() #..............Recebe a sequência e deixa em caixa alta
gdnaA = gdna.count('A') #.................contagem de A
gdnaT = gdna.count('T') #.................contagem de T
gdnaC = gdna.count('C') #.................contagem de C
gdnaG = gdna.count('G') #.................contagem de G
soma_gdna = gdnaA+gdnaT+gdnaC+gdnaG #.....tamanho ideal da sequência
tamanho = len(gdna) #.....................tamanho real da sequência
n1 = int(sys.argv[2]) #...................entrada de n1
n2 = int(sys.argv[3]) #...................entrada de n2
n3 = int(sys.argv[4]) #...................entrada de n3
n4 = int(sys.argv[5]) #...................entrada de n4
n5 = int(sys.argv[6]) #...................entrada de n5
n6 = int(sys.argv[7]) #...................entrada de n6
intr1 = gdna[n2:n3-1] #...................sequência do intron_1
intr2 = gdna[n4:n5-1] #...................sequência do intron_2
cDNA = (gdna[n1:n2-1])+(gdna[n3:n4-1])+(gdna[n5:n6-1]) #DNA sem introns

# validar a entada do DNA genomico
if tamanho != soma_gdna:
    print('\nErro: sequencia de GDNA fornecida esta incorreta, verifique os dados fornecidos')
    sys.exit(1)
else:
    None

if n1 >= n2 or n2 >= n3 or n3 >= n4 or n4 >= n5 or n5 >= n6:
    print(f'\nErro: Posição dos nucleotideos fornecidos fora de ordem\nVerifique se: "{n1} < {n2} < {n3} < {n4} < {n5} < {n6}"')
    sys.exit(2)
elif n6 >= tamanho:
    print(f'\nErro: parametro "n6 = {n6}" é superior ao tamanho da sequencia {tamanho} nt')
    sys.exit(3)
else:
    print('')

if intr1.startswith('GT') and intr1.endswith('AG'):
    if intr2.startswith('GT') and intr2.endswith('AG'):
        print(f' Intron_1: {intr1} encontrado entre n={n2} e n={n3}\n Intron_2: {intr2} encontrado entre n={n4} e n={n5}')
        print('')
        print(f' A sequencia CDNA:\n {cDNA}')
    else:
        print(f'Intron_2 não encontrado entre n={n4} e n={n5}')
else:
    print(f'Intron_1 não encontrado entre n={n2} e n={n3}')

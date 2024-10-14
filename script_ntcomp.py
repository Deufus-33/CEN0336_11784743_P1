#!/usr/bin/env python3
import sys

dna = input('Escreva a sequência a ser analisada: ').upper() #Coleta a entrada do usuario, e padroniza em caixa alta para os proximos processos

for n in dna:
    countA = dna.count('A')
    countC = dna.count('C')
    countT = dna.count('T')
    countG = dna.count('G')
    soma = countA+countC+countT+countG
if soma == len(dna): #valida a integridade da sequência(apenas atcg)
    print("A: ", countA)
    print("T: ", countT)
    print("C: ", countC)
    print("G: ", countG)
else:
    print("Erro: Verifique a sequência fornecida") #avisa o usr que a sequencia esta incorreta

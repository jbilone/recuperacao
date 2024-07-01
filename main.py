#Calculadora de medias 
#Programa desenvolvido por 
#Beatryz
#Eycom
#Aluno orientador
#Rennan
from calculadora_de_media import Calculadora 
print('''
0. sair 
1. calculadora 
''') 

opcao = input('digite sua opcao: ')

if opcao == "0":
    print('saindo do programa...')
else:
    nota1 = float(input('digite a primeira nota:'))
    if nota1 < 0 or nota1 >10:
        while nota1< 0 or nota1 > 10:
            print ('a nota não pode ser menor que 0 ou maior que 10')
        nota1 = float(input('digite a nota novamente: '))

    nota2 = float(input('digite a segunda nota: '))
    if nota2 < 0 or nota2 > 10:
        while nota2< 0 or nota2 > 10:
            print ('a nota não pode ser menor que 0 ou maior que 10')
        nota2 = float(input('digite a nota novamente: '))

    nota3 = float(input('digite a terceira nota:'))
    if nota3 < 0 or nota3 > 10:
        while nota3< 0 or nota3 > 10:
            print ('a nota não pode ser menor que 0 ou maior que 10')
        nota3 = float(input('digite a nota novamente: '))

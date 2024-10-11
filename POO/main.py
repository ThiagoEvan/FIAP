import calculos

#Definindo os dados
try:
    n1 = float(input("Digite o 1º número: "))
    n2 = float(input("Digite o 2º número: "))

except:
    print("Tente novamente")

#menu
try:
    operacaoMat = int(input('''Qual operação deseja realizar: 
    [1] - Somar
    [2] - Subtrair
    [3] - Multiplicar
    [4] - Dividir

Opção: '''))

except:
    print("Tente novamente")

else:
    #Operação
    match operacaoMat:
    
        case 1:
            print(f'O resultado é {calculos.somar(n1,n2)}')

        case 2:
            print(f'O resultado é {calculos.subitração(n1,n2)}')

        case 3:
            print(f'O resultado é {calculos.multiplicacao(n1,n2)}')

        case 4:
            print(f'O resultado é {calculos.divisao(n1,n2)}')
        case _: 
            print('Opção não encontrada')

finally:
    print('Operação realizada com sucesso')
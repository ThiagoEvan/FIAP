#variavel que irá receber a opção do usuário
opcao = 0

#inicio do menu
while opcao != 4:
    print('''Painel do programa       
1 - Cód 1
2 - Cód 2
3 - Cód 3
4 - Sair do programa''')
    opcao = int(input("Opção:"))
    
    #Verificação das opções 
    if opcao == 1:
        print("\nSão Paulo é tri-campeão mundial\n")
    elif opcao == 2:
        print("\nSão Paulo é campeão de tudo\n")
    elif opcao == 3:
        print("\nSão Paulo nunca foi rebaixado\n")

print("\nResumindo, o São Paulo é o maior time do Brasil")
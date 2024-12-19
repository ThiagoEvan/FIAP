#testando a função LAMBDA        
#soma = lambda a, b: a + b
#print(soma(3,4))

#testando a função LAMBDA condicional 
#verificarPositivo = lambda x: "Positivo" if x >= 0 else "Negativo"
#print(verificarPositivo(3-2+5))

# Função MAP

ImparPar = lambda x: f'O número {x} é par ' if x % 2 == 0 else f'O número {x} é impar'

print(list(map(ImparPar, [2, 32, 53, 6, 75,97])))


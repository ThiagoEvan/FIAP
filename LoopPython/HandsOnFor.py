peso = 0.0
total = 0

for i in range (1,11):

    peso_atual = float(input(f"Qual é o peso da caixa {i}: "))
    peso += peso_atual
    total += i

media = peso/ total

print(f'O peso total do estoque é {peso} \nA média de peso é {media}')
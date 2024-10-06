try:
    idade = int(input("Digite sua idade: "))

except ValueError:
    print("Insira um valor de um número inteiro para a idade")

else:
    print(f"Sua idade é {idade}")

finally:
    print("Obrigado por usar o nosso programa")

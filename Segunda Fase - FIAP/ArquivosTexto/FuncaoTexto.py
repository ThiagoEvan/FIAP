arq = open("c:\\Users\\tevan\\OneDrive\\Documentos\\FIAP\\FIAP\\Assets\\script.txt")


for linha in arq.readlines():
    print(linha)

arq.seek(3)
print(arq.readline())
print(f'Linha: {arq.tell}')

arq.close()



import csv

with open('c:\\Users\\tevan\\OneDrive\\Documentos\\FIAP\\FIAP\\Assets\\script.csv') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=',', quotechar='"')
    next(leitor_csv)  
    
    for linha in leitor_csv:
        mensagem = f"Nome: {linha[0]} - Idade: {linha[1]} - Altura {linha[2]}"
        print(mensagem)
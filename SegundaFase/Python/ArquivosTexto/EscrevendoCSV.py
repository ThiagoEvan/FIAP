import csv

dados = ['Gabi', 17, '165']

with open("c:\\Users\\tevan\\OneDrive\\Documentos\\FIAP\\FIAP\\Assets\\script.csv", mode = 'a', newline = '') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter= ',')
    escritor_csv.writerow(dados)

def velocidadeMedia(dist, temp):
    #calculando a velocidade média:
    VelMedia = dist/temp

    #rretornar o calculo da velocidade média
    return VelMedia

#Definindo distancia e tempo
try:
    distancia = float(input('Distância pecorrida (km): '))
    tempo = float(input('Tempo da viagem (h): '))
except:
    print('Tente novamente!')

# Chamando a função
print(f'A velocidade média é {velocidadeMedia(distancia,tempo)} km/h')

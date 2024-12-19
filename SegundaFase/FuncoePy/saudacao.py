def Saudacao(Periodo, *Nome):

    for i in Nome:

        if Periodo.lower() in ('manha', 'm'):
            print(f'Bom dia {i}, Como vai?')
        
        elif Periodo.lower() in ('tarde', 't'):
            print(f'Bom tarde {i}, Como vai?')
        else: 
            print( f'Bom noite {i}, Como vai?')
        
print(Saudacao('m','Thiago','Lucas'))
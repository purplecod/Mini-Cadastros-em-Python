def achearquirvo(texto):
    """
    essa função vai analisar se a sua maquina contém o arquivo que o usuario passou no parânmetro "texto", se sim, irá retornar o valor True, se não, False.
    
    
    """
    try:
        manipulador = open(texto)
        manipulador.close()
    except:
        return False
    else:
        return True


def criararquivo(nome):
    """
    essa função irá criar um arquivo com o nome que o usuario passar no parâmetro. 
    """
    try:
         open(nome, 'wt+')


    except:
        print('houve algum erro ao criar o arquirvo...')

    else:
        print('arquirvo criado')

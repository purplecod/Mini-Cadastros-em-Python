def achearquirvo(texto):
    try:
        manipulador = open(texto)
        manipulador.close()
    except:
        return False
    else:
        return True


def criararquivo(nome):
    try:
         open(nome, 'wt+')


    except:
        print('houve algum erro ao criar o arquirvo...')

    else:
        print('arquirvo criado')

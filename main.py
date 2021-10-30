from bib import menu, cores, arqui
import time
import os

sexo = 0
okk = False
dados = []
pessoas = {}
z = len(dados)
cont = 0
arq = 'cadastro.txt'
try:
    arq = open('cadastro.txt')
except:
    if arqui.achearquirvo(arq):
        print('arquirvo encontrado')

    else:
        print('arquirvo não encontrado')
        arqui.criararquivo(arq)
else:
    print('arquivo esta pronto')

ok = False
hora = time.localtime()
menu.cadasmenu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Limpar Cadastros', 'Sair do sistema'])
while True:
    while not ok:
        try:
            a = int(input(cores.verde('digite a sua opção: ')))
        except ValueError:
            print(cores.vermelho('ERRO: Por favor, digite um numero inteiro.'))
            time.sleep(1)
        except KeyboardInterrupt:
            print(cores.vermelho('\no usuário optou por não digitar.\n encerrando o sistema...'))
            time.sleep(1)
            break
        else:
            if a >= 1 and a <= 4:
                ok = True

            else:
                print(cores.vermelho('ERRO: opção invalida, por favor digite uma das opção do menu principal'))

    if a == 1:
        menu.titulo('VISUALISANDO CADASTROS')
        arq = open('cadastro.txt', 'r')
        dados = arq.readlines()
        for linha in dados:
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:^3} anos {dado[2]:>8}')

        ok = False
        a = 0
        arq.close()
    elif a == 2:
        menu.titulo('ADCIONANDO CADASTROS')
        arq = open('cadastro.txt', 'a')
        okk = False
        while not okk:
            try:
                quantas = int(input('quantas pessoas voce quer cadastrar?: '))
            except ValueError:
                print(cores.vermelho('ERRO: digite um numero inteiro.'))
            else:
                okk = True

        for a in range(0, quantas):
            okk = False
            nome = str(input('qual é o nome do individo? [Digite <PARE> para parar de cadastrar]: ')).strip()
            if 'PARE' in nome:
                a = 0
                ok = False
                arq.close()
                print(cores.amarelo('Cadastro interrompido'))
                break
            while not okk:
                try:
                    idade = int(input('qual é a idade: '))
                except ValueError:
                    print(cores.vermelho('ERRO: Por favor, digite um numero inteiro.'))
                else:
                    okk = True
            okk = False
            while not okk:
                try:
                    sexo = int(input('qual é seu sexo? [Masculino/1] [feminino/2]: '))

                except ValueError:
                    print(cores.vermelho('porfavor digite um numero inteiro.'))
                else:
                    if sexo == 1 or sexo == 2:
                        okk = True
                    else:
                        print(cores.vermelho('ERRO: digite uma opção valida'))
            arq.write(f'{nome}')
            arq.write(';')
            arq.write(f'{idade}')
            arq.write(';')
            if sexo == 1:
                arq.write(f'Masculino\n')
            else:
                arq.write(f'Feminino\n')
        a = 0
        ok = False
        arq.close()
    elif a == 3:
        menu.titulo('EXCLUIR CADASTROS')
        okk = False
        while not okk:
            try:
                crt = int(input(cores.amarelo('Tem certeza que deseja o arquivo? ') + '[SIM/1] [NÃO/2] '))
            except ValueError:
                print(cores.vermelho('ERRO: digite um numero inteiro'))
            else:
                if crt == 1:
                    os.remove('cadastro.txt')
                    print('arquirvo limpo')
                    open('cadastro.txt', 'wt+')
                    okk = True
                elif crt == 2:
                    print('arquivo mantidos')
                    okk = True
                else:
                    print(cores.vermelho('ERRO:porfavor digite 1 para sim ou 2 para não'))
        a = 0
        ok = False
    elif a == 4:
        menu.titulo('SAINDO DO PROGRAMA')
        print('salvando e encerrando o seu programa...')
        arq.close()
        if hora.tm_hour >= 0 and hora.tm_hour < 6 or hora.tm_hour >= 18 and hora.tm_hour <= 23:
            a = 0
            print('tenha uma boa noite!')
            break
        elif hora.tm_hour >= 6 and hora.tm_hour < 12:
            print('tenha um bom dia!')
            break
        elif hora.tm_hour >= 12 and hora.tm_hour < 18:
            print('tenha uma boa tarde!')
            break
arq.close()

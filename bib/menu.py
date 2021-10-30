from bib import cores

def titulo(txt):
  print('==='*15)
  print(txt.center(44))
  print('==='*15)


def cadasmenu(lista,txt='MENU PRINCIPAL'):
  c=1
  titulo(txt)
  for items in lista:
    print(f'{c} - {cores.roxo(items)}')
    c+=1
  print('==='*15)
 
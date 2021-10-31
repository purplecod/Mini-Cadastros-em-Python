from bib import cores

def titulo(txt):
  """
  essa função irar criar um titulo centralisado, exemplo:
  =============================================
                    titulo               
  ============================================= 
  o parâmatro "txt" é o titulo que o usuario deseja usar.
  """
  print('==='*15)
  print(txt.center(44))
  print('==='*15)


def cadasmenu(lista,txt='MENU PRINCIPAL'):
  """
  essa função irá criar um menu bem organizado, onde o parâmetro "lista" vai ser as opções do menu (use lista para evitar problemas), e o parâmatro "txt" vai ser o titulo do menu (se não for editado pelo usuario, o titulo sera 'MENU PRINCIPAL')
  """
  c=1
  titulo(txt)
  for items in lista:
    print(f'{c} - {cores.roxo(items)}')
    c+=1
  print('==='*15)
 
#-- SOBRE O TRABALHO ------------------------------------------------------------------------------------------------------------------------
# ENGENHARIA DE SOFTWARE - 5° PERÍODO - UNIMONTES 2023
# >> Professor
# ● Allysson Costa Silva
# >> Equipe
# ● Mateus Moreira Durães; 
# ● Uedson Gaiek Souza;
# ● Júlio César Porto de Carvalho; 
# ● Bruno Alex Cardoso Freitas
# >> Escopo do projeto
#   Com este sistema, um gerente de uma loja hipotética será capaz de verificar o estoque atual de sua loja, o valor líquido dos produtos,
# assim como adicionar e remover produtos a qualquer momento.
#   O programa será feito em python e usará um arquivo .TXT como arquivo para de banco de dados. O sistema será demonstrado através de uma
# interface gerada no CMD.
#-- BIBLIOTECAS -----------------------------------------------------------------------------------------------------------------------------
from config import *
from pages import *
#-- CHAMADA PRINCIPAL -----------------------------------------------------------------------------------------------------------------------
# Executando o programa
if __name__ == '__main__':
    system('cls')

    page = 0
    while (True): # Loop principal
        PÁGINAS[page].pgDesenharPag()
        PÁGINAS[1].pgAtualizarPag(f'''
|== ESTOQUE ============================|
{cfMostrarEstoque()}
{cfValorLiquido()}
| 1. Voltar                             |
|=======================================|''')
        page = PÁGINAS[page].pgExcSel(input('>> '))

    # Fim do programa
        if page == -1: break
        elif page < -1:
            cfPrint('Um erro inesperado ocorreu...', type = 'Erro', skip = True)
            break
    print(f'{CMD_VERDE}< FIM DO PROGRAMA >{CMD_DEFAULT}')
    

#--------------------------------------------------------------------------------------------------------------------------------------------
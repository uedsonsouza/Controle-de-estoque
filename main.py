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
# assim como adicionar e remover produtos a qualquer momento. O sistema também deverá ser capaz de registrar e atualizar uma lista
# de fornecedores. Além disso, através de uma página de log-in, o sistema será capaz de definir o tipo de usuário (admin ou funcionário) para
# limitar funções dentro do processo.
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
        page = PÁGINAS[page].pgExcSel(input('>> '))

    # Fim do programa
        if page == -1: break
        elif page < -1:
            cfPrint('Um erro inesperado ocorreu...', skip = True)
            break
    print(f'{CMD_VERDE}< FIM DO PROGRAMA >{CMD_DEFAULT}')
    

#--------------------------------------------------------------------------------------------------------------------------------------------
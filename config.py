#-- O QUE HÁ AQUI ---------------------------------------------------------------------------------------------------------------------------
# Neste script, definimos todas as variáveis de configuração assim como as funções micelânias que foram utilizadas pelo sistema.
#-- BIBLIOTECAS -----------------------------------------------------------------------------------------------------------------------------
from os import system
#-- CONFIGURAÇÕES ---------------------------------------------------------------------------------------------------------------------------
DEPURAÇÃO = True
EM_EXECUÇÃO = True
# >> Define cores
CMD_VERMELHO = '\033[1;31;40m'
CMD_VERDE    = '\033[1;32;40m'
CMD_AMARELO  = '\033[1;33;40m'
CMD_AZUL     = '\033[1;34;40m'
CMD_MAGENTA  = '\033[1;35;40m'
CMD_CIANO    = '\033[1;36;40m'
CMD_BRANCO   = '\033[1;37;40m'
CMD_DEFAULT  = '\033[1;0;40m'
#-- COMANDOS --------------------------------------------------------------------------------------------------------------------------------
# >> Validar seleção
def cfValidarSel(arg, num_sel):
    # A seleção deve ser inteiro
    try: arg = int(arg)
    except: return False
    # A seleção deve estar entre 1 e num_sel
    if arg < 1 or arg > num_sel: return False
    return True

# >> Coloca um texto na tela somente em mode de depuração
def cfPrint(text, skip = False):
    if DEPURAÇÃO:
        print(f'{CMD_AMARELO}[DEPURAÇÃO] {text}{CMD_DEFAULT}')
        if not skip: system('pause')
#--------------------------------------------------------------------------------------------------------------------------------------------
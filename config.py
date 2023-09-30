#-- O QUE HÁ AQUI ---------------------------------------------------------------------------------------------------------------------------
# Neste script, definimos todas as variáveis de configuração assim como as funções micelânias que foram utilizadas pelo sistema.
#-- BIBLIOTECAS -----------------------------------------------------------------------------------------------------------------------------
from os import system
#-- CONFIGURAÇÕES ---------------------------------------------------------------------------------------------------------------------------
# >> Gerais
DEPURAÇÃO = True
EM_EXECUÇÃO = True
# >> Definições
SEPARADOR = ';'
PRODUTOS_DIR = './produtos.txt'
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
def cfPrint(text, type = '', skip = False):
    if DEPURAÇÃO:
        match type:
            case 'Sucesso' : print(f'{CMD_VERDE}[DEPURAÇÃO] ', end = '')
            case 'Aviso'   : print(f'{CMD_AMARELO}[AVISO] ', end = '')
            case 'Erro'    : print(f'{CMD_VERMELHO}[ERRO] ', end = '')
            case ''        : print(f'{CMD_AZUL}[DEPURAÇÃO] ', end = '')
        print(f'{text}{CMD_DEFAULT}')
        if not skip: system('pause')
#-- BANCO DE DADOS --------------------------------------------------------------------------------------------------------------------------
PRODUTOS = []
try:
    with open(PRODUTOS_DIR, 'r', encoding='utf-8') as prod_db:
        for line in prod_db.readlines():
            PRODUTOS.append( line.split(SEPARADOR)[:-1] )
except:
    system('cls')
    cfPrint(f'O arquivo "{PRODUTOS_DIR}" não pode ser aberto corretamente!', type = 'Erro')

def cfMostrarEstoque(ARG):
    output = ''
    for prod in ARG:
        output += ('|{:<25} {:<5.2f}R$ {:<4}x|\n'.format(prod[0], float(prod[1]), prod[2]))
    output += '|---------------------------------------|'
    return output

def cfValorLiquido(ARG):
    total = 0
    for prod in ARG:
        total += float(prod[1]) * float(prod[2])
    return '> Valor total em estoque {:<5.2f}R$'.format(total)

#--------------------------------------------------------------------------------------------------------------------------------------------
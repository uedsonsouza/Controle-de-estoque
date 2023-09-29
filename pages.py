#-- O QUE HÁ AQUI ---------------------------------------------------------------------------------------------------------------------------
# Neste script, definimos a classe das páginas utilizadas e suas lógicas para execução do sistema.
#-- BIBLIOTECAS -----------------------------------------------------------------------------------------------------------------------------
from config import *
#-- CLASSE ----------------------------------------------------------------------------------------------------------------------------------
class Página:
    def __init__(self, pg_nome, pg_num, pg_pag, num_sel = 0) -> None:
        self.nome = pg_nome
        self.num = pg_num
        self.pag = pg_pag
        self.num_sel = num_sel
    
    # Desenha a página na tela
    def pgDesenharPag(self):
        system('cls')
        cfPrint(f'PG_NUM: {self.num}', skip = True)
        print(self.pag)

    # Executa uma função
    def pgExcSel(self, cursor):
        system('cls')
        if (cfValidarSel(cursor, self.num_sel)):
            if self.nome == 'Menu principal':
                match cursor:
                    case '1': # Ver estoque
                        return 1

                    case '2': #TODO Adicionar produto
                        cfPrint(f'Ops! Esta função ainda não foi implementada...')

                    case '3': #TODO Remover produto
                        cfPrint(f'Ops! Esta função ainda não foi implementada...')

                    case '4': #TODO Lista de fornecedores
                        cfPrint(f'Ops! Esta função ainda não foi implementada...')

                    case '5': return -1
                    case _: return -2
            elif self.nome == 'Estoque':
                match cursor:
                    case '1': return 0
                    case _: return -2
        else: # Entrada inválida
            print(f'{CMD_VERMELHO}[ERRO!] Opção inválida! Por favor, certifique-se de selecionar uma das opções listadas.{CMD_DEFAULT}')
            system('pause')
            return self.num


#-- PÁGINAS ---------------------------------------------------------------------------------------------------------------------------------
PÁGINAS = [
# Página 0
Página('Menu principal', 0,
f'''
|== MENU PRINCIPAL =====================|
| 1. Ver estoque                        |
| 2. Adicionar produto                  |
| 3. Remover produto                    |
| 4. Lista de fornecedores              |
| 5. Sair                               |
|=======================================|''', num_sel = 5),

# Página 1
Página('Estoque', 1,
f'''
|== ESTOQUE ============================|
[...]
| 1. Voltar                             |
|=======================================|''', num_sel = 1)
]
#--------------------------------------------------------------------------------------------------------------------------------------------
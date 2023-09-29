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
                    case '1': return 1
                    case '2': return 2
                    case '3': #TODO Remover produto
                        cfPrint(f'Ops! Esta função ainda não foi implementada...', type = 'Aviso')
                        return self.num
                    case '4': return -1
                    case _: return -2

            elif self.nome == 'Estoque':
                match cursor:
                    case '1': return 0
                    case _: return -2

            elif self.nome == 'Adicionar produto':
                match cursor:
                    case '1':
                        prd_valor , prd_qnt = 0, 0
                        print('|== NOVO PROD. =========================|')
                        prd_nome  = input('Nome do produto: ')
                        while prd_valor < 0.01:
                            valor = input('Valor do produto (R$): ')
                            try: prd_valor = float(valor)
                            except: print(f'{CMD_VERMELHO}[ERRO!] Este não é um valor válido! {CMD_DEFAULT}')
                        while prd_qnt < 1:
                            qnt = input('Quantidade atual: ')
                            try: prd_qnt = int(qnt)
                            except: print(f'{CMD_VERMELHO}[ERRO!] Este não é uma quantidade válida! {CMD_DEFAULT}')

                        try:
                            with open(PRODUTOS_DIR, 'a', encoding='utf-8') as prod_db:
                                for line in prod_db.readlines():
                                    if line[0] == prd_nome: return 0
                                prod_db.write(f'\n{prd_nome}{SEPARADOR}{prd_valor}{SEPARADOR}{prd_qnt}{SEPARADOR}')
                        except:
                            system('cls')
                            cfPrint(f'O arquivo "{PRODUTOS_DIR}" não pode ser aberto corretamente!', type = 'Erro')

                        return 0
                    case '2': return 0
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
| 4. Sair                               |
|=======================================|''', num_sel = 4),

# Página 1
Página('Estoque', 1,
f'''
|== ESTOQUE ============================|
{cfMostrarEstoque(PRODUTOS)}
{cfValorLiquido(PRODUTOS)}
| 1. Voltar                             |
|=======================================|''', num_sel = 1),

# Página 2
Página('Adicionar produto', 2,
f'''
|== NOVO PROD. =========================|
| 1. Continuar                          |
| 2. Cancelar                           |
|=======================================|''', num_sel = 2)
]
#--------------------------------------------------------------------------------------------------------------------------------------------
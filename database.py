import psycopg2
from credentials import keys

DB_NAME = keys.get('DATABASE_NAME')
DB_USER = keys.get('DATABASE_USER')
DB_PASSWORD = keys.get('DATABASE_PASSWORD')
#dados = {'ida': [{'origem': 'VCP - 05:55', 'destino': 'SSA - 08:15', 'duracao': ' 02:20', 'conexao': ' Direto ', 'preco': ' R$ 1.899,55 '}, {'origem': 'VCP - 11:45', 'destino': 'SSA - 14:05', 'duracao': ' 02:20', 'conexao': ' Direto ', 'preco': ' R$ 1.899,55 '}, {'origem': 'VCP - 06:10', 'destino': 'SSA - 10:30', 'duracao': ' 04:20', 'conexao': ' 1 parada ', 'preco': ' R$ 2.657,55 '}, {'origem': 'VCP - 19:50', 'destino': 'SSA - 00:20', 'duracao': ' 04:30', 'conexao': ' 1 parada ', 'preco': ' R$ 2.657,55 '}, {'origem': 'VCP - 18:15', 'destino': 'SSA - 23:15', 'duracao': ' 05:00', 'conexao': ' 1 parada ', 'preco': ' R$ 2.657,55 '}, {'origem': 'VCP - 11:00', 'destino': 'SSA - 19:10', 'duracao': ' 08:10', 'conexao': ' 1 parada ', 'preco': ' R$ 2.657,55 '}, {'origem': 'VCP - 06:10', 'destino': 'SSA - 14:30', 'duracao': ' 08:20', 'conexao': ' 1 parada ', 'preco': ' R$ 2.657,55 '}], 'volta': [{'origem': 'SSA - 15:05', 'destino': 'VCP - 17:35', 'duracao': ' 02:30', 'conexao': ' Direto ', 'preco': ' R$ 756,45 '}, {'origem': 'SSA - 20:35', 'destino': 'VCP - 23:05', 'duracao': ' 02:30', 'conexao': ' Direto ', 'preco': ' R$ 756,45 '}, {'origem': 'SSA - 06:00', 'destino': 'VCP - 11:05', 'duracao': ' 05:05', 'conexao': ' 1 parada ', 'preco': ' R$ 2.659,45 '}, {'origem': 'SSA - 15:10', 'destino': 'VCP - 21:30', 'duracao': ' 06:20', 'conexao': ' 1 parada ', 'preco': ' R$ 2.659,45 '}, {'origem': 'SSA - 15:10', 'destino': 'VCP - 23:05', 'duracao': ' 07:55', 'conexao': ' 1 parada ', 'preco': ' R$ 2.659,45 '}, {'origem': 'SSA - 17:45', 'destino': 'VCP - 23:05', 'duracao': ' 05:20', 'conexao': ' 1 parada ', 'preco': ' R$ 2.659,45 '}]}

class config:
    def __init__(self, dadosconexao):
        self.dadosconexao = dadosconexao

    def setParametros(self):
        self.dadosconexao = "host='localhost' dbname= DB_NAME user= DB_USER password= DB_PASSWORD"
        return self

    def alteraBD(self, string_sql, valores):
        conn = None
        config.setParametros(self)
        
        try:
            conexao = psycopg2.connect(self.dadosconexao)
            sessao = conexao.cursor()
            sessao.execute(string_sql, valores)
            conexao.commit()
            sessao.close()

        except psycopg2.Error:
            print("error")
        
        finally:
            if conn is not None:
                conn.close()
                
class Passagens:
    def __init__(self, origem, destino, duracao, conexao, preco):
        self.origem = origem
        self.destino = destino
        self.duracao = duracao
        self.conexao = conexao
        self.preco = preco

    def criaPassagem(dict):
        return Passagens(dict['origem'], dict['destino'], dict['duracao'], dict['conexao'], dict['preco'])
    
    def cadastraPassagem(self):
        string_sql = 'insert into turismo_schemas.passagem_aerea(origem, destino, duracao, conexao, preco) VALUES("sao paulo", "teste2", "teste", "2", 100);'
        novo_registro = (self.origem, self.destino, self.duracao, self.conexao, self.preco) 
        status = config.alteraBD(config, string_sql, novo_registro)
        return status

valor = Passagens.criaPassagem(dados['ida'][0])
print(valor)
Passagens.cadastraPassagem(valor)
#Corporation.cadastraCorporation(valor)
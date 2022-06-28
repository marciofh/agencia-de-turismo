import psycopg2
import requests
from datetime import datetime
import time

class cidade:
    def __init__(self, descricao, location_id, nome_cidade):
        self.descricao = descricao
        self.location_id = location_id
        self.nome_cidade = nome_cidade

    def criacidade(listaValores):
        return cidade(str(listaValores[0]), str(listaValores[1]), int(listaValores[2]), str(listaValores[3]))

    def cadastracidade(self):
        string_sql = 'INSERT INTO TurismoSD.cidade (descricao, location_id, nome_cidade) VALUES (%s, %d, %s);'
        novo_registro = (self.descricao, self.location_id, self.nome_cidade)
        status = config.alteraBD(config, string_sql, novo_registro)
        return status

class hospedagem:
    def __init__(self, nome_hotel, data_checkin, data_checkout, num_adulto, num_crianca, quartos, preco, rating, endereco, descricao, web_url, location_id):
        self.nome_hotel = nome_hotel
        self.data_checkin = data_checkin
        self.data_checkout = data_checkout
        self.num_adulto = num_adulto
        self.num_crianca = num_crianca
        self.quartos = quartos
        self.preco = preco
        self.ratig = rating
        self.endereco = endereco
        self.descricao = descricao
        self.web_url = web_url
        self.location_id = location_id


    def criahospedagem(listaValores):
        return hospedagem(str(listaValores[0]), datetime(listaValores[1]), datetime(listaValores[2]), int(listaValores[3]), int(listaValores[4]), str(listaValores[5]), float(listaValores[6]), str(listaValores[7]), str(listaValores[8], ), str(listaValores[9]), str(listaValores[10]), int(listaValores[11]))

    def cadastrahospedagem(self):
        string_sql = 'INSERT INTO TurismoSD.hospedagem (nome_hotel, data_checkin, data_checkout, num_adulto, num_crianca, quartos, preco,rating, endereco,descricao, web_url, location_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
        novo_registro = (self.nome_hotel, self.data_checkin, self.data_checkout, self.num_adulto, self.num_crianca, self.quartos, self.preco, self.rating, self.endereco, self.web_url, self.location_id) 
        status = config.alteraBD(config, string_sql, novo_registro)
        return status

class lazer:
    def __init__(self, nome, descricao_lazer, web_url, sub_categoria, open_now_text, location_id):
        self.nome = nome
        self.descricao_lazer = descricao_lazer
        self.web_url = web_url
        self.sub_categoria = sub_categoria
        self.open_now_text = open_now_text
        self.location_id = location_id
        

    def crialazer(listaValores):
        return lazer(str(listaValores[0]), str(listaValores[1]), str(listaValores[2]), str(listaValores[3]), float(listaValores[4]), int(listaValores[5]))

    def cadastralazer(self):
        string_sql = 'INSERT INTO TurismoSD.lazer (nome, descricao_lazer, web_url, sub_categoria, open_now_text, location_id) VALUES (%s, %s, %s, %s, %s, %s);'
        novo_registro = (self.nome, self.descricao_lazer, self.web_url, self.sub_categoria, self.open_now_text, self.location_id) 
        status = config.alteraBD(config, string_sql, novo_registro)
        return status

class passagem_aerea:
    def __init__(self, origem, destino, qtde_adulto, qtde_crianca, dateTime_partida, dateTime_chegada, duracao, conexao, valor, id_passagem):
        self.origem = origem
        self.destino = destino
        self.qtde_adulto = qtde_adulto
        self.qtde_crianca = qtde_crianca
        self.dateTime_partida = dateTime_partida
        self.dateTime_chegada = dateTime_chegada
        self.duracao = duracao
        self.duracao = conexao
        self.valor = valor
        self.id_passagem = id_passagem

    def criapassagem_aerea(listaValores):
        return passagem_aerea(str(listaValores[0]), str(listaValores[1]), int(listaValores[2]), int(listaValores[3]), datetime.strptime(listaValores[4]).date(), datetime.strptime(listaValores[5]).date(), str(listaValores[6]), str(listaValores[7]), float(listaValores[8]), int(listaValores[9]) )

    def cadastrapassagem_aerea(self):
        string_sql = 'INSERT INTO TurismoSD.stock_daily (origem, destino, qtde_adulto, qtde_crianca, dateTime_partida, dateTime_chegada, duracao, conexao, valor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
        novo_registro = (self.origem, self.destino, self.qtde_adulto, self.qtde_crianca, self.dateTime_partida, self.dateTime_chegada, self.duracao, self.conexao, self.valor, self.id_passagem) 
        status = config.alteraBD(config, string_sql, novo_registro)
        return status

class config:
    def __init__(self, dadosconexao):
        self.dadosconexao = dadosconexao

    def setParametros(self):
        self.dadosconexao = "host='localhost' dbname='TurismoSD' user='postgres' password='12345'"
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

def DecideFuncao(opcao, nome_cidade, location_id):
    tupla = []
    if opcao == 1:
        tupla = (location_id,  nome_cidade['Name'], nome_cidade['Description'], nome_cidade['Country'], nome_cidade['Address'], nome_cidade['Sector'], nome_cidade['Industry'])
        valor = cidade.criacidade(tupla)
        cidade.cadastracidade(valor)
        return

    if opcao == 2:
        tupla = (location_id,  nome_cidade['Name'], nome_cidade['Description'], nome_cidade['Country'], nome_cidade['Address'], nome_cidade['Sector'], nome_cidade['Industry'])
        valor = hospedagem.criahospedagem(tupla)
        hospedagem.cadashospedagem(valor)
        return 

    if opcao == 3:
        tupla = (location_id,  nome_cidade['Name'], nome_cidade['Description'], nome_cidade['Country'], nome_cidade['Address'], nome_cidade['Sector'], nome_cidade['Industry'])
        valor = lazer.crialazer(tupla)
        lazer.cadastralazer(valor)
        return 

    if opcao == 4:
        tupla = (location_id,  nome_cidade['Name'], nome_cidade['Description'], nome_cidade['Country'], nome_cidade['Address'], nome_cidade['Sector'], nome_cidade['Industry'])
        valor = passagem_aerea.criapassagem_aerea(tupla)
        passagem_aerea.cadastrapassagem_aerea(valor)
        return  
    

if __name__ == "__main__":
    # ordem de preenchimento de tabelas 
    ordem = [(1, 'cidade'), (2, 'hospedagem'), (3, 'lazer'), (4, 'passagem_aerea')]
    
    for ordenado in ordem:
        print('Populando tabela {0}'.format(ordenado[2]))
        # busca o resultado da API
        url = ('https://travel-advisor.p.rapidapi.com/locations/v2/auto-complete'.format(ordenado[1]))
        r = requests.get(url)
        data = r.json()
        print('Inserindo ' + ordem)
        # preenche o banco
        DecideFuncao(ordenado[0], data)
        # espera 12 segundos pois somente eh possivel fazer 5 requisicoes por minuto
        time.sleep(12)
        print('Tabela {0} totalmente populada'.format(ordenado[2]))
            

        

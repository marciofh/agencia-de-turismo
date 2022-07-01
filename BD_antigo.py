import psycopg2
import requests
from datetime import datetime
import time

class Corporation:
    def __init__(self, simbolo, nome, descricao, pais, endereco, setor, industria):
        self.simbolo = simbolo
        self.nome = nome
        self.descricao = descricao
        self.pais = pais
        self.endereco = endereco
        self.setor = setor
        self.industria = industria

    def criaCorporation(listaValores):
        return Corporation(str(listaValores[0]), str(listaValores[1]), str(listaValores[2]), str(listaValores[3]), str(listaValores[4]), str(listaValores[5]), str(listaValores[6]))

    def cadastraCorporation(self):
        string_sql = 'INSERT INTO stocks_data_base.corporation (simbolo, nome, descricao, pais, endereco, setor, industria) VALUES (%s, %s, %s, %s, %s, %s, %s);'
        novo_registro = (self.simbolo, self.nome, self.descricao, self.pais, self.endereco, self.setor, self.industria)
        status = config.alteraBD(config, string_sql, novo_registro)
        return status

class StockWeekly:
    def __init__(self, simbolo, preco_abertura, preco_fechamento, preco_high, preco_low, data, volume):
        self.simbolo = simbolo
        self.preco_abertura = preco_abertura
        self.preco_fechamento = preco_fechamento
        self.preco_high = preco_high
        self.preco_low = preco_low
        self.data = data
        self.volume = volume

    def criaStockWeekly(listaValores):
        return StockWeekly(str(listaValores[0]), float(listaValores[1]), float(listaValores[2]), float(listaValores[3]), float(listaValores[4]), datetime.strptime(listaValores[5], '%Y-%m-%d').date(), int(listaValores[6]))

    def cadastraStockWeekly(self):
        string_sql = 'INSERT INTO stocks_data_base.stock_weekly (simbolo, preco_abertura, preco_fechamento, preco_high, preco_low, data, volume) VALUES (%s, %s, %s, %s, %s, %s, %s);'
        novo_registro = (self.simbolo, self.preco_abertura, self.preco_fechamento, self.preco_high, self.preco_low, self.data, self.volume) 
        status = config.alteraBD(config, string_sql, novo_registro)
        return status

class StockMonthly:
    def __init__(self, simbolo, preco_abertura, preco_fechamento, preco_high, preco_low, data, volume):
        self.simbolo = simbolo
        self.preco_abertura = preco_abertura
        self.preco_fechamento = preco_fechamento
        self.preco_high = preco_high
        self.preco_low = preco_low
        self.data = data
        self.volume = volume

    def criaStockMonthly(listaValores):
        return StockMonthly(str(listaValores[0]), float(listaValores[1]), float(listaValores[2]), float(listaValores[3]), float(listaValores[4]), datetime.strptime(listaValores[5], '%Y-%m-%d').date(), int(listaValores[6]))

    def cadastraStockMonthly(self):
        string_sql = 'INSERT INTO stocks_data_base.stock_monthly (simbolo, preco_abertura, preco_fechamento, preco_high, preco_low, data, volume) VALUES (%s, %s, %s, %s, %s, %s, %s);'
        novo_registro = (self.simbolo, self.preco_abertura, self.preco_fechamento, self.preco_high, self.preco_low, self.data, self.volume) 
        status = config.alteraBD(config, string_sql, novo_registro)
        return status

class StockDaily:
    def __init__(self, simbolo, preco_abertura, preco_fechamento, preco_high, preco_low, data, volume):
        self.simbolo = simbolo
        self.preco_abertura = preco_abertura
        self.preco_fechamento = preco_fechamento
        self.preco_high = preco_high
        self.preco_low = preco_low
        self.data = data
        self.volume = volume

    def criaStockDaily(listaValores):
        return StockDaily(str(listaValores[0]), float(listaValores[1]), float(listaValores[2]), float(listaValores[3]), float(listaValores[4]), datetime.strptime(listaValores[5], '%Y-%m-%d').date(), int(listaValores[6]))

    def cadastraStockDaily(self):
        string_sql = 'INSERT INTO stocks_data_base.stock_daily (simbolo, preco_abertura, preco_fechamento, preco_high, preco_low, data, volume) VALUES (%s, %s, %s, %s, %s, %s, %s);'
        novo_registro = (self.simbolo, self.preco_abertura, self.preco_fechamento, self.preco_high, self.preco_low, self.data, self.volume) 
        status = config.alteraBD(config, string_sql, novo_registro)
        return status

class InformationsEconomic:
    def __init__(self, simbolo, retorno_ativo, retorno_patrimonio, dividend_yield, beta, price_sale, margin_profit, market_cap, analyst_target_price, quarterly_revenue_growth_YOY, quarterly_earnings_growth_YOY):
        self.simbolo = simbolo
        self.retorno_ativo = retorno_ativo 
        self.retorno_patrimonio = retorno_patrimonio 
        self.dividend_yield = dividend_yield 
        self.beta = beta 
        self.price_sale = price_sale
        self.margin_profit = margin_profit 
        self.market_cap = market_cap
        self.analyst_target_price = analyst_target_price
        self.quarterly_revenue_growth_YOY = quarterly_revenue_growth_YOY
        self.quarterly_earnings_growth_YOY = quarterly_earnings_growth_YOY
        
    def criaInformationsEconomic(listaValores):
        return InformationsEconomic(str(listaValores[0]), float(listaValores[1]), float(listaValores[2]), float(listaValores[3]), float(listaValores[4]), float(listaValores[5]), float(listaValores[6]), float(listaValores[7]), float(listaValores[8]), float(listaValores[9]), float(listaValores[10]))

    def cadastraInformationsEconomic(self):
        string_sql = 'INSERT INTO stocks_data_base.informations_economics (simbolo, retorno_ativo, retorno_patrimonio, dividend_yield, beta, price_sale, margin_profit, market_cap, analyst_target_price, quarterly_revenue_growth_YOY, quarterly_earnings_growth_YOY) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
        novo_registro = (self.simbolo, self.retorno_ativo, self.retorno_patrimonio, self.dividend_yield, self.beta,
                        self.price_sale, self.margin_profit, self.market_cap, self.analyst_target_price, self.quarterly_revenue_growth_YOY, 
                        self.quarterly_earnings_growth_YOY) 
        status = config.alteraBD(config, string_sql, novo_registro)
        return status

class config:
    def __init__(self, dadosconexao):
        self.dadosconexao = dadosconexao

    def setParametros(self):
        self.dadosconexao = "host='localhost' dbname='StockDataBase' user='postgres' password='12345'"
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

def DecideFuncao(opcao, data, simbolo):
    tupla = []
    stocks = []
    if opcao == 1:
        tupla = (simbolo,  data['Name'], data['Description'], data['Country'], data['Address'], data['Sector'], data['Industry'])
        
        
        
        valor = Corporation.criaCorporation(tupla)
        Corporation.cadastraCorporation(valor)
         
        
        
        
        return 
    if opcao == 2:
        tupla = (simbolo, data['ReturnOnAssetsTTM'], data['ReturnOnEquityTTM'], data['DividendYield'], data['Beta'], data['PriceToSalesRatioTTM'], data['ProfitMargin'], data['MarketCapitalization'], data['AnalystTargetPrice'], data['QuarterlyRevenueGrowthYOY'], data['QuarterlyEarningsGrowthYOY'])
        valor = InformationsEconomic.criaInformationsEconomic(tupla)
        InformationsEconomic.cadastraInformationsEconomic(valor)
        return
    if opcao == 3:
        for date in data["Time Series (Daily)"]:
            stock = data["Time Series (Daily)"][date]
            tupla = (simbolo, stock['1. open'], stock['4. close'], stock['2. high'], stock['3. low'], date, stock['6. volume'])
            stocks.append(tupla)
        for valores in stocks:
            valor = StockDaily.criaStockDaily(valores)
            StockDaily.cadastraStockDaily(valor)
        return
    if opcao == 4:
        for date in data["Weekly Adjusted Time Series"]:
            stock = data["Weekly Adjusted Time Series"][date]
            tupla = (simbolo, stock['1. open'], stock['4. close'], stock['2. high'], stock['3. low'], date, stock['6. volume'])
            stocks.append(tupla)
        for valores in stocks:
            valor = StockWeekly.criaStockWeekly(valores)
            StockWeekly.cadastraStockWeekly(valor)
        return
    if opcao == 5:
        for date in data["Monthly Adjusted Time Series"]:
            stock = data["Monthly Adjusted Time Series"][date]
            tupla = (simbolo, stock['1. open'], stock['4. close'], stock['2. high'], stock['3. low'], date, stock['6. volume'])
            stocks.append(tupla)
        for valores in stocks:
            valor = StockMonthly.criaStockMonthly(valores)
            StockMonthly.cadastraStockMonthly(valor)
        return

if __name__ == "__main__":
    # acoes para insercao no banco    
    listaAtivos = [ 'IRBT', 'UPWK', 'FVRR', 'RDFN', 'BYND', 'ETSY', 'TDOC', 'ZG', 'ROKU', 'MO', 'MELI', 'SQ', 'SE', 'PM', 'CRM', 'DIS', 'AMZN', 'NVDA', 'ORCL', 
                    'KO', 'INTC', 'UNH', 'BABA', 'MA', 'BAC', 'JPM', 'TSM', 'JNJ', 'WMT','TSLA', 'MSFT', 'AAPL']
    # ordem de preenchimento de tabelas 
    ordem = [(1, 'OVERVIEW', 'corporation'), (2, 'OVERVIEW', 'informations_economics'), (3, 'TIME_SERIES_DAILY_ADJUSTED', 'stock_daily'), (4, 'TIME_SERIES_WEEKLY_ADJUSTED', 'stock_weekly'), (5, 'TIME_SERIES_MONTHLY_ADJUSTED', 'stock_monthly')]
    
    for ordenado in ordem:
        print('Populando tabela {0}'.format(ordenado[2]))
        for ativo in listaAtivos:
            # busca o resultado da API
            url = ('https://www.alphavantage.co/query?function={0}&symbol={1}&apikey=VPA90PVOIW5AX6Z2'.format(ordenado[1], ativo))
            r = requests.get(url)
            data = r.json()
            print('Inserindo ' + ativo)
            # preenche o banco
            DecideFuncao(ordenado[0], data, ativo)
            # espera 12 segundos pois somente eh possivel fazer 5 requisicoes por minuto
            time.sleep(12)
        print('Tabela {0} totalmente populada'.format(ordenado[2]))
            

        

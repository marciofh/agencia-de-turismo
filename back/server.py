from flask import Flask, request

app = Flask(__name__)

resposta = ''

@app.route("/passagem", methods = ['GET'])
def retornaPassagem():
    return resposta

@app.route("/locationId", methods = ['POST'])
def index():
    data = request.json['data']
    #CONSULTA CIDADE
    consultaCidade(data['origem'])
    
    #SE NÃO TEM
    getLocationId(data['origem'])#API
    #add cidade no banco
    #add cidade na resposta
    
    #SE TEM CIDADE
    #add cidade na resposta
    consultaPassagem(data)
    resposta

    #SE TEM PASSAGEM
    #add passagem na resposta e retorna

    #SE NÃO TEM PASSAGEM
    getPassagem(data)#CRAwLER
    #add passagem no banco
    #add passagem na resposta e retorna
    
    return 'RETORNO DO BACK' #RETORNAR CIDADE E PASSAGENS

#FUNÇÕES
def consultaCidade(cidade):
    pass

def consultaPassagem(data):
    pass

def getLocationId(cidade):
    pass

def getPassagem(data):
    pass

if __name__ == "__main__":
    app.run()



from flask import Flask, render_template, request
from crawler import Crawler

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/passagem", methods=["POST"])
def passagem():
    origem = request.form.get('origem')
    destino = request.form.get('destino')
    passageiros = request.form.get('passageiro')
    data_ida = request.form.get('data_ida')
    data_volta = request.form.get('data_volta')
    
    crawler = Crawler()
    list_section = crawler.send_dados(origem, destino, passageiros, data_ida, data_volta)
    dados = crawler.get_dados(list_section)

    #dados = {'ida': [{'origem': 'VCP - 05:55', 'destino': 'SSA - 08:15', 'duracao': ' 02:20', 'conexao': ' Direto ', 'preco': ' R$ 1.899,55 '}, {'origem': 'VCP - 11:45', 'destino': 'SSA - 14:05', 'duracao': ' 02:20', 'conexao': ' Direto ', 'preco': ' R$ 1.899,55 '}, {'origem': 'VCP - 06:10', 'destino': 'SSA - 10:30', 'duracao': ' 04:20', 'conexao': ' 1 parada ', 'preco': ' R$ 2.657,55 '}, {'origem': 'VCP - 19:50', 'destino': 'SSA - 00:20', 'duracao': ' 04:30', 'conexao': ' 1 parada ', 'preco': ' R$ 2.657,55 '}, {'origem': 'VCP - 18:15', 'destino': 'SSA - 23:15', 'duracao': ' 05:00', 'conexao': ' 1 parada ', 'preco': ' R$ 2.657,55 '}, {'origem': 'VCP - 11:00', 'destino': 'SSA - 19:10', 'duracao': ' 08:10', 'conexao': ' 1 parada ', 'preco': ' R$ 2.657,55 '}, {'origem': 'VCP - 06:10', 'destino': 'SSA - 14:30', 'duracao': ' 08:20', 'conexao': ' 1 parada ', 'preco': ' R$ 2.657,55 '}], 'volta': [{'origem': 'SSA - 15:05', 'destino': 'VCP - 17:35', 'duracao': ' 02:30', 'conexao': ' Direto ', 'preco': ' R$ 756,45 '}, {'origem': 'SSA - 20:35', 'destino': 'VCP - 23:05', 'duracao': ' 02:30', 'conexao': ' Direto ', 'preco': ' R$ 756,45 '}, {'origem': 'SSA - 06:00', 'destino': 'VCP - 11:05', 'duracao': ' 05:05', 'conexao': ' 1 parada ', 'preco': ' R$ 2.659,45 '}, {'origem': 'SSA - 15:10', 'destino': 'VCP - 21:30', 'duracao': ' 06:20', 'conexao': ' 1 parada ', 'preco': ' R$ 2.659,45 '}, {'origem': 'SSA - 15:10', 'destino': 'VCP - 23:05', 'duracao': ' 07:55', 'conexao': ' 1 parada ', 'preco': ' R$ 2.659,45 '}, {'origem': 'SSA - 17:45', 'destino': 'VCP - 23:05', 'duracao': ' 05:20', 'conexao': ' 1 parada ', 'preco': ' R$ 2.659,45 '}]}
    
    return render_template('passagens.html', content = dados)

@app.route("/hospedagem", methods=["POST"])
def hospedagem():
    voo_ida = request.form.get('voo_ida')
    voo_volta = request.form.get('voo_volta')

    res = {
        'voo_ida': voo_ida,
        'voo_volta': voo_volta
        }
    return res

if __name__ == "__main__":
    app.run()
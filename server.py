from flask import Flask, render_template, request
from crawler import Crawler
from api import Api

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

    #consulta cidade destino
    #NÃO TEM CIDADE     #quer dizer que o destino não foi pesquisando, nao tem passagem nem hotel
    crawler = Crawler()
    list_section = crawler.send_dados(origem, destino, passageiros, data_ida, data_volta)
    passagens = crawler.get_dados(list_section)
    #cadastra passagem
    #returna passagem

    #TEM CIDADE     #quer dizer que destino ja foi pesquisado, pode ter passagem e hotel (depende da data)
    #consulta passagem pela origem, data_ida
    #consulta passagem pelo destino, data_volta
        #NÃO TEM PASSAGEM
        # crawler = Crawler()
        # list_section = crawler.send_dados(origem, destino, passageiros, data_ida, data_volta)
        # passagens = crawler.get_dados(list_section)
        # #cadastra passagem
        # #retorna passagem

        #TEM PASSAGEM
        #retorna passagem

    return render_template('passagens.html', content = passagens)
    
@app.route("/hospedagem", methods=["POST"])
def hospedagem():
    voo_ida = request.form.get('voo_ida')
    voo_volta = request.form.get('voo_volta')    
    
    #id = Api.get_locationId(destino)
    #cadastra cidade

    #hoteis = Api.get_hotels(id, passageiros, data_ida, data_volta)
    #cadastra hotel


    res = {
        'voo_ida': voo_ida,
        'voo_volta': voo_volta
        }
    return res


if __name__ == "__main__":
    app.run()
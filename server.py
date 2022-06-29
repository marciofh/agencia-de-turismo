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
    
    return dados

if __name__ == "__main__":
    app.run()
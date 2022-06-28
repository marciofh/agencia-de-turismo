from flask import Flask, render_template, request
from 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/passagem", methods=["POST"])
def passagem():
    origem = request.form.get('origem')
    destino = request.form.get('destino')
    data_ida = request.form.get('data_ida')
    data_volta = request.form.get('data_volta')
    

    
    return 'oi'

if __name__ == "__main__":
    app.run()
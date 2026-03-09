from flask import Flask

app = Flask(__name__)

@app.route('/')
def casa():
    return 'Você estar em casa!'

@app.route('/Sobre')
def sobre():
    return 'Quer saber mais o que'
@app.route('/Livros')
def Livros():
    return 'Quer fica esperto ne, aqui teu livro'

@app.route("/Autores")
def Autores():
    return "Se você saber esses autores.... sabe muito"

if __name__ == '__main__':
    app.run(debug=True)

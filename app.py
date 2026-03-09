from flask import Flask

app = Flask(__name__)

@app.route('/')
def casa():
    return 'Você estar em casa!'

@app.route('/Sobre')
def sobre():
    return 'Quer saber mais o que'
@app.route('/Livros')
def LIvros():
    return 'Quer fica esperto ne, aqui teu livro'

if __name__ == '__main__':
    app.run(debug=True)

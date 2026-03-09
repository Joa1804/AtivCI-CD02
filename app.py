from flask import Flask

app = Flask(__name__)

@app.route('/')
def casa():
    return 'Você estar em casa!'

@app.route('/sobre')
def sobre():
    return 'Quer saber mais o que'


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request
import table

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Pact groupe 6.1\nConsEcolo"

@app.route("/somme/<a>/<b>")
def somme(a, b):
    return f"{a} + {b} = {int(a)+int(b)}"

@app.route("/sommeQuerry")
def sommeQ():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f"{a} + {b} = {a+b}"

@app.route("/deplacement")
def deplacement():
    return "Déplacement"

@app.route("/reponse/<question>/<reponse>")
def reponse(question, reponse):
    return "reponse"

@app.route("/getQuestion")
def getQuestion():
    return "question"

@app.route("/getConso")
def getConso():
    return str(table.getConso(request.args.get('id')))

@app.route("/classement")
def classement():
    return table.getRank()

@app.route("/achat")
def achat():
    return "achat"

@app.route("/delete")
def delete():
    return "delete"

@app.route("/getGlobal")
def getGlobal():
    return str(table.getMean())

@app.route("/setArticle")
def setArticle():
    return "Donner la consommation d'un article"

@app.route("/createAccount")
def createAccount():
    return "Créer un compte"

if __name__ == "__main__":
    app.run()
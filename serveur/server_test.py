from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Pact groupe 6.1\nConsEcolo"

@app.route("/somme/<a>/<b>")
def somme(a, b):
    return f"{a} + {b} = {int(a)+int(b)}"

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
    return "conso"

@app.route("/classement")
def classement():
    return "classement"

@app.route("/achat")
def achat():
    return "achat"

@app.route("/delete")
def delete():
    return "delete"

@app.route("/getConso")
def delete():
    return "Votre consommation"

@app.route("/getRank")
def delete():
    return "Votre classement"

@app.route("/getGlobal")
def delete():
    return "Consommation Globale"

@app.route("/setArticle")
def delete():
    return "Donner la consommation d'un article"

@app.route("/createAccount")
def delete():
    return "Créer un compte"

if __name__ == "__main__":
    app.run()
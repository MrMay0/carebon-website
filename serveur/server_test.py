from flask import Flask, request, render_template
import table
import os, sys

app = Flask(__name__)

os.chdir(sys.path[0])

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


@app.route("/getBadge")
def getBadge():
    return "Vos Badges"


@app.route("/homePage")
def goHome():
    return render_template("index.html")

@app.route("/read")
def read():
    with open(r"data.txt", 'r') as file:
        text = file.readlines()
        line = int(request.args.get('line'))
        print(text)
        if len(text) > line:
            return text[line]
        else:
            return "Donnée introuvable"

@app.route("/write")
def write():
    with open(r"data.txt", 'a') as file:
        file.write("\n" + request.args.get("text"))
    return "Données écrites"


if __name__ == "__main__":
    app.run()

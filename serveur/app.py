from flask import Flask, request, render_template
import table
import os, sys
import subprocess
from flask import jsonify

app = Flask(__name__)

os.chdir(sys.path[0])

@app.route("/")
def hello_world():
    return "Pact groupe 6.1 CareBon Test"


@app.route("/somme/<a>/<b>")
def somme(a, b):
    return f"{a} + {b} = {int(a)+int(b)}"


@app.route("/sommeQuerry")
def sommeQ():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f"{a} + {b} = {a+b}"


@app.route("/sommeJson/<a>/<b>")
def sommeJson(a, b):
    return jsonify(
                value=int(a)+int(b),
                message=f"{a} + {b} = {int(a)+int(b)}"
            )

@app.route("/sommePOST", methods=['POST'])
def sommePOST():
    data = request.get_json()
    a = data['a']
    b = data['b']
    return jsonify(
                value= a+b,
                message=f"{a} + {b} = {a+b}"
            )


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
    with open("data/data.txt", 'r') as file:
        text = file.readlines()
        line = int(request.args.get('line'))
        print(text)
        if len(text) > line:
            return text[line]
        else:
            return "Donnée introuvable"

@app.route("/write")
def write():
    with open("data/data.txt", 'a') as file:
        file.write("\n" + request.args.get("text"))
    return "Données écrites"


if __name__ == "__main__":
    app.run()
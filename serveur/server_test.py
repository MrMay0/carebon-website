from flask import Flask

app = Flask(__name__)

class Question:
    def __init__(self, text, choices, values):
        self.text = text
        self.choices = choices
        self.values = values

def discrete_to_func(choices, values):
    def func(choice):
        for i in range(len(choices)):
            if choices[i] == choice:
                return values[i]
        return "non valide"
    return lambda x: func(x)

questionnaire = {'1': Question("Combien de mètre carrés fait la maison ?", ("20 m²", "40m²", "100m²"),
                discrete_to_func(("20", "40", "100"), (200, 400, 1000))),
                '2': Question("Distance parcourue ?", None, lambda x: 10*x)}

@app.route("/")
def hello_world():
    return "<p> Hello, World! </p>"

@app.route("/somme/<a>/<b>")
def somme(a, b):
    return f"<p> {a} + {b} = {int(a)+int(b)} </p>"

@app.route("/deplacement")
def deplacement():
    return "<p> Déplacement </p>"

@app.route("/reponse/<question>/<reponse>")
def reponse(question, reponse):
    print(question, reponse)
    print(type(question), type(reponse))
    ans = questionnaire[question].values(reponse)
    return f"<p> {ans} </p>"

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

if __name__ == "__main__":
    app.run()
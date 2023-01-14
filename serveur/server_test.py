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

@app.route("/trajet")
def trajet():
    return "<p> Déplacement </p>"

@app.route("/questionnaire/<question>/<reponse>")
def questionnaire(question, reponse):
    print(question, reponse)
    print(type(question), type(reponse))
    ans = questionnaire[question].values(reponse)
    return f"<p> {ans} </p>"


@app.route("/somme/<a>/<b>")
def somme(a, b):
    return f"<p> {a} + {b} = {a+b} </p>"
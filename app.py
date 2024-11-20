from flask import Flask, render_template, redirect
import json
import fonct

app = Flask(__name__)

with open("./data/catalogue.json","r") as cataR:
    dico = json.load(cataR)
    
with open("./data/inventaire.json","r") as invR:
    inv =  json.load(invR)

@app.route("/")
def home():
    return redirect("http://127.0.0.1:5000/home")

@app.route("/home")
def homes():
    return render_template("home.html")

@app.route("/tout")
def tout():
    return render_template("tout.html",Lvelo = dico)

@app.route("/dispos")
def dispos():
    return render_template("dispos.html")

@app.route("/velo/<code>")
def velo(code):
    return render_template("velo.html", velo = dico[code])


if __name__=="__main__":
    app.run(debug=True)
    
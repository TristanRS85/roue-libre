from flask import Flask, render_template, redirect, request
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
    return render_template("dispos.html",Lvelo = fonct.dispo())

@app.route("/velo/<code>")
def velo(code):
    return render_template("velo.html", velo = dico[code])

@app.route("/achat/<code>")
def achat(code):
    return render_template("achat.html",velo = code)

@app.route("/envoieAchat/<velo>", methods=["POST"])
def formuAchat(velo):
    numSerie = fonct.retirerVelo(velo)
    nom = request.form.get("nom")
    email = request.form.get("email")
    tel = request.form.get("tel")
    fonct.ajoutVente(velo,numSerie,nom,email,tel)
    return render_template("home.html")

if __name__=="__main__":
    app.run(debug=True)
    
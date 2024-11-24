from flask import Flask, render_template, redirect, request, jsonify
import json
import fonct

app = Flask(__name__)
app.secret_key = "superCle"

with open("./data/catalogue.json","r") as cataR:
    dico = json.load(cataR)
    
with open("./data/inventaire.json","r") as invR:
    inv =  json.load(invR)

with open("./data/utilisateur.json","r") as userR:
    user =  json.load(userR)

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

@app.route("/login")
def login():
    return render_template("login.html")

@app.route('/dashboard', methods=["POST"])
def dashboard():
    id = request.form.get("id")
    mdp = request.form.get("mdp")
    if id in user and user[id] == mdp:
        return render_template("dash.html")
    else:
        return render_template("home.html")

@app.route('/ajouter-velo', methods=['POST'])
def ajouter_velo():
    data = request.json 
    id = data.get('id')
    nom = data.get('nom')
    descCourte = data.get('descCourte')
    descLongue = data.get('descLongue')
    
    resultat = fonct.nouveauVelo(id, nom, descCourte, descLongue)
    
    return jsonify({"message": resultat})

if __name__=="__main__":
    app.run(debug=True)
    
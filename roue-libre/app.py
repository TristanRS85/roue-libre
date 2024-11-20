from flask import Flask, render_template, redirect
import json

app = Flask(__name__)

with open("./data/catalogue.json","r") as cataR:
    dico = json.load(cataR)
    
with open("./data/inventaire.json","r") as invR:
    inv =  json.load(invR)

def nouveauVelo(id,nom,descCourte,descLongue):
    if id not in dico.keys():
        dico[id]={}
        dico[id]["nom"]=nom
        dico[id]["descCourte"]=descCourte
        dico[id]["descLongue"]=descLongue
        with open("./data/catalogue.json","w") as cataW:
            json.dump(dico, cataW)
        inv[id]={}
        inv[id]["numeroSerie"]=[id+"1"]
        with open("./data/inventaire.json","w") as invW:
            json.dump(inv, invW)
    else:
        temp = inv[id]["numeroSerie"]
        temp.append(id+str(int(temp[len(temp)-1][3:])+1))
        inv[id]["numeroSerie"]= temp
        with open("./data/inventaire.json","w") as invW:
            json.dump(inv, invW)
    

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
    
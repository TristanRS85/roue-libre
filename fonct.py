import json

with open("./data/catalogue.json","r") as cataR:
    dico = json.load(cataR)
    
with open("./data/inventaire.json","r") as invR:
    inv =  json.load(invR)

with open("./data/vente.json","r") as venteR:
    vente =  json.load(venteR)

def nouveauVelo(id,nom,descCourte,descLongue):
    if id in dico.keys():
        temp = inv[id]["numeroSerie"]
        temp.append(id+str(int(temp[len(temp)-1][3:])+1))
        inv[id]["numeroSerie"]= temp
        with open("./data/inventaire.json","w") as invW:
            json.dump(inv, invW)  
    else:
        try:
            if(id==""or nom=="" or descCourte=="" or descLongue=="" or len(id)!=3):
                return "veuillez vérifier les champs"
            else:
                int(id)
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
        except:
            return "veuillez vérifier les champs"
    return "succès"
    
def dispo():
    dico2={}
    for id in dico.keys():
        if len(inv[id]["numeroSerie"])!=0:
            dico2[id]=dico[id]
    return dico2

def retirerVelo(id):
    res = inv[id]["numeroSerie"][0]
    inv[id]["numeroSerie"].pop(0)
    with open("./data/inventaire.json","w") as invW:
            json.dump(inv, invW)
    return res

def ajoutVente(code,numSerie,nom,email,tel):
    vente[numSerie]={}
    vente[numSerie]["code"]=code
    vente[numSerie]["nom"]=nom
    vente[numSerie]["email"]=email
    vente[numSerie]["tel"]=tel
    with open("./data/vente.json","w") as venteW:
            json.dump(vente, venteW)
import json

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
    
def dispo():
    dico2={}
    for id in dico.keys():
        if len(inv[id]["numeroSerie"])!=0:
            dico2[id]=dico[id]
    return dico2

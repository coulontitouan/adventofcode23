print("-------------1ere partie-------------")

print(sum([__import__('math').floor(pow(2,len(set([[j for j in i.split(" ") if j != ""] for i in ligne.split(":")[1].replace("  "," ").replace("\n","").split("|")][1]).intersection(set([[j for j in i.split(" ") if j != ""] for i in ligne.split(":")[1].replace("  "," ").replace("\n","").split("|")][0])))-1)) for ligne in open("input.txt", "r")]))

print("-------------2eme partie-------------")

with open("input.txt", "r") as fichier:
    dico = dict()
    for ligne in fichier:
        dico[int(ligne.split(":")[0].split(" ")[-1])] = dico.get(int(ligne.split(":")[0].split(" ")[-1]),0)+1
        for i in range(1,len(set([[j for j in i.split(" ") if j != ""] for i in ligne.split(":")[1].replace("  "," ").replace("\n","").split("|")][1]).intersection(set([[j for j in i.split(" ") if j != ""] for i in ligne.split(":")[1].replace("  "," ").replace("\n","").split("|")][0])))+1):
            dico[int(ligne.split(":")[0].split(" ")[-1])+i] = dico.get(int(ligne.split(":")[0].split(" ")[-1])+i,0) + dico[int(ligne.split(":")[0].split(" ")[-1])]

print(sum(dico.values()))
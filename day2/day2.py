print("-------------1ere partie-------------")

print(sum([int(ligne.split(':')[0].split(' ')[1]) for ligne in open("input.txt", "r") if sum([{"red":12,"green":13,"blue":14}[ligne.split(":")[1][1:].replace(";","").replace("\n","").replace(",","").split(" ")[i+1]] >= int(ligne.split(":")[1][1:].replace(";","").replace("\n","").replace(",","").split(" ")[i]) for i in range(0,len(ligne.split(":")[1][1:].replace(";","").replace("\n","").replace(",","").split(" ")),2)]) / len([{"red":12,"green":13,"blue":14}[ligne.split(":")[1][1:].replace(";","").replace("\n","").replace(",","").split(" ")[i+1]] >= int(ligne.split(":")[1][1:].replace(";","").replace("\n","").replace(",","").split(" ")[i]) for i in range(0,len(ligne.split(":")[1][1:].replace(";","").replace("\n","").replace(",","").split(" ")),2)]) == 1]))

print("-------------2eme partie-------------")

with open("input.txt", "r") as fichier:
    somme = 0
    for ligne in fichier:
        maxi = {"red":0,"green":0,"blue":0}
        for i in range(0,len(ligne.split(":")[1].replace("\n","").replace(",","").replace(";","").split(" ")[1:]),2):
            maxi[ligne.split(":")[1].replace("\n","").replace(",","").replace(";","").split(" ")[1:][i+1]] = max(maxi[ligne.split(":")[1].replace("\n","").replace(",","").replace(";","").split(" ")[1:][i+1]],int(ligne.split(":")[1].replace("\n","").replace(",","").replace(";","").split(" ")[1:][i]))
        mult = 1
        for j in maxi.values():
            mult *= j
        somme += mult
print(somme)

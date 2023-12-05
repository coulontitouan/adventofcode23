print("-------------1ere partie-------------")

with open("input.txt", "r") as fichier:
    somme = 0
    y = 0
    dernier_chiffre = 0
    lignes = fichier.readlines()
    def construit_chiffre(x,y):
        chiffre = ""
        while x < 140 and lignes[y][x].isnumeric() :
            chiffre+=str(lignes[y][x])
            x+=1
        return chiffre
    def verif_symbole(x,y,longueur):
        verify = -1
        while verify < 2:
            verifx = -1
            while verifx < longueur+int(x<138):
                if y+verify < 0:
                    verify+=1
                if x+verifx < 0:
                    verifx+=1
                if x+verifx > 139 or y+verify > 139:
                    break
                symbole = lignes[y+verify][x+verifx]
                if symbole != "." and not symbole.isnumeric():
                    return True
                verifx+=1
            verify+=1
        return False
    while y < len(lignes):
        x = 0
        while x < len(lignes[y]):
            symbole =lignes[y][x]
            if symbole.isnumeric():
                chiffre = int(construit_chiffre(x,y))
                if verif_symbole(x,y,len(str(chiffre))):
                    somme+=chiffre
                x+=len(str(chiffre))-1
            x+=1
        y+=1

print(somme)

print("-------------2eme partie-------------")

with open("input.txt", "r") as fichier:
    somme = 0
    y = 0
    lignes = fichier.readlines()
    def construit_chiffre(x,y):
        chiffre = lignes[y][x]
        try:
            countmoins = -1
            countplus = 1
            while lignes[y][x+countmoins].isnumeric():
                chiffre = f"{lignes[y][x+countmoins]}{chiffre}"
                countmoins -= 1
            while lignes[y][x+countplus].isnumeric():
                chiffre = f"{chiffre}{lignes[y][x+countplus]}"
                countplus += 1
        except IndexError:
            pass
        return int(chiffre)
    def ratio(x,y,count):
        alentours = set()
        verify = -1
        while verify < 2:
            verifx = -1
            while verifx < 2:
                if y+verify < 0:
                    verify+=1
                if x+verifx < 0:
                    verifx+=1
                if x+verifx > 139 or y+verify > 139:
                    break
                symbole = lignes[y+verify][x+verifx]
                if symbole.isnumeric():
                    alentours.add(construit_chiffre(x+verifx,y+verify))
                verifx+=1
            verify+=1
        if len(alentours) == 2:
            res = 1
            for i in alentours:
                res *=i
            return res
        return 0
    count=0
    while y < len(lignes):
        x = 0
        while x < len(lignes[y]):
            symbole =lignes[y][x]
            if symbole == "*":
                somme += ratio(x,y,count)
                count+=1
            x+=1
        y+=1


print(somme)
print("-------------1ere partie-------------")

def trouvepremier(chaine:str):
    for i in chaine:
        if i.isnumeric():
            return i
def trouvedernier(chaine:str):
    for i in reversed(chaine):
        if i.isnumeric():
            return i 
        
with open('input.txt', 'r') as fichier:
    sum = 0
    for ligne in fichier:
        sum += int(f"{trouvepremier(ligne)}{trouvedernier(ligne)}")
print(sum)

print("-------------2eme partie-------------")

mots = ["one", "two", "three", "four", "five", "six", "seven", "eight","nine"]

def remplace(chaine:str):
    for mot in mots:
        chaine = chaine.replace(mot,f"{mot[0]}{str(mots.index(mot)+1)}{mot[-1]}")
    return chaine

with open('input.txt', 'r') as fichier:
    sum = 0
    for ligne in fichier:
        sum += int(f"{trouvepremier(remplace(ligne))}{trouvedernier(remplace(ligne))}")
print(sum)
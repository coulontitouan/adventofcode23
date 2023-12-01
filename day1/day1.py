print("-------------1ere partie-------------")
 
with open('input.txt', 'r') as fichier:
    sum = 0
    for ligne in fichier:
        sum += int(f"{[i for i in ligne if i.isnumeric()][0]}{[i for i in reversed(ligne) if i.isnumeric()][0]}")
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
        sum += int(f"{[i for i in remplace(ligne) if i.isnumeric()][0]}{[i for i in reversed(remplace(ligne)) if i.isnumeric()][0]}")
print(sum)
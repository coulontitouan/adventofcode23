print("-------------1ere partie-------------")

with open("input.txt", "r") as fichier:
    seeds = fichier.readlines()[0].replace("\n","").split(": ")[1].split(" ")
    print(seeds)
    locations = list()
    for ligne in fichier:
        if ligne.contains("-to-"):
            from,to = ligne.split("-to-")
            
print(min(locations))

print("-------------2eme partie-------------")

mots = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("input.txt", "r") as fichier:
    for ligne in fichier:
        pass
class Race:
    def __init__(self,duration,record) -> None:
        self.duration = duration
        self.record = record
        self.solutions = 0
    def __str__(self) -> str:
        return f"Durée : {self.duration} Record : {self.record} Solutions : {self.solutions}"

print("-------------1ere partie-------------")

with open("input.txt", "r") as fichier:
    races = list()
    lignes = fichier.readlines()
    for i in range(len(lignes)):
        lignes[i] = lignes[i].replace("\n","")
        while lignes[i].__contains__("  "):
            lignes[i] = lignes[i].replace("  "," ")
        lignes[i] = lignes[i].split(": ")[1].split(" ")
    for i in range(len(lignes[0])):
        races.append(Race(int(lignes[0][i]),int(lignes[1][i])))
    res = 1
    for r in races:
        for speed in range(1,r.duration):
            temps_restant=r.duration-speed
            if temps_restant*speed > r.record:
                r.solutions+=1
        res *= r.solutions

print(res)

print("-------------2eme partie-------------")

with open("input.txt", "r") as fichier:
    races = list()
    lignes = fichier.readlines()
    for i in range(len(lignes)):
        lignes[i] = lignes[i].replace("\n","")
        while lignes[i].__contains__("  "):
            lignes[i] = lignes[i].replace(" ","")
        lignes[i] = lignes[i].split(":")[1].split(" ")
    for i in range(len(lignes[0])):
        races.append(Race(int(lignes[0][i]),int(lignes[1][i])))
    res = 1
    for r in races:
        for speed in range(1,r.duration):
            temps_restant=r.duration-speed
            if temps_restant*speed > r.record:
                r.solutions+=1
        res *= r.solutions

print(res)
import os
for i in range(1,26):
    try:
        os.mkdir(f"day{i}",mode=511)
        if not os.path.isfile(f"day{i}/day{i}.py"):
            open(f"day{i}/day{i}.py","w")
        if not os.path.isfile(f"day{i}/input.txt"):
            open(f"day{i}/input.txt","w")
    except FileExistsError:
        print(f"day{i} already exists")
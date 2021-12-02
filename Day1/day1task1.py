eka = True
edellinen = 0
verrattava = 0
kertoma = 0

with open("input.txt") as file:
    for item in file:
        if eka == True:
            eka = False
            edellinen = int(item)
        else:
            if int(item) > edellinen:
                kertoma += 1
                print("kasvoi")
                edellinen = int(item)
            if int(item) < edellinen:
                print("laski")
                edellinen = int(item)
print(kertoma)
taulukko = []
i = 0
summa1 = 0
summa2 = 0
kertoma = 0

with open("input.txt") as file:
    for item in file:
        taulukko.append(int(item))
while i < len(taulukko) - 3:
    summa1 = taulukko[i] + taulukko[i+1] + taulukko[i+2]
    summa2 = taulukko[i+1] + taulukko[i+2] + taulukko[i+3]

    if summa1 < summa2:
        kertoma += 1
    i += 1

print(kertoma)
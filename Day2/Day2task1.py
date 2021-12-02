eteenpain = 0
alaspain = 0

data = []
with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip('\n')
        suunta, arvo = line.split(" ", 1)
        data.append([suunta, arvo])

for i in data:
    if i[0] == "forward":
        print("eteen")
        eteenpain += int(i[1])
        
    elif i[0] == "up":
        print("ylös")
        alaspain -= int(i[1])
        
    elif i[0] == "down":
        print("alas")
        alaspain += int(i[1])
        
print("syvyys: ", alaspain)
print("eteen: ", eteenpain)

tulos = alaspain * eteenpain
print("tulos: ", tulos)
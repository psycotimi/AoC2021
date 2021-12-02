eteenpain = 0
alaspain = 0
aim = 0

data = []
with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip('\n')
        suunta, arvo = line.split(" ", 1)
        data.append([suunta, arvo])

for i in data:
    if i[0] == "forward":
        eteenpain += int(i[1])
        alaspain += int(i[1]) * aim
        
    elif i[0] == "up":
        aim -= int(i[1])
        
    elif i[0] == "down":
        aim += int(i[1])
        
print("syvyys: ", alaspain)
print("eteen: ", eteenpain)

tulos = alaspain * eteenpain
print("tulos: ", tulos)
print("aim: ", aim)
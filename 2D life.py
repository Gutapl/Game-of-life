import random
import time
c = ''
lenworld = 5 #int(input("Введите длину мира"))
widthworld = 10 #int(input("Введите ширину мира"))
realworld = []
p = []
s = 0 #тут считает количество списков которые состоят из 0
for i in range(lenworld):
    for j in range(widthworld):
        p.append(random.randint(0, 1))
    realworld.append(p)
    p = []
def vivodpole(rw):
    for i in rw:
            for j in i:
                print(j, end='  ')
            print()
vivodpole(realworld)
pokoleniya = int(input("Введите количество поколений"))
print(c.replace("0", " "))
futurepole = realworld.copy()
for z in range(pokoleniya):
    time.sleep(0.5)
    s = 0
    futurepole = [[0] * widthworld for _ in range(lenworld)]
    lin = -1
    for i in range(0, lenworld):
        for j in range(0, widthworld):
            lin += 1
            count = 0
            count += int(realworld[(i + 1) % lenworld][j])
            count += int(realworld[i - 1][j])
            count += int(realworld[i][(j + 1) % widthworld])
            count += int(realworld[i][j - 1])
            count += int(realworld[(i + 1) % lenworld][(j + 1) % widthworld])
            count += int(realworld[i - 1][(j + 1) % widthworld])
            count += int(realworld[(i + 1) % lenworld][j - 1]) 
            count += int(realworld[i - 1][j - 1])
            #print("lin:", lin, "count;", count, "j:", j, "i:", i,"realworld:", realworld[i][j])
            if (int(realworld[i][j]) == 0) and (count == 3):
                futurepole[i][j] = 1
            elif (int(realworld[i][j]) == 1) and ((count == 2) or (count == 3)):
                futurepole[i][j] = 1
            else:
                futurepole[i][j] = 0
    if futurepole == realworld:
        break
    elif realworld == [[0] * widthworld for _ in range(lenworld)]:
        break
    else:
        to = 0
    realworld = futurepole.copy()
    vivodpole(realworld)
    realworld = futurepole.copy()
    print()

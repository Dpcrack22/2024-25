import time
dimension = 4
carita = ["☻", 2,0,1,1]
while True:
    for i in range(dimension):
        for j in range(dimension):
            if i ==carita[1] and j == carita[2]:
                print("☻".center(6),end="")
            else:
                print(".".center(7),end="")

        print()
    if carita[2] +  carita[4] > dimension-1:
        carita[4] = -1
    elif carita[2] + carita[4] < 0:
        carita[4] = 1
    carita[2] = carita[2] + carita[4]



    time.sleep(1)
    print("\n"*10)
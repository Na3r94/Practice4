def Shatranj(x , y):
    for j in range(0 , y):
        if j % 2 == 0:
            for i in range(0 , x):
                if i % 2 == 0:
                    print("#" , end=' ')
                elif i % 2 == 1:
                    print("*" , end =' ')
            print()
        if j % 2 == 1:
            for i in range(0 , x):
                if i % 2 == 1:
                    print("#" , end=' ')
                elif i % 2 == 0:
                    print("*" , end =' ')
            print()



x = int(input("Tedade Soton : "))
y = int(input("Tedad satr : "))

Shatranj(x , y)

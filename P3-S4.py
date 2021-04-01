def Jadval (a , b):
    for i in range (1 , a +1):
        for j in range (1 , b+1):
            print(i * j , end=' ')
        print()

a = int(input("Tedade Soton : "))
b = int(input("Tedade satr : "))

Jadval (a , b)
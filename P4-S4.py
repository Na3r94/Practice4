import math

def Moadele(a , b , c, d):
    s = 18*a*b*c*d - 4 * b**3 * d + b**2 * c**2 - 4 * a * c**3 - 27 * a**2 * d**2
    return s

a = float(input())
b = float(input())
c = float(input())
d = float(input())

i = (-1) ** (1/2)
u1 = 1
u2 = (-1 + i * math.sqrt(3)) / 2
u3 = (-1 - i * math.sqrt(3)) / 2   
    
s0 = b ** 2 - 3 * a * c
s1 = 2 * b**3 - 9 * a*b*c + 27 * a**2 *d
w = ((math.sqrt(-27 * a ** 2 * Moadele(a,b,c,d)) + s1) / 2 ) ** (1/3)

x1= (-1/(3*a))*(b+u1*w+ s0/(u1*w))   
x2= (-1/(3*a))*(b+u2*w+ s0/(u2*w))
x3= (-1/(3*a))*(b+u3*w+ s0/(u3*w))

print("x1 = ",x1)
print("x2 = ",x2)
print("x3 = ",x3)
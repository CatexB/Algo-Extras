import math
def Karatsuba(first, second, z1, z2):
    n = len(str(first))
    print(n)
    print("Current Problem: " + (first) + "*" + (second))
    if(n <= 2):
        first = int(first)
        second = int(second)
        print("HIT BASE")
        return first * second

        n2 = int(n/2)

        a = (first[0:n2])
        b = (first[n2:])
        c = (second[0:n2])
        d = (second[n2:])
        print(a,b,c,d)



        x = 0
        y = 0
        z = 0

        x = x + (Karatsuba(a,c))
        y = (y + Karatsuba(b,d))
        z = z + (Karatsuba (a+b, c+d)) - x - y
        print("Current x: ",x)
        print("Current y: ",y)
        print("Current z: ", z)

        p1 = math.pow(10,int(n)) * x
        p2 = math.pow(10, int(n/2)) * z
        return(p1 + p2 + y)



print(Karatsuba("20194102", "47295610"))

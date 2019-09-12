import math
def Karatsuba(first, second):
    n = len(str(first))
    print("Current Problem: " + str(first) + "*" + str(second))
    if(n <= 2):
        print(first, "*", second, "=", first*second)
        print("HIT BASE")
        return first * second
    else:
        first = str(first)
        second = str(second)

        n2 = int(n/2)

        a = int((first[0:n2]))
        b = int((first[n2:]))
        c = int((second[0:n2]))
        d = int((second[n2:]))
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
        print("p1 = 10^"+str(n)+"*"+str(x))
        p2 = math.pow(10, int(n/2)) * z
        print("p2 = 10^"+str(int(n/2))+"*"+str(z))
        return(p1 + p2 + y)



print(Karatsuba("20194102", "47295610")) #Put your question here

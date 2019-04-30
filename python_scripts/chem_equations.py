import math

def quadratic(a,b,c):

    return ((-b - math.sqrt(b**2 - 4*a*c))/(2*a),(-b + math.sqrt(b**2 - 4*a*c))/(2*a))

def debye_huckel(z,m,a):
    return -0.51*z**2*math.sqrt(m)/(1+a*math.sqrt(m)/305)

def weak_acid(f,ka):
    return quadratic(1,ka,-f*ka)

def sci_not(num):
    e = 0
    if num == 0: 
        print("0")
        return 0
    e = math.floor(math.log10(num))
    num = num * 10**(-e)
 #  print("{}E{}".format(num,e))
 #   return (num,e)
    return "{}E{}".format(num,e)

if __name__ == "__main__":
    print(quadratic(1,0,-4))
    print(weak_acid(.1,3.77*(10**-5)))
    # ka = 5.69*(10**-10)
    # for e in range (-1,-7,-1):
    #     ans = weak_acid(10**e,ka)
    #     print(e,ans[1],-1*math.log(ans[1],10))

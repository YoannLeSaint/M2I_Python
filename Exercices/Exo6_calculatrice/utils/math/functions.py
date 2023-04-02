def test():
    print("test")


def add(a,b):
    return a+b

def add2(*param):
    s=0
    for p in param:
        s+= p
    return s

#print(add2(1,2,3,4))

def sous(a,b):
    return som(a,-b)

def sous2(*param):
    return add2(param)

def div(a,b):
    if b!=0:
        return a/b
    else:
        return "error"

def div2(*param):
    if len(param) == 1:
        return param
    div = param[0]
    print(div)
    for i in range(len(param)-1):
        div /= param[i+1]
    return div

# print(div2(2))
# print(div2(1,2))
# print(div2(1,2,3))


def fac(n):
    if n <= 1:
        return 1
    else:
        return n * fac(n - 1)

def fac2(*param):
    n = param[0]
    if n <= 1:
        return 1
    else:
        return n * fac2(n - 1)

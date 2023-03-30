def test():
    print("test")


def add(a,b):
    return a+b

def sous(a,b):
    return som(a,-b)

def div(a,b):
    if b!=0:
        return a/b
    else:
        return "error"

def fac(n):
    if n <= 1:
        return 1
    else:
        return n * fac(n - 1)


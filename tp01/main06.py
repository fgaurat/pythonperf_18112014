
def add(*l):
    print(l)
    r = 0
    for i in l:
        r+=i
    return r

def add1(*l):
    return sum(l)

# def hello(name:str,first_name:str)->None:
def hello(**kwargs)->None:
    """
    Ceci est une docstring
    """
    print("bonjour",kwargs)

def hello2(name,firstname,/): # positional only
    print(name,firstname)

def hello3(*,name,firstname): # kw only
    print(name,firstname)


def main():
    #region test args
    l = [10,20,30,40,50]
    l1 = 10,20,30,40,50
    r = add1(*l1)
    print(r) # 150

    r = add(10,20,30,40,50)
    print(r) # 150

    a,b,*c= 0,1,2,3,453,765,645
    print(a)
    print(b)
    print(c)
    print(*c,sep="--")
    # print(2,3,453,765,645)
    print("valeur de a",a)
    #endregion

    hello(first_name="Frédéric",name="GAURAT",job="dev",age="48")
    hello3(firstname="Frédéric",name="GAURAT")
if __name__=='__main__':
    main()

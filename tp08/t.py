
def f(*p):
    print(p) 


def f1(p1,p2):
    pass

def main():
    f("toto",'tutu')

    t = 'toto','tutu'

    f1(t[0],t[1])
    f1(*t)

if __name__=='__main__':
    main()

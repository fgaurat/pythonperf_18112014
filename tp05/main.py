from Carre import Carre
from Cercle import Cercle


def main():
    c = Carre(3)
    print(c.cote)
    print(c.surface)
    print(c)
    ce = Cercle(3)
    print(ce.surface)

if __name__=='__main__':
    main()

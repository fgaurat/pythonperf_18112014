from Rectangle import Rectangle
from DataRectangle import DataRectangle


def main():
    r = Rectangle(2,3)
    # print(r._Rectangle__longueur)
    # print(r.__longueur)
    # print(r.__largeur)
    # r.__longueur = -435
    # print(r.__longueur)
    
    # print('longueur',r.get_longueur())
    # print('largeur',r.get_largeur())
    # r.set_longueur(12)
    # print('longueur',r.get_longueur())
    # print('surface',r.get_surface())

    r.longueur = 12
    print(r.longueur)
    print(r.surface)
    print(50*'-')
    d = DataRectangle(4,5)
    print(d.largeur)
    print(d.longueur)
    print(d.surface)
    print(50*'-')
    r = Rectangle(2,3)    
    r1 = Rectangle(2,3)    

    # if r.__eq__(r1):
    if r==r1:
        print("ok")
    else:
        print("ko")
    d = DataRectangle(4,5)
    d1 = DataRectangle(4,5)
    if d==d1:
        print("ok")
    else:
        print("ko")

    print(50*'-')
    r = Rectangle(2,3)    
    print(r)

if __name__=='__main__':
    main()



class Rectangle:
    
    def __init__(self,longueur,largeur):
        self.__longueur =longueur
        self.__largeur =largeur
    
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self,longueur):
        assert longueur > 0 
        self.__longueur = longueur

    def set_largeur(self,largeur):
        assert largeur > 0 
        self.__largeur = largeur

    def get_surface(self):
        return self.__largeur*self.__longueur
    
    longueur = property(get_longueur,set_longueur,doc="Longueur property")
    largeur = property(get_largeur,set_largeur,doc="Largeur property")
    surface = property(get_surface,doc="Surface property")
    
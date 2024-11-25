

class Rectangle:
    
    def __init__(self,longueur,largeur):
        self.__longueur =longueur
        self.__largeur =largeur
    
    @property
    def longueur(self):
        return self.__longueur
    
    @property
    def largeur(self):
        return self.__largeur
    
    @longueur.setter
    def longueur(self,longueur):
        assert longueur > 0 
        self.__longueur = longueur
    
    @largeur.setter
    def largeur(self,largeur):
        assert largeur > 0 
        self.__largeur = largeur

    @property
    def surface(self):
        return self.__largeur*self.__longueur
    

    def __eq__(self, value):
        return self.longueur == value.longueur and self.largeur == value.largeur
    
    def __str__(self):
        return f"{__class__.__name__}: {self.longueur}, {self.largeur}"
    
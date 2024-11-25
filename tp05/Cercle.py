from ICalcGeo import ICalcGeo 
import math

class Cercle(ICalcGeo):

    def __init__(self,rayon):

        self.__rayon = rayon
    
    @property
    def rayon(self):
        return self.__rayon
    
    @rayon.setter
    def rayon(self,rayon):
        assert rayon >0
        self.__rayon = rayon
    
    # @property
    # def surface(self):
    #     return math.pi*self.__rayon**2

    def __str__(self):
        return f"{__class__.__name__}: {self.rayon}"

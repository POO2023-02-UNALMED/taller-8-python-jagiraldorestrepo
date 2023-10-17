class Deportista():
    def __init__(self,añosPracticando):
        self.__deporte="Futbol"
        self.__añosPracticando=añosPracticando

    def getDeporte(self):
        return self.__deporte

    def setDeporte(self,deporte):
        self.__deporte=deporte

    def getAñosPracticando(self):
        return self.__añosPracticando

    def setAñosPracticando(self,añosPracticando):
        self.__añosPracticados=añosPracticando
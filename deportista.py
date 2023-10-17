class Deportista():
    def __init__(self, deporte="Futbol", añosPracticando=0):
        self.__deporte = deporte
        self.__añosPracticando = añosPracticando

    def getDeporte(self):
        return self.__deporte

    def setDeporte(self,deporte):
        self.__deporte=deporte

    def getAñosPracticando(self):
        return self.__añosPracticando

    def setAñosPracticando(self,añosPracticando):
        self.__añosPracticados=añosPracticando
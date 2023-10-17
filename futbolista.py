from deportista import Deportista
from persona import Persona

class Futbolista(Persona,Deportista):
    __listaFutbolistas=[]
    def __init__(self,nombre,edad,altura,sexo,añosPracticando,golesMarcados,tarjetasRojas,piernaHabil):
        super().__init__(nombre,edad,altura,sexo,añosPracticando)
        self.__golesMarcados=golesMarcados
        self.__tarjetasRojas=tarjetasRojas
        self.__piernaHabil=piernaHabil
        self.__listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self.__golesMarcados

    def setGolesMarcados(self,golesMarcados):
        self.__golesMarcados=golesMarcados

    def getTarjetasRojas(self):
        return self.__tarjetasRojas

    def setTarjetasRojas(self,tarjetasRojas):
         self.__tarjetasRojas=tarjetasRojas
        
    def getPiernaHabil(self):
        return self.__piernaHabil

    def setPiernaHabil(self,piernaHabil):
        self.__piernaHabil=piernaHabil

    def __str__(self):
        return "Mi nombre es "+self.getNombre()+" soy profesional en el deporte "+self.getDeporte()+" Tengo "+str(self.getEdad()) +" años de edad y llevo "+str(self.getAñosPracticando())+" años en el deporte"

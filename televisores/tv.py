from televisores.marca import Marca

class TV:
    _numTV = 0

    def __init__(self, marca: Marca, estado: bool):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500

        TV._numTV += 1
    
    @classmethod
    def getNumTV(cls) -> int:
        return cls._numTV
    
    @classmethod
    def setNumTV(cls, numTV: int):
        cls._numTV = numTV

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def volumenDown(self):
        self.setVolumen(self._volumen - 1)
    
    def canalUp(self):
        self.setCanal(self._canal + 1)

    def canalDown(self):
        self.setCanal(self._canal - 1)

    def volumenUp(self):
        self.setVolumen(self._volumen + 1)

    def getMarca(self):
        return self._marca
    
    def getCanal(self):
        return self._canal
    
    def getPrecio(self):
        return self._precio
    
    def getVolumen(self):
        return self._volumen

    def getControl(self):
        return self._control
    
    def getEstado(self):
        return self._estado
    
    def setMarca(self, marca: Marca):
        self._marca = marca
    
    def setCanal(self, canal: int):
        if self._estado == True:
            if 1 <= canal <= 120:
                self._canal = canal

    def setPrecio(self, precio: int):
        self._precio = precio

    def setVolumen(self, volumen: int):
        if self._estado == True:
            if 0 <= volumen <= 7:
                self._volumen = volumen

    def setControl(self, control: Control):
        self._control = control
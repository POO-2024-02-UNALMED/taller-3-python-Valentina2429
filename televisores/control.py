class Control:
    def __init__(self): 
        self._tv = None    

    def enlazar(self, tv):
        self._tv = tv
        tv.setControl(self)

    def turnOn(self):
        self._tv.turnOn()

    def canalDown(self):
        self._tv.canalDown()

    def volumenUp(self):
        self._tv.volumenUp()
    
    def volumenDown(self):
        self._tv.volumenDown()

    def turnOff(self):
        self._tv.turnOff()

    def canalUp(self):
        self._tv.canalUp()

    def setCanal(self, canal: int):
        self._tv.setCanal(canal)

    def setVolumen(self, volumen: int):
        self._tv.setVolumen(volumen)

    def getTv(self) -> TV:
        return self._tv
    
    def setTv(self, tv: TV):
        self._tv = tv
    
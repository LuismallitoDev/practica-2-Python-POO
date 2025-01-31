class Contabilidad():
    _costoCompensacion = 10
    def __init__(self,ingresos=0.0,costosOperativos=0.0,ventas=[],transacionesReembolsadas=[]):
        self._ingresos = ingresos
        self._costosOperativos = costosOperativos
        self._ventas = ventas
        self._transacionesReembolsadas = transacionesReembolsadas
    
    #Definiendo Getters y Setters    
    def getIngresos(self)->float:
        return self._ingresos
    def getCostosOperativos(self)->float:
        return self._costosOperativos
    def getVentas(self)->list:
        return self._ventas
    def getTransaccionesReembolsadas(self)->list:
        return self._transacionesReembolsadas
    def setIngresos(self,ingresos):
        self._ingresos = ingresos
    def setCostosOperativos(self, costosOperativos):
        self._costosOperativos = costosOperativos
    def setVentas(self, ventas):
        self._ventas = ventas
    def setTransaccionesReembolsadas(self, transaccionesReembolsadas):
        self._transaccionesReembolsadas = transaccionesReembolsadas
        
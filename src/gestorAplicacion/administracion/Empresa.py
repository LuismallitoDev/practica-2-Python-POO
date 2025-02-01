class Empresa:
    def __init__(
        self,
        nombre: str = "",
        empleados: list = [],
        buses: list = [],
        rutas: list = [],
        dineroEmpresa: float = 0.0,
    ):
        self._nombre = nombre
        self._empleados = empleados
        self._buses = buses
        self._rutas = rutas
        self._dineroEmpresa = dineroEmpresa

    # Definiendo Getters y Setters
    def getNombre(self) -> str:
        return self._nombre

    def setNombre(self, nombre: str):
        self._nombre = nombre

    def getEmpleados(self) -> list:
        return self._empleados

    def setEmpleados(self, empleados: list):
        self._empleados = empleados

    def getBuses(self) -> list:
        return self._buses

    def setBuses(self, buses: list):
        self._buses = buses

    def getRutas(self) -> list:
        return self._rutas

    def setRutas(self, rutas: list):
        self._rutas = rutas

    def getDineroEmpresa(self) -> float:
        return self._dineroEmpresa

    def setDineroEmpresa(self, dineroEmpresa: float):
        self._dineroEmpresa = dineroEmpresa

    # Metodos de Instacia
    def agregarEmpleado(self, empleado: object):
        pass

    def contratarEmpleado(self):
        pass

    def despedirEmpleado(self, empleado: object):
        pass

    def comprarBus(self, valor: int):
        pass

    def desvincularBus(self, bus: object):
        pass

    def asignarRutas(self, rutas: object):
        pass

    def reportarFinanzas(self):
        pass

    def reasignarPasajero(self):
        pass

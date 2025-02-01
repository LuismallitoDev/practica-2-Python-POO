class Bus:
    # Esto nos dira la cantidad maxima de equipaje que soporta cada bus ¡¡Peso en Kg!!
    PesoMaximo = {"LIGERO": 500, "MEDIO": 750, "PESADO": 1000, "EXTRA_PESADO": 1250}
    _buses = []

    # Este es el constructor de la clase, donde inicializamos los atributos
    def __init__(
        self,
        placa: str = "",
        cantidadAsientos: int = 20,
        asientos: list = [],
        kilometrosRecorridos: float = 0.0,
        rutasFuturas: list = [],
        empresa: object = None,
        equipaje: list = [],
        consumo: float = 0.0,
        pesoMaximo: float = 0.0,
    ):
        self.placa = placa
        self._cantidadAsientos = cantidadAsientos
        self._asientos = asientos
        self._kilometrosRecorridos = kilometrosRecorridos
        self._rutasFuturas = rutasFuturas
        self.empresa = empresa
        self._equipaje = equipaje
        self._consumo = consumo
        self._pesoMaximo = pesoMaximo

        # Agregamos el bus a la lista de buses
        if self.empresa is not None:
            self.empresa.agregarBus(self)

    def getCantidadAsientos(self):
        return self._cantidadAsientos

    def getAsientos(self):
        return self._asientos

    def setAsientos(self, value: list):
        self._asientos = value

    def getKilometrosRecorridos(self):
        return self._kilometrosRecorridos

    def setKilometrosRecorridos(self, value: float):
        self._kilometrosRecorridos = value

    def getRutasFuturas(self):
        return self._rutasFuturas

    def setRutasFuturas(self, value: list):
        self._rutasFuturas = value

    def getEquipaje(self):
        return self._equipaje

    def setEquipaje(self, value: list):
        self._equipaje = value

    def getConsumo(self):
        return self._consumo

    def setConsumo(self, value: float):
        self._consumo = value

    def getPesoMaximo(self):
        return self._pesoMaximo

    def setPesoMaximo(self, value: float):
        self._pesoMaximo = value

    # Métodos de Clase
    @classmethod
    def anadirBus(cls):
        pass

    def cantidadBuses(cls) -> int:
        return len(cls._buses)

    def getBuses(cls):
        return cls._buses

    # Métodos de Instancia
    def isDisponbile(self):
        pass

    def anadirRutaFutura(self) -> bool:
        pass

    def quitarRutaFutura(self) -> bool:
        pass

    def asignarPasajero(self) -> str:
        pass

    def eliminarPasajero(self) -> str:
        pass

    def reparar(self):
        pass

    def verificarIntegridad(self):
        pass

    def calcularConsumoCombustible(self):
        pass

    def danoAleatorio(self) -> float:
        pass

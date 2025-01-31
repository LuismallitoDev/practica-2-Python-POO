class Asiento:
    _asientos = []

    def __init__(
        self,
        bus: object = None,
        estado: bool = True,
        usuario: object = None,
        integridad: str = "",
    ):
        self._idAsiento = Asiento.cantidadAsientos + 1
        self._bus = bus
        self._estado = estado
        self._usuario = usuario
        self._integridad = integridad

    # Difiniendo Getters y Setters
    def getIdAsiento(self) -> int:
        return self._idAsiento

    def getBus(self) -> object:
        return self._bus

    def getEstado(self) -> bool:
        return self._estado

    def getUsuario(self) -> object:
        return self._usuario

    def getIntegridad(self) -> str:
        return self._integridad

    def setIdAsiento(self, idAsiento: int):
        self._idAsiento = idAsiento

    def setBus(self, bus: object):
        self._bus = bus

    def setEstado(self, estado: bool):
        self._estado = estado

    def setUsuario(self, usuario: object):
        self._usuario = usuario

    def setIntegridad(self, integridad: str):
        self._integridad = integridad

    @classmethod
    def cantidadAsientos(cls) -> int:
        return len(cls._asientos)

    def getAsientos(cls) -> list:
        return cls._asientos

    @classmethod
    def agregarAsiento(cls, asiento: "Asiento"):
        cls._asientos.append(asiento)

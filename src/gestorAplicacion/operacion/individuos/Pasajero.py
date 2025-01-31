import Persona


class Pasajero(Persona):
    _pasajeroRegistrados = []

    def __init__(
        self,
        nombre: str = "",
        edad: int = 0,
        id: int = 0,
        maletas: list = [],
        wallet: float = 0.0,
        facturas: list = [],
        numReembolsoDisp: int = 0,
        acompanante: object = None,
    ):
        super.__init__(nombre, edad, id)
        self._maletas = maletas
        self._wallet = wallet
        self._facturas = facturas
        self._numReembolsoDisp = numReembolsoDisp
        if acompanante != None:
            self._acompanante = acompanante
            Pasajero._pasajeroRegistrados.append(self)

    # Defiendo Getters y Setters ¡¡Los getters y Setters de nombre, edad y id ya se heredaron por Persona!!
    def getMaletas(self) -> list:
        return self._maletas

    def getWallet(self) -> float:
        return self._wallet

    def getFacturas(self) -> list:
        return self._facturas

    def getNumReembolsoDisp(self) -> int:
        return self._numReembolsoDisp

    def getAcompanante(self) -> object:
        return self._acompanante

    def setMaletas(self, maletas: list):
        self._maletas = maletas

    def setWallet(self, wallet: float):
        self._wallet = wallet

    def setFacturas(self, facturas: list):
        self._facturas = facturas

    def setNumReembolsoDisp(self, numReembolsoDisp: int):
        self._numReembolsoDisp = numReembolsoDisp

    def setAcompanante(self, acompanante: object):
        self._acompanante = acompanante
        Pasajero._pasajeroRegistrados.append(self)

    @staticmethod
    def getPasajerosRegistrados():
        return Pasajero._pasajeroRegistrados

    @staticmethod
    def getCantidadPasajeros():
        return len(Pasajero._pasajeroRegistrados)

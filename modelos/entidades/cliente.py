from modelos.entidades.bebidaConAlcohol import BebidaConAlcohol
from modelos.entidades.bebidaSinAlcohol import BebidaSinAlcohol
from modelos.entidades.bebida import Bebida
class Cliente:
    @classmethod
    def fromDiccionario(cls, diccionario: dict)->"Cliente":
        # Determinar el tipo de bebida basado en los datos del diccionario
        bebida_dict = diccionario["bebidaPreferida"]
        if "graduacionAlcoholica" in bebida_dict:
            bebida_preferida = BebidaConAlcohol.fromDiccionario(bebida_dict)
        elif "sabor" in bebida_dict:
            bebida_preferida = BebidaSinAlcohol.fromDiccionario(bebida_dict)
        else:
            raise ValueError("Tipo de bebida no reconocido")
        
        return cls(diccionario["dni"], diccionario["nombre"], diccionario["apellido"], bebida_preferida)
    def __init__(self, dni: int, nombre: str, apellido: str, bebidaPreferida: Bebida):
        if not isinstance(dni, int) or dni <= 0:
            raise ValueError("El DNI debe ser un número entero positivo")
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        if not isinstance(apellido, str) or apellido.strip() == "":
            raise ValueError("El apellido no puede estar vacío")
        if not isinstance(bebidaPreferida, Bebida):
            raise ValueError("La bebida preferida no puede estar vacía")
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__bebidaPreferida = bebidaPreferida

    def obtenerDni(self)->int:
        return self.__dni

    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerApellido(self)->str:
        return self.__apellido
    
    def obtenerBebidaPreferida(self)->Bebida:
        return self.__bebidaPreferida
    
    def existeCliente(self)->bool:
        pass
    
    def __str__(self):
        return f"DNI: {self.__dni}, Nombre: {self.__nombre} {self.__apellido}, Bebida preferida: {self.__bebidaPreferida}"
    
    def toDiccionario(self)->dict:
        return {
            "dni": self.__dni,
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "bebidaPreferida": self.__bebidaPreferida.toDiccionario()
        }
    
    def modificarDatosCliente(self, nombre: str, apellido: str, bebidaPreferida: Bebida):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        if not isinstance(apellido, str) or apellido.strip() == "":
            raise ValueError("El apellido no puede estar vacío")
        if not isinstance(bebidaPreferida, Bebida):
            raise ValueError("La bebida preferida no puede estar vacía")
        self.__nombre = nombre
        self.__apellido = apellido
        self.__bebidaPreferida = bebidaPreferida
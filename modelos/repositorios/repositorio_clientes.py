from modelos.entidades.cliente import Cliente
from modelos.entidades.bebida import Bebida
import json
from typing import List

class RepositorioClientes:
    ruta_archivo = "datos/clientes.json"

    def __init__(self):
        self.__clientes = []
        self.__cargarClientes()
    
    def __cargarClientes(self):
        try:
            with open(RepositorioClientes.ruta_archivo, "r") as archivo:
                lista_dicc_clientes = json.load(archivo)
                for cliente in lista_dicc_clientes:
                    self.__clientes.append(Cliente.fromDiccionario(cliente))
        except FileNotFoundError:
            print("No se encontro el archivo de Clientes")
        except Exception as e:
            print("Error cargando los clientes del archivo.\n" + str(e))

    def __guardarClientes(self):
        try:
            with open(RepositorioClientes.ruta_archivo, "w") as archivo:
                lista_dicc_clientes = [cliente.toDiccionario() for cliente in self.__clientes]
                json.dump(lista_dicc_clientes, archivo, indent=4)
        except Exception as e:
            print("Error guardando los clientes en el archivo.\n" + str(e))

    def obtenerTodosLosClientes(self)->List[Cliente]:
        """Retorna una lista con todos los clientes"""
        return self.__clientes
    
    def obtenerClientePorDni(self, dni: int)->Cliente:
        """Retorna el cliente con el DNI indicado, None si no existe"""
        for cliente in self.__clientes:
            if cliente.obtenerDni() == dni:
                return cliente
        return None
    
    def existeClientePorDni(self, dni: int)->bool:
        """Retorna True si existe un cliente con el DNI indicado, False en caso contrario"""
        return self.obtenerClientePorDni(dni) is not None
    
    def agregarCliente(self, cliente: Cliente):
        """Agrega un cliente al repositorio. Lanza ValueError si ya existe un cliente con el mismo DNI"""
        if self.existeClientePorDni(cliente.obtenerDni()):
            raise ValueError("Ya existe un cliente con el mismo DNI")
        self.__clientes.append(cliente)
        self.__guardarClientes()
    
    def actualizarCliente(self, dni: int, nombre: str, apellido: str, bebidaPreferida: Bebida):
        """Actualiza los datos del cliente en base a su DNI. Retorna True si el cliente fue actualizado, False en caso contrario"""
        cliente = self.obtenerClientePorDni(dni)
        if cliente:
            cliente.modificarDatosCliente(nombre, apellido, bebidaPreferida)
            self.__guardarClientes()
            return True
        return False
    
    def eliminarClientePorDni(self, dni: int):
        """Elimina el cliente con el DNI indicado. Retorna True si el cliente fue eliminado, False en caso contrario"""
        for cliente in self.__clientes:
            if cliente.obtenerDni() == dni:
                self.__clientes.remove(cliente)
                self.__guardarClientes()
                return True
        return False
    

    


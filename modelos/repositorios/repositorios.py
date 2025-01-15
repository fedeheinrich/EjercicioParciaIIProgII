from modelos.repositorios.repositorio_bebidas import RepositorioBebidas
from modelos.repositorios.repositorio_clientes import RepositorioClientes

bebidas = None
clientes = None

def obtenerRepoBebidas():
    global bebidas
    if bebidas == None:
        bebidas = RepositorioBebidas()
    return bebidas

def obtenerRepoClientes():
    global clientes
    if clientes == None:
        clientes = RepositorioClientes()
    return clientes
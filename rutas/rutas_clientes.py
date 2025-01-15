from flask import Blueprint, jsonify, request
from modelos.entidades.cliente import Cliente
from modelos.repositorios.repositorios import obtenerRepoClientes, obtenerRepoBebidas


repo_clientes = obtenerRepoClientes()
repo_bebidas = obtenerRepoBebidas()

bp_clientes = Blueprint("bp_clientes", __name__)

@bp_clientes.route("/clientes", methods=["GET"])
def listar_clientes():
    return jsonify([cliente.toDiccionario() for cliente in repo_clientes.obtenerTodosLosClientes()])

@bp_clientes.route("/clientes/<int:dni>", methods=["GET"])
def obtener_cliente(dni):
    cliente = repo_clientes.obtenerClientePorDni(dni)
    if cliente == None:
        return jsonify({"error": "Cliente no encontrado"}), 404
    else:
        return jsonify(cliente.toDiccionario())

@bp_clientes.route("/clientes", methods=["POST"])
def agregar_cliente():
    try:
        datos = request.json
        if not datos:
            return jsonify({"error": "No se recibieron datos"}), 400

        # Verificar que estén todos los campos necesarios
        campos_requeridos = ["dni", "nombre", "apellido", "bebidaPreferida"]
        for campo in campos_requeridos:
            if campo not in datos:
                return jsonify({"error": f"Falta el campo {campo}"}), 400

        # Verificar que la bebida preferida existe
        nombre_bebida = datos["bebidaPreferida"].get("nombre")
        if not nombre_bebida:
            return jsonify({"error": "La bebida preferida debe tener un nombre"}), 400
        
        bebida = repo_bebidas.obtenerBebidaPorNombre(nombre_bebida)
        if not bebida:
            return jsonify({"error": "La bebida preferida no existe"}), 404

        # Crear el cliente
        cliente = Cliente(
            dni=datos["dni"],
            nombre=datos["nombre"],
            apellido=datos["apellido"],
            bebidaPreferida=bebida
        )
        
        repo_clientes.agregarCliente(cliente)
        return jsonify({
            "mensaje": "Cliente agregado correctamente",
            "cliente": cliente.toDiccionario()
        }), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Error interno del servidor"}), 500
    
@bp_clientes.route("/clientes/<int:dni>", methods = ["PUT"])
def modificar_cliente(dni):
    try:
        datos = request.json
        if not datos:
            return jsonify({"error": "No se recibieron datos"}), 400

        # Verificar que el cliente existe
        cliente = repo_clientes.obtenerClientePorDni(dni)
        if not cliente:
            return jsonify({"error": "Cliente no encontrado"}), 404

        # Verificar que estén los campos necesarios
        campos_requeridos = ["nombre", "apellido", "bebidaPreferida"]
        for campo in campos_requeridos:
            if campo not in datos:
                return jsonify({"error": f"Falta el campo {campo}"}), 400

        # Verificar que la bebida preferida existe
        nombre_bebida = datos["bebidaPreferida"].get("nombre")
        if not nombre_bebida:
            return jsonify({"error": "La bebida preferida debe tener un nombre"}), 400
        
        bebida = repo_bebidas.obtenerBebidaPorNombre(nombre_bebida)
        if not bebida:
            return jsonify({"error": "La bebida preferida no existe"}), 404

        # Actualizar el cliente
        if repo_clientes.actualizarCliente(dni, datos["nombre"], datos["apellido"], bebida):
            return jsonify({
                "mensaje": "Cliente actualizado correctamente",
                "cliente": cliente.toDiccionario()
            })
        
        return jsonify({"error": "No se pudo actualizar el cliente"}), 500

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Error interno del servidor"}), 500
    
@bp_clientes.route("/clientes/<int:dni>", methods = ["DELETE"])
def eliminar_cliente(dni):
    if repo_clientes.eliminarClientePorDni(dni):
        return jsonify({"mensaje": "Cliente eliminado correctamente"}), 201
    return jsonify({"error": "No se encontró el cliente a eliminar."}), 404


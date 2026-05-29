import json

def cargar_clientes():
    try:
        with open("clientes.json", "r") as f:
            clientes = json.load(f)
            return clientes
        
    except (FileNotFoundError, json.JSONDecodeError):
        clientes = []
        return clientes
    
def guardar_clientes(clientes):
    with open("clientes.json", "w") as f:
        json.dump(clientes, f, indent=4)

def pedir_datos(clientes):
    id = max([c["id"] for c in clientes], default=0) +1

    nombre = input("Ingrese el nombre: ").strip().title()
    
    while True:
        try:
            edad = int(input("Ingresa la edad del cliente: "))
            break

        except ValueError:
            print("Error: Ingresa solo numeros")
    
    ciudad = input("Ingrese la ciudad: ").strip().title()

    nuevo_cliente = {
        "id" : id,
        "nombre" : nombre,
        "edad" : edad,
        "ciudad" : ciudad
    }

    return nuevo_cliente

def mostrar_clientes(clientes):
    if not clientes:
        print("No hay clientes registrados")
        return

    for c in clientes:
        print(f"{c['id']} - {c['nombre']} - {c['edad']} años - {c['ciudad']}")

def agregar_cliente(clientes, nuevo_cliente):
    if any(c.get("id") == nuevo_cliente["id"] for c in clientes):
        return clientes, "Id duplicado"
    
    clientes.append(nuevo_cliente)
    return clientes, "Cliente agregado con exito!"

def pedir_id():
    while True:
        try:
            id_pedido = int(input("Ingresa el id del cliente: "))
            break
        except ValueError:
            print("Error: Ingresa solo numeros")
    
    return id_pedido

def buscar_cliente(clientes, cliente_id):
    return next((c for c in clientes if c.get("id") == cliente_id), None)

def eliminar_cliente(clientes, cliente_id):

    for i, c in enumerate(clientes):
        if cliente_id == c['id']:
            del clientes[i]
            return "Cliente eliminado con exito!"
        
    return None

def modificar_cliente(clientes, cliente_id):
    
    if cliente_id not in [c['id'] for c in clientes]:
        return "Cliente inexistente"
    else:
        nombre_nuevo = input("Ingrese el nombre nuevo: ").strip().title()

    for c in clientes:
        if cliente_id == c['id']:
            c['nombre'] = nombre_nuevo
            return "Cambio de nombre exitoso! "
        
def filtrar_clientes(clientes):
    if len(clientes) == 0:
        return "No hay clientes que filtrar!"

    while True:
        try:
            edad_minima = int(input("Ingrese la edad minima: "))
            break
        except ValueError:
            print("Error: Ingrese solo numeros.")
    
    clientes_filtrados = [c['nombre'] for c in clientes if c['edad'] >= edad_minima]
    return clientes_filtrados

def mostrar_menu():
    print("1.Mostrar clientes")
    print("2.Agregar clientes")
    print("3.Buscar clientes")
    print("4.Eliminar cliente")
    print("5.Filtra clientes por edad")
    print("6.Modificar clientes")
    print("7.Salir")


def escoger_opcion():
    while True:
        try:
            opcion = int(input("Ingrese la opcion (1-7): "))
            if opcion > 0 and opcion < 8:
                return opcion
            print("Ingrese una opcion dentro del rango (1-7)")

        except ValueError:
            print("Error: Ingrese solo numeros")

def mensaje_despedida():
    print("Gracias por usar el menu de opciones")


def main():
    clientes = cargar_clientes()

    while True:
        mostrar_menu()

        opcion = escoger_opcion()

        if opcion == 1:
            mostrar_clientes(clientes)

        elif opcion == 2:
            nuevo_cliente = pedir_datos(clientes)
            clientes, mensaje = agregar_cliente(clientes, nuevo_cliente)
            guardar_clientes(clientes)
        
            print(mensaje)

        elif opcion == 3:
            cliente_id = pedir_id()
            cliente = buscar_cliente(clientes, cliente_id)
        
            if cliente:
                print(cliente)
            else:
                print("No se encontro el cliente")

        elif opcion == 4:
            cliente_id = pedir_id()
            resultado = eliminar_cliente(clientes, cliente_id)

            if resultado:
                print(resultado)
            else:
                print("Cliente inexistente!")

            guardar_clientes(clientes)

        elif opcion == 5:
            resultado = filtrar_clientes(clientes)
            print(f"Clientes que cumplen la edad minima: {resultado}")
        
        elif opcion == 6:

            cliente_id = pedir_id()

            resultado = modificar_cliente(clientes, cliente_id)
            print(resultado)

            guardar_clientes(clientes)
        
        elif opcion == 7:
            break

    mensaje_despedida()

main()







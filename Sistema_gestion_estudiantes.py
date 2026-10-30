estudiantes = []
contador = 0
banderaSalir = False

def mostrar(est):
    print(f"ID: {est['id']} Nombre: {est['nombre']} carrera:{est['carrera']}" )

def agregar ():
    global contador
    try:
        id_e = int(input("ID:"))
        for e in estudiantes:
            if e["id"] == id_e:
                print("ID ya existe")
                return
        nombre = input("Nombre:").strip()
        if not nombre:
            print("Nombre vacio")
            return
        carrera = input("carrera:").strip()
        estudiantes.append({"id": id_e, "nombre": nombre, "carrera": carrera})
        contador += 1
        print(f"Agregado. Total: {contador}")
    except ValueError:
        print("ID debe ser numero")

def listar ():
    if contador == 0:
        print("Sin estudiantes")
        return
    for i, e in enumerate(estudiantes, 1):
        print(f"{i}.", end="")
        mostrar(e)

def buscar ():
    if contador == 0:
        print ("Sin estudiantes")
        return
    try:
        id_b = int(input("ID a buscar: "))
        encontrado = False
        for e in estudiantes:
            if e["id"] == id_b:
                print("encontrado:")
                mostrar(e)
                encontrado =True
                break
        if not encontrado:
            print ("Estudiantes no encontrado")
    except ValueError:
        print("ID debe ser numero")

while not banderaSalir:
    print("\n--- SGE ----")
    print("1. Agregar\n2. Mostrar\n3. Buscar por ID\4. Salir")
    try:
        op = int(input("opcion:"))
    except ValueError:
        print("opcion invalida")
        continue
    match op:
        case 1:
            agregar()
        case 2:
            listar()
        case 3:
            buscar()
        case 4: 
            banderaSalir = True
            print("Saliendo...")
        case _:
            print("opcion 1-4")
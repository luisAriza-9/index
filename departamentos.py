import json
import os

def clear():
    os.system("clear")

def leerInt(msg):
    while True:
        try:
            iNum = int(input(msg))
            return iNum
        except ValueError:
            print("¡Error! Ingrese un numero entero valido")

def leerFloat(msg):
    while True:
        try:    
            while True:
                iNum = float(input(msg))
                return iNum
        except ValueError:
            print("¡Error! Ingrese un numero valido")

def leerString(msg):
    while True:
        try:
            sNom = input(msg)
            if sNom.strip() == "":
                print("\n¡Error! Entrada vacia")
                continue
            return sNom
        except Exception as e:
            print("\n¡Error! Entrada no valida")

def menu():
    while True:
        print("MENU PRINCIPAL GESTION DE DEPARTAMENTOS Y CIUDADES\n\n"
            "1.Listar todas las ciudades\n"
            "2.Añadir una ciudad\n"
            "3.Eliminar una ciudad\n"
            "4.Crear un departamento\n"
            "5.Eliminar un departamento\n"
            "6.Listar todos los departamentos\n"
            "7.Salir\n")
        op = leerInt("Ingrese el numero de la opcion que desea --> ")
        if op < 1 or op > 7:
            print("¡Error! Ingrese una opcion valida") 
            continue
        break
    return op

def cargarDat():
    with open("Campus-main/Repasos/PaísCiudad.json", "r") as archivo:
        datos = json.load(archivo)
    return datos

def listCiu(dat):
    print("LISTA DE TODAS LAS CIUDADES\n")
    for dep in dat["Departamentos"]:
        for ciu in dep["Ciudades"]:
            print(f"Id: {ciu['idCiudad']}")
            print(f"Nombre: {ciu['nomCiudad']}")
            print(f"Imagen: {ciu['imagen']}")
            print(f"Coordenadas: [{ciu['coordenadas']['lat']:,.0f}, {ciu['coordenadas']['lon']:,.0f}]\n")
    input("Ingrese cualquier letra o numero para continuar--> ")

def adcCiu(dat):
    print("AÑADIR UNA CIUDAD\n")
    while True:
        st = False
        id = leerInt("Ingrese el id del departamento: ")
        for dep in dat["Departamentos"]:
            if id == dep["idDep"]:
                st = True
                break
        if st == False:
            print("\n¡Error! El id ingresado no existe\n")
            continue
        else:
            break
    while True:
        st = False
        nueIdCiu = leerInt("\nIngrese el id de la nueva ciudad: ")
        for dep in dat["Departamentos"]:
            for ciu in dep["Ciudades"]:
                if nueIdCiu == ciu["idCiudad"]:
                    st = True
                    break
        if st == True:
            print("\n¡Error! El id ingresado ya existe\n")
            continue
        else:
            break
    while True:
        st = False
        nueNomCiu = leerString("\nIngrese el nombre de la ciudad: ")
        for dep in dat["Departamentos"]:
            for ciu in dep["Ciudades"]:
                if nueNomCiu.lower() == ciu["nomCiudad"].lower():
                    st = True
                    break
        if st == True:
            print("\n¡Error! El nombre ingresado ya existe\n")
            continue
        else:
            break
    nueImgCiu = leerString("Ingrese la ruta de la imagen de la ciudad: ")
    nueCorLat = leerFloat("Ingrese la coordenada de latitud de la ciudad: ")
    nueCorLon = leerFloat("Ingrese la coordenada de longitud de la ciudad:")
    for dep in dat["Departamentos"]:
            if dep["idDep"] == id:
                dep["Ciudades"].append({
                    "idCiudad": nueIdCiu,
                    "nomCiudad": nueNomCiu,
                    "imagen": nueImgCiu,
                    "coordenadas": {"lat":nueCorLat, "lon":nueCorLon}
                })
    print("\nCIUDAD AGREGADA")
    input("\nIngrese cualquier letra o numero para continuar--> ")

def eliCiu(dat):
    print("ELIMINAR UNA CIUDAD\n")
    while True:
        st = False
        id = leerInt("Ingrese el id del departamento: ")
        for dep in dat["Departamentos"]:
            if id == dep["idDep"]:
                st = True
                break
        if st == False:
            print("\n¡Error! El id ingresado no existe\n")
            continue
        else:
            break
    while True:
        st = False
        id = leerInt("Ingrese el id de la ciudad que quiere eliminar: ")
        for dep in dat["Departamentos"]:
            cont = 0
            for ciu in dep["Ciudades"]:
                if id == ciu["idCiudad"]:
                    st = True
                    dep["Ciudades"].pop(cont)
                    break
                cont += 1
        if st == False:
            print("\n¡Error! El id ingresado no existe\n")
            continue
        else:
            break
    print("\nCIUDAD ELIMINADA")
    input("\nIngrese cualquier letra o numero para continuar--> ")
    
def adcDep(dat):
    print("AÑADIR UN DEPARTAMENTO\n")
    while True:
        st = False
        id = leerInt("Ingrese el id del departamento: ")
        for dep in dat["Departamentos"]:
            if id == dep["idDep"]:
                st = True
                break
        if st == True:
            print("\n¡Error! El id ingresado ya existe\n")
            continue
        else:
            break
    while True:
        st = False
        nueNomCiu = leerString("\nIngrese el nombre del departamento: ")
        for dep in dat["Departamentos"]:
                if nueNomCiu.lower() == dep["nomDepartamento"].lower():
                    st = True
                    break
        if st == True:
            print("\n¡Error! El nombre ingresado ya existe")
            continue
        else:
            break

    print("\nDEPARTAMENTO AGREGADO")
    input("\nIngrese cualquier letra o numero para continuar--> ")

def eliDep(dat):
    print("ELIMINAR UN DEPARTAMENTO")
    while True:
        st = False
        id = leerInt("\nIngrese el id del departamento: ")
        for dep in dat["Departamentos"]:
            cont = 0
            if id == dep["idDep"]:
                st = True
                dat["Departamentos"].pop(cont)
                break
            cont += 1
        if st == False:
            print("\n¡Error! El id ingresado no existe\n")
            continue
        else:
            break
    print("\nDEPARTAMENTO ELIMINADO")
    input("\nIngrese cualquier letra o numero para continuar--> ")

def listDep(dat):
    print("LISTADO DE DEPARTAMENTOS")
    for dep in dat["Departamentos"]:
        print("_"*50)
        print(f"\nId departmento: {dep['idDep']}\n")
        print(f"Nombre: {dep['nomDepartamento']}")
        for ciu in dep["Ciudades"]:
            if ciu == {}:
                break
            print(f"Id ciudad: {ciu['idCiudad']}")
            print(f"Nombre: {ciu['nomCiudad']}")
            print(f"Imagen: {ciu['imagen']}")
            print(f"Coordenadas: [{ciu['coordenadas']['lat']:,.0f}, {ciu['coordenadas']['lon']:,.0f}]\n")
    input("Ingrese cualquier letra o numero para continuar--> ")

datos = cargarDat()
while True:
    clear()
    op = menu()
    if op == 1:
        clear()
        listCiu(datos)
    elif op == 2:
        clear()
        adcCiu(datos)
    elif op == 3:
        clear()
        eliCiu(datos)
    elif op == 4:
        clear()
        adcDep(datos)
    elif op == 5:
        clear()
        eliDep(datos)
    elif op == 6:
        clear()
        listDep(datos)
    else:
        with open("Campus-main/Repasos/PaísCiudad.json", "w") as archivo:
            json.dump(datos, archivo, indent = 4)
        print("\nFin del programa")
        break
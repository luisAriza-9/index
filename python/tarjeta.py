import json

def leerInt(msg):
    while True:
        try:
            iNum = int(input(msg))
            return iNum
        except ValueError:
            print("_" * 75)
            print("Ingrese un número entero válido")

def leerFloat(msg):
    while True:
        try:    
            fNum = float(input(msg))
            return fNum
        except ValueError:
            print("_" * 75)
            print("Ingrese un número decimal válido")

def leerString(msg):
    while True:
        sNom = input(msg)
        if sNom.strip() == "":
            print("\nPor favor ingrese un nombre válido")
        else:
            return sNom

def cargarInfo(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def sobreInfo(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)
        print("_" * 50)
        print("\nDatos guardados")

def menu(opciones, mensaje):
    while True:
        print("_" * 50)
        print("MENU PRINCIPAL\n")
        for key, value in opciones.items():
            print(f"{key}. {value}")
        opc = leerInt(mensaje)
        if opc not in opciones:
            print("Ingrese un valor válido")
        else:
            return opc

def menuTC():
    opciones = {
        1: "Añadir",
        2: "Modificar",
        3: "Eliminar",
        4: "Buscar",
        5: "Salir"
    }
    return menu(opciones, "\nIngrese el número de la opción que desea --> ")

def añadirTC(ruta, datBan):
    # Resto del código para la función añadirTC

def modificarTC(ruta, datBan):
    # Resto del código para la función modificarTC

def eliminarTC(ruta, datBan):
    # Resto del código para la función eliminarTC

def tipTC(datBan, cedCli, numTC):
    # Resto del código para la función tipTC

def buscarTC(datBan):
    # Resto del código para la función buscarTC

def tarjetasCre(ruta, datBan):
    # Resto del código para la función tarjetasCre

def menuInformes():
    # Resto del código para la función menuInformes

def informe1(datBan):
    # Resto del código para la función informe1

def informe2(datBan):
    # Resto del código para la función informe2

def informe3(datBan):
    # Resto del código para la función informe3

def informe4(datBan):
    # Resto del código para la función informe4

def informe5(datBan):
    # Resto del código para la función informe5

def informesTC(datBan):
    # Resto del código para la función informesTC

def main():
    ruta = "Filtros/bancoACME.json"
    dataBanco = {}

    while True:
        dataBanco = cargarInfo(ruta)
        opciones_menu = {
            1: "Tarjetas de crédito",
            2: "Informes",
            3: "Salir"
        }
        op = menu(opciones_menu, "\nIngrese el número de la opción que desea --> ")
        if op == 1:
            tarjetasCre(ruta, dataBanco)
        elif op == 2:
            informesTC(dataBanco)
        else:
            print("\nFIN DEL PROGRAMA. GRACIAS POR USAR NUESTROS SERVICIOS")
            input("\nPresione cualquier tecla para salir -->")
            break

if __name__ == "__main__":
    main()
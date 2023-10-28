import json

def leerInt(msg):
    while True:
        try:
            iNum = int(input(msg))
            return iNum
        except ValueError:
            print("_" * 75)
            print("Ingrese un numero entero valido")

def leerString(msg):
    while True:
        try:
            sNom = input(msg)
            if sNom.strip() == "":
                print("\nPor favor ingrese un nombre valido")
                continue
            return sNom
        except Exception as e:
            print("\nError al ingresar un nombre" , e.message)

def menu():
    while True:
        print("_" * 50)
        print("\nMENU\n"
            "\n1.Productos\n"
            "2.Ventas\n"
            "3.Informe\n"
            "4.Salir")
        print("_" * 50)
        opc = leerInt("\nIngrese el numero de la opción que desea -->")
        if opc < 1 or opc > 4:
            print("Ingrese un valor valido")
            continue
        return opc

def productos():
    produc = {}
    while True:
        print("_" * 50)
        print("\nBIENVENIDO AL MENU PARA AGREGAR PRODUCTOS")
        print("_" * 50)
        codPro = leerInt("Ingrese el codigo del producto: ")
        print("_" * 50)
        nomPro = leerString("Ingrese el nombre del producto: ")
        print("_" * 50)        
        valPro = leerInt("Ingrese el valor del producto: ")
        while True:
            print("_" * 50)
            print("Ingrese la categoria del IVA")
            print("\n1.Exento (0% IVA)")
            print("\n2.Bienes (5% IVA)")
            print("\n3.Generales (19% IVA)")
            desIva = leerInt("\n-->")
            if desIva == 1:
                ivaPro = 0
            elif desIva == 2:
                ivaPro = 0.05
            elif desIva ==3:
                ivaPro = 0.19
            else:
                print("\nIngrese una opción valida")
                continue
            break
        produc[codPro] = {}
        produc[codPro]["Nombre"] = nomPro
        produc[codPro]["Valor"] = valPro
        produc[codPro]["IVA"] = ivaPro
        with open("Productos.json", "w") as archivo:
            json.dump(produc, archivo)
            print("Se ha escrito en disco")
        desSeg = leerInt("¿Desea ingresar algun otro producto (1 para si) (2 para no)?")
        if desSeg == 1:
            continue
        break

def ventas():
    while True:
        with open("Clientes.json", "r", encoding = "utf-8") as archivo:
            clientes = json.load(archivo)
        with open("Productos.json", "r", encoding = "utf-8") as archivo:
            produc = json.load(archivo)
        print("_" * 50)
        print("\nBIENVENIDO AL MENU PARA VENDER")
        cedCli = leerInt("Ingrese su numero de cedula: ")
        if str(cedCli) in clientes:
            print("Bienvenido de nuevo")
        else:
            print("Detectamos que es un nuevo cliente, bienvenido")
        while True:
            while True:
                codPro = leerInt("Ingrese el codigo del producto que desea comprar: ")
                if str(codPro) in produc:
                    print(f"Producto {produc[str(codPro)]['Nombre']} añadido a la compra")
                    break
                else:
                    print("El codigo del producto no existe, vuelvalo a intentar")
                    continue
            desSeg = leerInt("¿Desea comprar algun otro producto? (1 para si) (2 para no)")
            if desSeg == 1:
                continue
            print("Compra finalizada")
            #Facturación
            print("FACTURA")
            break
        desCli = leerInt("¿Desea hacer una venta a otro cliente? (1 para si) (2 para no)")
        if desSeg == 1:
            continue
        break
        
    
        
    
    

while True:
    op = menu()
    if op == 1:
        productos()
        input("\nOprima cualquier letra para dirigirse al menu principal")
    elif op ==2:
        ventas()
        input("\nOprima cualquier letra para dirigirse al menu principal")
    elif op ==3:
        input("\nOprima cualquier letra para dirigirse al menu principal")
    else:
        print("\nFin del programa")
        break
import json

def leerInt(msg):
    while True:
        try:
            iNum = int(input(msg))
            return iNum
        except ValueError:
            print("_" * 75)
            print("Ingrese un numero entero valido")

def leerFloat(msg):
    while True:
        try:    
            iNum = float(input(msg))
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

def cargarInfo(ruta, datos):
    aJ = open(ruta, "a+", encoding = "utf-8")
    aJ.seek(0)
    try:
        datos = json.load(aJ)
    except Exception as e:
        datos = {}
    aJ.close()
    return datos

def sobreInfo(ruta, datos):
    with open(ruta, "w") as archivo:
        json.dump(datos, archivo)
        print("_" * 50)
        print("\nDatos guardados")

def menu():
    while True:
        print("_" * 50)
        print("MENU PRINCIPAL\n"
            "\n1.Tarjetas de credito\n"
            "2.Informes\n"
            "3.Salir")
        opc = leerInt("\nIngrese el numero de la opción que desea --> ")
        if opc < 1 or opc > 3:
            print("Ingrese un valor valido")
            continue
        return opc

def menuTC():
    while True:
        print("_" * 50)
        print("MENU TARJETAS DE CREDITO\n"
            "\n1.Añadir\n"
            "2.Modificar\n"
            "3.Eliminar\n"
            "4.Buscar\n"
            "5.Salir")
        opc = leerInt("\nIngrese el numero de la opción que desea --> ")
        if opc < 1 or opc > 5:
            print("\nIngrese un valor valido")
            continue
        return opc

def añadirTC(rut, datBan):
    print("_" * 50)
    print("AÑADIR")
    cedCli = leerInt("\nIngrese el numero de cedula del cliente: ")
    if str(cedCli) in datBan:
        print("_" * 50)
        print("\nEl usuario esta registrado".upper())
        r = 1
    else:
        print("_" * 50)
        print("\nEl usuario no esta registrado".upper())
        r = 0
        nomCli = leerString("\nIngrese el nombre del nuevo cliente: ")
        while True:
            genCli = leerString("\nIngrese el genero del cliente(F o M): ")
            if genCli.upper() == "F" or genCli.upper() == "M":
                break
            print("\nIngrese solo F o M")
        while True:
            telCli = leerString("\nIngrese el numero de telefono del cliente: ")
            if len(telCli) != 10:
                print("\nEl numero de telefono tiene que tener 10 numeros")
                continue
            break
    while True:
        print("_" * 50)
        print("\nTipos de tarjeta\n"
            "\n1.MasterCard\n"
            "2.Visa\n"
            "3.American Express")
        print("_" * 50)
        tipTC = leerInt("\nIngrese el numero de la opción que desea --> ")
        if tipTC < 1 or tipTC > 3:
            print("\nIngrese un valor valido")
            continue
        break
    numTC = leerInt("\nIngrese el numero de la tarjeta: ")
    while True:
        mesTC = leerInt("\nIngrese el mes de vencimiento de la tarjeta: ")
        if mesTC < 1 or mesTC > 12:
            print("\nEl mes tiene que estar entre 1 y 12")
            continue
        break
    anTC = leerInt("\nIngrese el año de vencimiento de la tarjeta: ")
    while True:
        codTC = leerInt("\nIngrese el codigo de verificación de la tarjeta: ")
        if codTC < 100 or codTC > 999:
            print("\nEl codigo de verificación debe estar entre 100 y 999")
            continue
        break
    if r == 0:
        datBan[str(cedCli)] = {}
        datBan[str(cedCli)]["Nombre"] = nomCli
        datBan[str(cedCli)]["Telefono"] = telCli
        datBan[str(cedCli)]["Genero"] = genCli.upper()
    datBan[str(cedCli)][numTC] = {}
    datBan[str(cedCli)][numTC]["Tipo"] = tipTC
    datBan[str(cedCli)][numTC]["Mes"] = mesTC
    datBan[str(cedCli)][numTC]["Año"] = anTC
    datBan[str(cedCli)][numTC]["Codigo V"] = codTC
    
    sobreInfo(rut, datBan)

def modificarTC(rut, datBan):
    print("_" * 50)
    print("MODIFICAR")
    while True:
        cedCli = leerString("\nIngrese la cedula del cliente: ")
        if cedCli in datBan:
            break
        else:
            print("\nLa cedula del cliente no esta registrada")
            continue
    while True:
        print("_" * 50)
        print("¿Que desea modificar?")
        print("\n1.Nombre del cliente")
        print("2.Telefono del cliente")
        print("3.Genero del cliente")
        print("4.Tarjeta de credito")
        op = leerInt("\nIngrese el numero de la opción que desea -->")
        if op < 1 or op > 4:
            print("\nIngrese una opción valida")
            continue
        break
    if op == 1:
        nueNomCli = leerString("\nIngrese el nuevo nombre del cliente: ")
        datBan[cedCli]["Nombre"] = nueNomCli
    elif op == 2:
        while True:
            nuetelCli = leerString("\nIngrese el nuevo numero de telefono del cliente: ")
            if len(nuetelCli) != 10:
                print("\nEl numero de telefono tiene que tener 10 numeros")
                continue
            break
        datBan[cedCli]["Telefono"] = nuetelCli
    elif op == 3:
        while True:
            nuegenCli = leerString("\nIngrese el nuevo genero del cliente(F o M): ")
            if nuegenCli.upper() == "F" or nuegenCli.upper() == "M":
                break
            print("\nIngrese solo F o M")
        datBan[cedCli]["Genero"] = nuegenCli
    elif op == 4:
        while True:
            numTC = leerInt("\nIngrese el numero de la tarjeta del cliente: ")
            if str(numTC) in datBan[cedCli]:
                break
            else:
                print("\nEl numero de la tarjeta de credito no existe")
        while True:
            print("_" * 50)
            print("¿Que desea modificar?")
            print("\n1.Fecha de vencimiento")
            print("2.Codigo de verificación")
            print("3.Tipo de tarjeta")
            op = leerInt("\nIngrese el numero de la opción que desea -->")
            if op < 1 or op > 3:
                print("\nIngrese una opción valida")
                continue
            break
        if op == 1:
            nueMesTC = leerString("\nIngrese el nuevo mes de vencimiento: ")
            nueAnTC = leerString("\nIngrese el nuevo año de vencimiento: ")
            datBan[cedCli][str(numTC)]["Mes"] = nueMesTC
            datBan[cedCli][str(numTC)]["Año"] = nueAnTC
        elif op == 2:
            while True:
                nuecodTC = leerInt("\nIngrese el codigo de verificación de la tarjeta: ")
                if nuecodTC < 100 or nuecodTC > 999:
                    print("\nEl codigo de verificación debe estar entre 100 y 999")
                    continue
                break
            datBan[cedCli][str(numTC)]["Codgio V"] = nuecodTC
        else:
            while True:
                print("_" * 50)
                print("\nTipos de tarjeta\n"
                    "\n1.MasterCard\n"
                    "2.Visa\n"
                    "3.American Express")
                print("_" * 50)
                nuetipTC = leerInt("\nIngrese el numero de la opción que desea --> ")
                if nuetipTC < 1 or nuetipTC > 3:
                    print("\nIngrese un valor valido")
                    continue
                break
            datBan[cedCli][str(numTC)]["Tipo"] = nuetipTC
    sobreInfo(rut, datBan)

def eliminarTC(rut, datBan):
    print("_" * 50)
    print("ELIMINAR")
    while True:
        while True:
            des = leerInt("\nPara elimiar un cliente ingrese 1, para eliminar una tarjeta ingrese 2 --> ")
            if des < 1 or des > 2:
                print("\nIngrese una opción valida")
                continue
            break
        while True:
            cedCli = leerString("\nIngrese la cedula del cliente: ")
            if cedCli in datBan:
                break
            else:
                print("\nLa cedula del cliente no esta registrada")
                continue
        if des == 1:
            datBan.pop(cedCli)
            break
        while True:
            numTC = leerInt("\nIngrese el numero de la tarjeta del cliente: ")
            if str(numTC) in datBan[cedCli]:
                break
            else:
                print("\nEl numero de la tarjeta de credito no existe")
        datBan[cedCli].pop(str(numTC))
        break
    sobreInfo(rut, datBan)

def tipTC(datBan, cedCli, numTC):
    if datBan[str(cedCli)][str(numTC)]["Tipo"] == 1:
        tT = "Master Card"
    elif datBan[str(cedCli)][str(numTC)]["Tipo"] == 2:
        tT = "Visa"
    else:
        tT = "American Express"
    return tT

def buscarTC(datBan):
    print("_" * 50)
    print("BUSCAR")
    while True:
        cedCli = leerString("\nIngrese la cedula del cliente: ")
        if cedCli in datBan:
            break
        else:
            print("\nLa cedula del cliente no esta registrada")
            continue
    while True:
        numTC = leerInt("\nIngrese el numero de la tarjeta del cliente: ")
        if str(numTC) in datBan[cedCli]:
            break
        else:
            print("\nEl numero de la tarjeta de credito no existe")
    tT = tipTC(datBan, cedCli, numTC)
    print(f"\nNumero de la tarjeta de credito: {numTC}\n"
          f"Tipo de tarjeta: {tT}\n"
          f"Fecha de vencimiento: {datBan[str(cedCli)][str(numTC)]['Mes']} del {datBan[str(cedCli)][str(numTC)]['Año']}\n"
          f"Codigo de verificación: {datBan[str(cedCli)][str(numTC)]['Codigo V']}")

def tarjetasCre(rut, datBan):
    while True:
        op = menuTC()
        if op == 1:
            añadirTC(rut, datBan)
            input("\nPresione cualquier tecla para volver al menu de tarjetas de credito -->")
        elif op == 2:
            modificarTC(rut, datBan)
            input("\nPresione cualquier tecla para volver al menu de tarjetas de credito -->")
        elif op == 3:
            eliminarTC(rut, datBan)
            input("\nPresione cualquier tecla para volver al menu de tarjetas de credito -->")
        elif op == 4:
            buscarTC(datBan)
            input("\nPresione cualquier tecla para volver al menu de tarjetas de credito -->")
        else:
            input("\nPresione cualquier tecla para volver al menu principal -->")
            break

def menuInformes():
    while True:
        print("_" * 50)
        print("MENU TARJETAS DE INFORMES\n"
            "\n1.Tarjetas de credito de un cliente especifico\n"
            "2.Información de una tarjeta de credito\n"
            "3.Listado de tarjetas de credito\n"
            "4.Listado de clientes\n"
            "5.Cantidad de tarjetas de credito de cada tipo\n"
            "6.Salir")
        opc = leerInt("\nIngrese el numero de la opción que desea --> ")
        if opc < 1 or opc > 6:
            print("\nIngrese un valor valido")
            continue
        return opc

def informe1(datBan):
    print("_" * 50)
    print("INFORME DE TARJETAS DE CADA CLIENTE")
    while True:
        cedCli = leerString("\nIngrese la cedula del cliente: ")
        if cedCli in datBan:
            break
        else:
            print("\nLa cedula del cliente no esta registrada")
            continue
    i = 0
    print(f"\nNombre : {datBan[cedCli]['Nombre']}\n")
    for e in datBan[cedCli].keys():
        if e == "Nombre" or e == "Telefono" or e == "Genero":
            pass
        else:
            tT = tipTC(datBan, cedCli, e)
            print(f"Tarjeta {i+1}: {e}\n"
                  f"Tipo de tarjeta: {tT}\n"
                  f"Fecha de vencimiento: {datBan[str(cedCli)][e]['Mes']} del {datBan[str(cedCli)][e]['Año']}\n"
                  f"Codigo de verificación: {datBan[str(cedCli)][e]['Codigo V']}\n")
            i += 1

def informe2(datBan):
    print("_" * 50)
    print("INFORME DE UNA TARJETA DE CREDITO")
    while True:
        cedCli = leerString("\nIngrese la cedula del cliente: ")
        if cedCli in datBan:
            break
        else:
            print("\nLa cedula del cliente no esta registrada")
            continue
    while True:
        numTC = leerInt("\nIngrese el numero de la tarjeta del cliente: ")
        if str(numTC) in datBan[cedCli]:
            break
        else:
            print("\nEl numero de la tarjeta de credito no existe")
    tT = tipTC(datBan, cedCli, numTC)
    print(f"\nNumero de la tarjeta de credito: {numTC}\n"
          f"Tipo de tarjeta: {tT}\n"
          f"Fecha de vencimiento: {datBan[str(cedCli)][str(numTC)]['Mes']} del {datBan[str(cedCli)][str(numTC)]['Año']}\n"
          f"Codigo de verificación: {datBan[str(cedCli)][str(numTC)]['Codigo V']}\n"
          f"Identificacion del cliente: {cedCli}\n"
          f"Nombre del cliente: {datBan[str(cedCli)]['Nombre']}\n"
          f"Telefono del cliente: {datBan[str(cedCli)]['Telefono']}\n"
          f"Genero del cliente: {datBan[str(cedCli)]['Genero'].upper()}")

def informe3(datBan):
    print("_" * 50)
    print("LISTADO DE TARJETAS DE CREDITO\n")
    for e in datBan.keys():
        nom = datBan[e]["Nombre"]
        datBan[e].pop("Nombre")
        datBan[e].pop("Telefono")
        datBan[e].pop("Genero")
        for i in datBan[e].keys():
            tT = tipTC(datBan, e, i)
            print(f"Numero de la tarjeta de credito: {i}\n"
                    f"Fecha de vencimiento: {datBan[e][i]['Mes']} del {datBan[e][i]['Año']}\n"
                    f"Tipo de tarjeta: {tT}\n"
                    f"Identificacion del cliente: {e}\n"
                    f"Nombre del cliente: {nom}\n")

def informe4(datBan):
    print("_" * 50)
    print("LISTADO DE CLIENTES")
    for e in datBan.keys():
        print(f"\nNombre: {datBan[e]['Nombre']}\n"
              f"Cedula: {e}\n"
              f"Telefono: {datBan[e]['Telefono']}")

def informe5(datBan):
    print("_" * 50)
    print("CANTIDAD DE TARJETAS")
    numTC = 0
    contMC = 0
    contV = 0
    contAE = 0
    for e in datBan.keys():
        datBan[e].pop("Nombre")
        datBan[e].pop("Telefono")
        datBan[e].pop("Genero")
        for i in datBan[e].keys():
            if datBan[e][i]["Tipo"] == 1:
                tT = "Master Card"
                contMC += 1
            elif datBan[e][i]["Tipo"] == 2:
                tT = "Visa"
                contV += 1
            else:
                tT = "American Express"
                contAE += 1
            numTC +=1
    print(f"\nEl banco tiene emitidas {numTC} tarjetas de credito\n"
          f"\nMasterCard: {contMC}\n"
          f"Visa: {contV}\n"
          f"American Express: {contAE}")

def informesTC(datBan):
    while True:
        op = menuInformes()
        if op == 1:
            informe1(datBan)
            input("\nPresione cualquier tecla para volver al menu de informes -->")
        elif op == 2:
            informe2(datBan)
            input("\nPresione cualquier tecla para volver al menu de informes -->")
        elif op == 3:
            informe3(datBan)
            input("\nPresione cualquier tecla para volver al menu de informes -->")
        elif op == 4:
            informe4(datBan)
            input("\nPresione cualquier tecla para volver al menu de informes -->")
        elif op == 5:
            informe5(datBan)
            input("\nPresione cualquier tecla para volver al menu de informes -->")
        else:
            input("\nPresione cualquier tecla para volver al menu principal -->")
            break

ruta = "Filtros/bancoACME.json"
dataBanco = {}

while True:
    dataBanco = cargarInfo(ruta, dataBanco)
    op = menu()
    if op == 1:
        tarjetasCre(ruta, dataBanco)
    elif op == 2:
        informesTC(dataBanco)
    else:
        print("\nFIN DEL PROGRAMA GRACIAS POR USAR NUESTROS SERVICIOS")
        input("\nPresione cualquier tecla para salir -->")
        break
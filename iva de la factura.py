
import io
import json

#Leer String

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

#Leer Int

def leerInt(msg):
    while True:
        try:
            print("_" * 70)
            iNum = int(input(msg))
            return iNum
        except ValueError:
            print("_" * 70)
            print("\nIngrese un numero entero valido")

#Leer Float

def leerFloat(msg):
    while True:
        try:
            print("_" * 70)
            iNum = float(input(msg))
            return iNum
        except ValueError:
            print("_" * 70)
            print("\nIngrese un numero decimal valido")

#Menu basico

def menu():
    while True:
        print("_" * 75)
        print("\nMENU")
        print("_" * 75)
        print("\n1.")
        print("2.")
        print("3. Salir")
        op = leerInt("\nSeleccione una opción de 1 a 3: ")
        if op < 1 or op > 3:
            print("Opcion no valida")
            continue
        return op
    
#Cantidad de palabras de una cadena de texto

def palabrasString():
    print("_" * 75)
    print("\n----- 1. CANTIDAD DE PALABRAS EN UN STRING -----")
    sString = input("Ingrese el string: ")
    print("_" * 75)
    iCont = 0
    for i in range(0, len(sString)):
        if sString[i] == " ":
            iCont += 1
    print(f"El string ({sString}) contiene {iCont + 1} palabras")
    input("\nPresione cualquier tecla para volver al menu--->")
    pass

#Metodo de euclides para calcular mcd

def metEuclides(iNum1, iNum2):
    fModDiv = iNum1 % iNum2
    if fModDiv == 0:
        print(f"El mcd de {iNum1} y {iNum2} es {iNum2}")
    else:
        while True:
            fModDivn = iNum2 % fModDiv
            if fModDivn == 0:
                print(f"\nEl mcd de los numeros ingresados es {fModDiv}")
                break
            iNum2 = fModDiv
            fModDiv = fModDivn
            continue

#IVA de un producto

def iva(iValProduc, iIva = 21):
    print("_" * 75)
    print("\n----- 3. CALCULAR EL IVA DE UNA FACTURA -----")
    iProducIva = iValProduc + (iValProduc * (iIva / 100))
    print("_" * 75)
    print("\nFACTURA\n"
          f"\nValor del producto: {iValProduc:,.0f}\n"
          f"Porcentaje de IVA: {iIva}%\n"
          f"Total a pagar: {iProducIva:,.0f}")
    input("\nPresione cualquier tecla para volver al menu--->")  

#Agregar con diccionarios

def agregar(empleados, ids, nom, horasT, valorH):
    empleados[ids] = {}
    empleados[ids]["nombre"] = nom
    empleados[ids]["HorasT"] = horasT
    empleados[ids]["ValorH"] = valorH
    print(empleados)
    
#Modificar con diccionarios

def modificar(empleados):
    id = leerInt("\nIngrese el id del empleado: ")
    for k in empleados.keys():
        if k == id:
            e = k
            break

    print("_"*75)
    print("MENU DE MODIFICACION")
    print("\n1. Nombre")
    print("2. Horas trabajadas")
    print("3. Valor de la hora")
    while True:
        op = leerInt("\nSeleccione el que quiere modificar: ")
        if op < 1 or op > 3:
            print("Ingrese un valor valido")
            continue
        break
    if op == 1:
        print("_" * 75)
        print("Modificar nombre")
        nueNom = leerString("Ingrese el nuevo nombre: ")
        empleados[e]["nombre"] = nueNom
    elif op == 2:
        print("_" * 75)
        print("Modificar horas trabajadas")
        while True:
            nueHor = leerInt("Ingrese el nuevo numero de horas trabajadas del empleado: ")
            if nueHor < 1 or nueHor > 160:
                print("El numero de horas tiene que estar entre 1 y 160")
                continue
            break
        empleados[e]["HorasT"] = nueHor
    elif op == 3:
        print("_" * 75)
        print("Modificar valor de la hora")
        while True:
            nueValor = leerInt("Ingrese el valor unitario de la hora: ")
            if nueValor < 8000 or nueValor > 150000:
                print("El nuevo valor de la horas tiene que estar entre 8.000 y 150.000")
                continue
            break    
        empleados[e]["ValorH"] = nueValor          

#Buscar con diccionarios

def buscar(empleados): 
    id = leerInt("\nIngrese el id del empleado: ")
    for k in empleados.keys():
        if k == id:
            e = k
            break
    print(f"\nNombre: ", empleados[e]["nombre"])
    print(f"\nNumero de horas trabajadas:", empleados[e]["HorasT"])
    print(f"\nValor de la hora: $", empleados[e]["ValorH"])

#Eliminar con diccionarios

def eliminar(empleados):
    id = leerInt("\nIngrese el id del empleado: ")
    for k in empleados.keys():
        if k == id:
            e = k
            break
    empleados.pop(e)    
    print("El empleado ha sido eliminado")

#Listar empleados con paginacion

def listEmpleados(empleados):  
    while True:
        l = 0
        for k in empleados.keys():
            print(f"Id: {k}\tNombre: {empleados[k]['nombre']}\tHoras trabajadas: {empleados[k]['HorasT']}\tValor horas: {empleados[k]['ValorH']:,.0f}")
            l += 1
            if l >= (len(empleados)):
                return
            if l == 5:
                while True:
                    conf = int(input("\nSi desea continuar digite 1, si quiere salir presione 2: "))
                    if conf < 1 or conf > 2:
                        print("Ingrese una opción valida")
                        continue
                    break
                if conf == 2:
                    return

#Nomina de un empleado con diccionarios

def nomEmpleado(empleados):
    auxi = 0
    id = leerInt("\nIngrese el id del empleado: ")
    for k in empleados.keys():
        if k == id:
            e = k
            break
    salBru = empleados[e]["HorasT"] * empleados[e]["ValorH"]
    if salBru < 1160000:
        auxi = 140606
    desPen = salBru * 0.04 
    desEPS = salBru * 0.04
    salNet = salBru + auxi - desPen - desEPS

    print(f"Id: {e}\tNombre: {empleados[e]['nombre']}\tHoras trabajadas: {empleados[e]['HorasT']}\tValor horas: {empleados[e]['ValorH']:,.0f}")
    print(f"Salario Bruto: {salBru:,.0f}\tAuxilio: {auxi:,.0f}\tDescuento pensión: -{desPen:,.0f}\tDescuento EPS: -{desEPS:,.0f}\tSalario neto: {salNet:,.0f}")

#Nomina de todos los empleados con paginacion

def nomEmpleados(empleados):
    while True:
        l = 0
        for k in empleados.keys():
                salBru = empleados[k]["HorasT"] * empleados[k]["ValorH"]
                if salBru < 1160000:
                    auxi = 140606
                desPen = salBru * 0.04 
                desEPS = salBru * 0.04
                salNet = salBru + auxi - desPen - desEPS
                print(f"Id: {k}\tNombre: {empleados[k]['nombre']}\tHoras trabajadas: {empleados[k]['HorasT']}\tValor horas: {empleados[k]['ValorH']:,.0f}")
                print(f"Salario Bruto: {salBru:,.0f}\tAuxilio: {auxi:,.0f}\tDescuento pensión: -{desPen:,.0f}\tDescuento EPS: -{desEPS:,.0f}\tSalario neto: {salNet:,.0f}")
                l += 1
                if l >= (len(empleados)):
                    return
                if l == 5:
                    while True:
                        conf = int(input("\nSi desea continuar digite 1, si quiere salir presione 2: "))
                        if conf < 1 or conf > 2:
                            print("Ingrese una opción valida")
                            continue
                        break
                    if conf == 2:
                        return

#Funcion salir para un menu

def salir():
    while True:
        des = leerInt("\nSi desea salir presione 1, si no desea salir presione 2: ")
        if des < 1 or des > 2:
            print("Por favor seleccione una de las dos opciones")
            continue
        return des

#Listar empleados con paginacion en listas

def listEmpleados(lstId, lstNom, lstHor, lstVal):
    ini = 0
    fi = 5
    while True:
        for l in range(ini, fi):
            if l >= len(lstId):
                return
            else:    
                print(f"Id: {lstId[l]}\tNombre: {lstNom[l]}\tHoras trabajadas: {lstHor[l]}\tValor horas: {lstVal[l]:,.0f}")
        while True:
            conf = int(input("\nSi desea continuar digite 1, si quiere salir presione 2: "))
            if conf < 1 or conf > 8:
                print("Ingrese una opción valida")
                continue
            break
        if conf == 2:
            return
        ini +=5
        fi +=5   

#Leer archivo json y meterlo

def cargarArch():
    with open("13-Ejercicio1_archivoJson_emplacme.json", "r", encoding = "utf-8") as archivo:
        emAc = json.load(archivo)
        print(emAc)
    return emAc

#Reescribir archivo json al subirlo

def subirArc():
    empleadosAr = {}
    with open("13-Ejercicio1_archivoJson_emplacme.json", "w", encoding = "utf-8") as archivo:
        json.dump(empleadosAr, archivo)
        print("Se ha escrito en disco")

#ordenar datos de un diccionario por llave

desserts = {
    "Ice cream":10,
    "Brownies":12,
    "Cheesecake":3,
    "Swiss roll":5,
    "Cookies":4,
    "Cup cake":2
}

keys = desserts.keys()
print(keys)

#Output
# ['Ice cream', 'Brownies', 'Cheesecake', 'Swiss roll', 'Cookies', 
# 'Cup cake']

sorted_keys = sorted(keys)
print(sorted_keys)

# # Output
# ['Brownies', 'Cheesecake', 'Cookies', 'Cup cake', 'Ice cream', 'Swiss roll']

sorted_desserts = {}
for key in sorted_keys:
  sorted_desserts[key] = desserts[key]

print(sorted_desserts)

# # Output
# {'Brownies': 12, 'Cheesecake': 3, 'Cookies': 4, 'Cup cake': 2, 
# 'Ice cream': 10, 'Swiss roll': 5}

sorted_desserts = {key:desserts[key] for key in sorted_keys}
print(sorted_desserts)

# {'Brownies': 12, 'Cheesecake': 3, 'Cookies': 4, 'Cup cake': 2, 
# 'Ice cream': 10, 'Swiss roll': 5}

#ordenar datos de un diccionario por llave

desserts.items()

# dict_items([('Ice cream', 10), ('Brownies', 12), ('Cheesecake', 3), 
# ('Swiss roll', 5), ('Cookies', 4), ('Cup cake', 2)])

dict_items = desserts.items()
for item in dict_items:
  print(f"key:{item[0]},value:{item[1]}")

# # Output
# key:Ice cream,value:10
# key:Brownies,value:12
# key:Cheesecake,value:3
# key:Swiss roll,value:5
# key:Cookies,value:4
# key:Cup cake,value:2

sorted_desserts = dict(sorted(desserts.items(), key=lambda item:item[1]))
print(sorted_desserts)

# {'Cup cake': 2, 'Cheesecake': 3, 'Cookies': 4, 'Swiss roll': 5, 
# 'Ice cream': 10, 'Brownies': 12}

sorted_desserts = {key:value for key, value in sorted(desserts.items(), 
key=lambda item:item[1])}

print(sorted_desserts)

# # Output
# {'Cup cake': 2, 'Cheesecake': 3, 'Cookies': 4, 'Swiss roll': 5, 
# 'Ice cream': 10, 'Brownies': 12}

sorted_desserts = dict(sorted(desserts.items(), key=lambda item:item[1], 
reverse=True))
print(sorted_desserts)

# # Output
# {'Brownies': 12, 'Ice cream': 10, 'Swiss roll': 5, 'Cookies': 4, 
# 'Cheesecake': 3, 'Cup cake': 2}
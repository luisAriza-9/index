# Insertar -> para insertar nuevos registros en el fichero de libros
# Consulta -> busca registros por código
import json

# funciones

# funcion editar libros

def modificarLibro(lstLibros, rutaFile):  
    fd = open(rutaFile , "w")

    print("\n\n3. Editar información del libro") 
    cod = input("Ingrese el código del libro: ")

    if not existeCod(cod , lstLibros): 
        print("El libro no existe") 
        input("Presione Enter para continuar")
        return  
    
    op = int(input("\n1. Título\n2. Autor\n3. Precio\nOpcion[1-3]? "))

    for i in range(len(lstLibros)):
        datos = lstLibros[i]
        k = list(datos.keys())[0]
        if k == cod:
            for elemento in lstLibros[i]:

                if op == 1: 
                    titulo = input("Ingrese el título correcto: ")
                    lstLibros[i][elemento]["titulo"] = titulo 

                elif op == 2: 
                    autor = input("Ingrese el autor correcto: ")
                    lstLibros[i][elemento]["autor"] = autor

                elif op == 3: 
                    precio = input("Ingrese el precio correcto: ")
                    lstLibros[i][elemento]["precio"] = precio  

            json.dump(lstLibros, fd)
            fd.close()


# funcion ordenamiento burbuja para cadenas
def burbuja_optimus(lstLibros):
    n = len(lstLibros)
    # print(lstLibros)
    for i in range(n-1):
        intercambio = False
 
        for j in range(n-1-i):
            # k -> llave del codigo de la posición j de la lista
            # k1 -> llave del codigo de la posicion j+1 de la lista
            k = list(lstLibros[j].items())[0][0]
            k1 = list(lstLibros[j+1].items())[0][0]
            print(list(lstLibros[j].items())[0][1]["titulo"])
            #print("K, K+1, nombre: ", k, k1, nom)
            if k > k1:
                lstLibros[j], lstLibros[j+1] = lstLibros[j+1], lstLibros[j]
                intercambio = True
 
        if intercambio == False:
            break
    return lstLibros


# funcion listar libros por título
def listarLibrosTitulo(lstLibros):
    ini = 0
    fin = 3
    n = len(lstLibros)
    # print(lstLibros)
    for i in range(n-1):
        intercambio = False
 
        for j in range(n-1-i):
            # k -> llave del codigo de la posición j de la lista
            # k1 -> llave del codigo de la posicion j+1 de la lista
            k = list(lstLibros[j].items())[0][1]["titulo"]
            k1 = list(lstLibros[j+1].items())[0][1]["titulo"]
            #print(list(lstLibros[j].items())[0][1]["titulo"])
            #print("K, K+1, nombre: ", k, k1, nom)
            if k > k1:
                lstLibros[j], lstLibros[j+1] = lstLibros[j+1], lstLibros[j]
                intercambio = True
 
        if intercambio == False:
            break
    #print(f"\nTítulo \t\t\tAutor \t\t\tPrecio \t\tcódigo")
    print("{:<20} {:<20} {:<20}".format("Libro", "Autor", "Precio"))
    while True:
        for i in range(ini,fin):
            if i >= len(lstLibros):
                return
            else:  
                for elemento in lstLibros[i]:  
                    #print(f"{lstLibros[i][elemento]['titulo']}\t\t\t{lstLibros[i][elemento]['autor']}\t\t\t${lstLibros[i][elemento]['precio']:,}")
                    print("{:<20} {:<20} {:<20}".format(lstLibros[i][elemento]['titulo'],lstLibros[i][elemento]['autor'],lstLibros[i][elemento]['precio']))
        while True:
            continuar = int(input("\nSi desea continuar digite 1, si quiere salir presione 2: "))
            if continuar < 1 or continuar > 2:
                print("Ingrese una opción valida")
                continue
            break
        if continuar == 2:
            return
        ini +=3
        fin +=3
    return lstLibros

# funcion listar libros por autor
def listarLibrosAutor(lstLibros):
    ini = 0
    fin = 3
    n = len(lstLibros)
    # print(lstLibros)
    for i in range(n-1):
        intercambio = False
 
        for j in range(n-1-i):
            # k -> llave del codigo de la posición j de la lista
            # k1 -> llave del codigo de la posicion j+1 de la lista
            k = list(lstLibros[j].items())[0][1]["autor"]
            k1 = list(lstLibros[j+1].items())[0][1]["autor"]
            #print(list(lstLibros[j].items())[0][1]["titulo"])
            #print("K, K+1, nombre: ", k, k1, nom)
            if k > k1:
                lstLibros[j], lstLibros[j+1] = lstLibros[j+1], lstLibros[j]
                intercambio = True
 
        if intercambio == False:
            break
    #print(f"\nTítulo \t\t\tAutor \t\t\tPrecio \t\tcódigo")
    print("{:<20} {:<20} {:<20}".format( "Autor", "Título Libro", "Precio"))
    while True:
        for i in range(ini,fin):
            if i >= len(lstLibros):
                return
            else:  
                for elemento in lstLibros[i]:  
                    #print(f"{lstLibros[i][elemento]['titulo']}\t\t\t{lstLibros[i][elemento]['autor']}\t\t\t${lstLibros[i][elemento]['precio']:,}")
                    print("{:<20} {:<20} {:<20}".format(lstLibros[i][elemento]['autor'],lstLibros[i][elemento]['titulo'],lstLibros[i][elemento]['precio']))
        while True:
            continuar = int(input("\nSi desea continuar digite 1, si quiere salir presione 2: "))
            if continuar < 1 or continuar > 2:
                print("Ingrese una opción valida")
                continue
            break
        if continuar == 2:
            return
        ini +=3
        fin +=3
    return lstLibros
    
# funcion listar libros por precio
def listarLibrosPrecio(lstLibros):
    ini = 0
    fin = 3
    n = len(lstLibros)
    # print(lstLibros)
    for i in range(n-1):
        intercambio = False

        for j in range(n-1-i):
            # k -> llave del codigo de la posición j de la lista
            # k1 -> llave del codigo de la posicion j+1 de la lista
            k = list(lstLibros[j].items())[0][1]["precio"]
            k1 = list(lstLibros[j+1].items())[0][1]["precio"]
            #print(list(lstLibros[j].items())[0][1]["titulo"])
            #print("K, K+1, nombre: ", k, k1, nom)
            if k > k1:
                lstLibros[j], lstLibros[j+1] = lstLibros[j+1], lstLibros[j]
                intercambio = True

        if intercambio == False:
            break
    #print(f"\nTítulo \t\t\tAutor \t\t\tPrecio \t\tcódigo")
    print("{:<20} {:<20} {:<20}".format("Precio", "Autor", "Título Libro"))
    while True:
        for i in range(ini,fin):
            if i >= len(lstLibros):
                return
            else:  
                for elemento in lstLibros[i]:  
                    #print(f"{lstLibros[i][elemento]['titulo']}\t\t\t{lstLibros[i][elemento]['autor']}\t\t\t${lstLibros[i][elemento]['precio']:,}")
                    print("{:<20} {:<20} {:<20}".format(lstLibros[i][elemento]['precio'],lstLibros[i][elemento]['autor'],lstLibros[i][elemento]['titulo']))
        while True:
            continuar = int(input("\nSi desea continuar digite 1, si quiere salir presione 2: "))
            if continuar < 1 or continuar > 2:
                print("Ingrese una opción valida")
                continue
            break
        if continuar == 2:
            return
        ini +=3
        fin +=3
    return lstLibros

def guardarLibro(lstLibros , ruta): 
    
    try: 
        fd = open(ruta , "w") # Abre el archivo
    except Exception as e: 
        print("Error al abrir el archivo para guardar el libro\n" , e) 
        return None
    
    try: 
        json.dump(lstLibros, fd) # Guarda el archivo
    except Exception as e: 
        print("Error al guardar la informacion del libro\n" , e)
        return None

    fd.close() # Cierra el archivo
    return True

# funcion borrar libro
def borrarLibro(lstLibros , rutaFile):  
    print("\n\n4. Borrar libros") 

    cod = (input("Ingrese el código del libro: ")) 
    if not existeCod(cod, lstLibros):  
        print("No existe un libro con ese código") 
        input("Presione Enter para continuar")
        return

    for i in range(len(lstLibros)): #Busqueda por posición
        datos = lstLibros[i]
        k = list(datos.keys())[0]
        if k == cod: 
            del lstLibros[i] 
            break 
    
    if guardarLibro(lstLibros , rutaFile) == True: 
        print("El libro ha sido borrado con exito")
        input("Presione Enter para continuar.") 
    else: 
        print("Ocurrió un error al borrar el libro")



# función guardar libro




# funcion que analiza si el código del libro ya existe en el fichero

def existeCod(cod, lstLibros): 
    for datos in lstLibros:  
        k = str(list(datos.keys())[0]) # Devuelve la lista de las llaves pero se debe colocar el list para que la ordene correctamente en la lista
        if k == cod:
            return True 
    return False



# funcion agregar libro

def agregarLibro(lstLibros , ruta): 
    print("\n\n1. Agregar Libro") 

    cod = input("Ingrese el código del libro: ")

    while  existeCod(cod , lstLibros):  
        print("-> Ya existe un libro con ese código") 
        input("Presione Enter para continuar") 
        cod = input("\nIngrese el código: ")

    titulo = input("Título: ") 
    autor = input("Autor: ")
    precio = int(input("Precio: ")) 

    dicLibro = {}
    dicLibro[cod] = {"titulo":titulo , "autor":autor , "precio":precio} 

    lstLibros.append(dicLibro)
    burbuja_optimus(lstLibros)

    if guardarLibro(lstLibros , ruta)  == True:

        input("El libro ha sido registrado con exito,\nPresione Enter para continuar")
    
    else: 
        input("Ocurrio algun error al guardar el libro. \nPresione Enter para continuar")




# funcion menu

def menu():
    while True:
        try:
            print("*** LIBRERÍA ***".center(40))
            print("MENU".center(40))
            print("1. Ingresar libro ")
            print("2. Consultar libro ")
            print("3. Editar libro ")
            print("4. Borrar libro ")
            print("5. Listar libros por nombre ")
            print("6. Listar libros por autor ")
            print("7. Listar libros por precio ")
            print("8. Salir ")
            op = int(input(">>> Opción (1-8)? "))
            if op < 1 or op > 8:
                print("Opción no válida. Escoja de 1 a 8.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 8.")
            input("Presione cualquier tecla para continuar...")


# función para cargar archivo

def cargarInfo(lstLibros , ruta): 
    try: 
        fd = open(ruta, "r") #Fd es la apertura del archivo
    except Exception as e:  

        try: 
            fd = open(ruta , "w")  
        except Exception as d:  
            print("Error al intentar abrir el archivo\n" , d) 
            return None 
    try:
        linea = fd.readline()
        if linea.strip() != "": # Si tiene el archivo algo de contenido cargará los datos, sino creará una lista vacia.
            fd.seek(0) # Posiciona el puntero en 0
            lstLibros = json.load(fd) # json.load() --> carga el archivo
        else: 
            lstLibros = []
    except Exception as e: 
        print("Error al cargar la informacion\n" , e) 
        return None 
    
    # print(lstPersonal) # -> imprime si el archivo existe
    fd.close() #Si se carga todo cierre el archivo
    return lstLibros #Devuelve la lista cargada


# funcion mostrar libro

def consultarLibro(lstLibros): 

    print("\n\n2. Consultar libro") 
    cod = input("Ingrese el código: ") 

    if not existeCod(cod , lstLibros): 
        print("El libro no está registrado en el fichero.") 
        input("Presione Eter para continuar")
        return
    
    for i in range(len(lstLibros)):  
        datos = lstLibros[i] 
        k = list(datos.keys())[0]
        if k == cod:
            for elemento in lstLibros[i]:
                print(f"Título: {lstLibros[i][elemento]['titulo']}") 
                print(f"Autor: {lstLibros[i][elemento]['autor']}") 
                print(f"Precio: ${lstLibros[i][elemento]['precio']:,}") 
                input("\nPresione Enter para continuar.")


# programa principal
rutaFile = "Temas de Clase/Ejercicio-tipo-test-Oct17/lst-libros.json"
lstLibros = []
lstLibros = cargarInfo(lstLibros, rutaFile)

while True:

    op = menu()

    if op == 1:
        agregarLibro(lstLibros, rutaFile)
    elif op == 2:
        consultarLibro(lstLibros)  
    elif op == 3:
        modificarLibro(lstLibros,rutaFile)
    elif op == 4:
        borrarLibro(lstLibros,rutaFile)
    elif op == 5:
        listarLibrosTitulo(lstLibros)
    elif op == 6:
        listarLibrosAutor(lstLibros)
    elif op == 7:
        listarLibrosPrecio(lstLibros)
    elif op == 8:
        print("Gracias por usar el software") 
        break
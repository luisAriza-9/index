# Definir un diccionario para representar el grafo de ciudades y vías ferroviarias
grafo = {}

# Función para agregar una vía ferroviaria entre dos ciudades
def agregar_via(ciudad1, ciudad2):
    if ciudad1 in grafo:
        grafo[ciudad1].append(ciudad2)
    else:
        grafo[ciudad1] = [ciudad2]

# Leer el número de ciudades
N = int(input("Ingrese el número de ciudades: ")) 


# Leer y almacenar las ciudades y las vías ferroviarias
for _ in range(N):
    ciudad, * vias = input(f"Ingrese el nombre de la ciudad y las ciudades enlazadas, separadas por espacios: ").split()
    for via in vias:
        agregar_via(ciudad, via)
        agregar_via(via, ciudad)

# Función para verificar si hay una vía directa entre dos ciudades
def hay_via_directa(ciudad_origen, ciudad_destino):
    if ciudad_origen in grafo and ciudad_destino in grafo:
        return ciudad_destino in grafo[ciudad_origen]
    else:
        return False

# Leer pares de ciudades para verificar si hay una vía directa entre ellas
while True:
    ciudad_origen, ciudad_destino = input("Ingrese dos ciudades separadas por espacios para verificar si hay una vía directa (o escriba 'salir' para terminar): ").split()
    if ciudad_origen.lower() == "salir" or ciudad_destino.lower() == "salir":
        break
    if hay_via_directa(ciudad_origen, ciudad_destino):
        print("Hay una vía directa entre las ciudades.")
    else:
        print("No hay una vía directa entre las ciudades.")

N = int(input("Ingrese el número de ciudades: 
rpmk`pmwM`PMPMepMGPM̀EPLL,G+p,`
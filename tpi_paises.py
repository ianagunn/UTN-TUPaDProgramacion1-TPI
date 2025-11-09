import os
import csv

#Archivo CSV
nombre_archivo = "paises.csv"

#Crear archivo si no existe
def crear_archivo():
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["NOMBRE", "POBLACION", "SUPERFICIE", "CONTINENTE"])
            escritor.writeheader()
        print("Se ha creado el archivo paises.csv\n")


#Obtener lista de países desde el CSV
def obtener_paises():
    paises = []
    if not os.path.exists(nombre_archivo):
        return paises

    with open(nombre_archivo, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila["NOMBRE"] != "" and fila["POBLACION"].isdigit() and fila["SUPERFICIE"].isdigit():
                pais = {
                    "NOMBRE": fila["NOMBRE"],
                    "POBLACION": int(fila["POBLACION"]),
                    "SUPERFICIE": int(fila["SUPERFICIE"]),
                    "CONTINENTE": fila["CONTINENTE"]
                }
                paises.append(pais)
    return paises

#Guardar lista de países en el CSV
def guardar_paises(paises):
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["NOMBRE", "POBLACION", "SUPERFICIE", "CONTINENTE"])
        escritor.writeheader()
        escritor.writerows(paises)


#Agregar un nuevo país
def agregar_pais():
    print("\n----------- Agregar País -----------")
    nombre = input("Nombre: ").strip()
    poblacion = input("Población: ").strip()
    superficie = input("Superficie (km²): ").strip()
    continente = input("Continente: ").strip()

    if nombre == "" or continente == "" or not poblacion.isdigit() or not superficie.isdigit():
        print("\nDatos inválidos. Intente nuevamente.\n")
        return

    paises = obtener_paises()
    for p in paises:
        if p["NOMBRE"].lower() == nombre.lower():
            print("\nEse país ya existe.\n")
            return

    nuevo = {
        "NOMBRE": nombre,
        "POBLACION": int(poblacion),
        "SUPERFICIE": int(superficie),
        "CONTINENTE": continente
    }
    paises.append(nuevo)
    guardar_paises(paises)
    print("\nPaís agregado correctamente.\n")


#Buscar país (coincidencia parcial)
def buscar_pais():
    print("\n----------- Buscar País -----------")
    consulta = input("Ingrese el nombre o parte del nombre: ").strip().lower()
    paises = obtener_paises()
    encontrados = []
    for p in paises:
        if consulta in p["NOMBRE"].lower():
            encontrados.append(p)

    if len(encontrados) == 0:
        print("\nNo se encontraron coincidencias.\n")
    else:
        for p in encontrados:
            print(p["NOMBRE"], "- Población:", p["POBLACION"], "- Superficie:", p["SUPERFICIE"], "km² -", p["CONTINENTE"])
        print()


#Actualizar población y superficie
def actualizar_pais():
    print("\n----------- Actualizar País -----------")
    nombre = input("Ingrese el nombre exacto del país: ").strip()
    paises = obtener_paises()
    encontrado = False

    for p in paises:
        if p["NOMBRE"].lower() == nombre.lower():
            nueva_pob = input("Nueva población: ").strip()
            nueva_sup = input("Nueva superficie (km²): ").strip()
            if not nueva_pob.isdigit() or not nueva_sup.isdigit():
                print("\nDebe ingresar números válidos.\n")
                return
            p["POBLACION"] = int(nueva_pob)
            p["SUPERFICIE"] = int(nueva_sup)
            encontrado = True
            break

    if encontrado:
        guardar_paises(paises)
        print("\nPaís actualizado correctamente.\n")
    else:
        print("\nNo se encontró el país.\n")


#Filtros
def filtrar_por_continente():
    print("\n----------- Filtrar por Continente -----------")
    continente = input("Ingrese el nombre del continente: ").strip().lower()
    paises = obtener_paises()
    filtrados = []
    for p in paises:
        if p["CONTINENTE"].lower() == continente:
            filtrados.append(p)

    if len(filtrados) == 0:
        print("\nNo se encontraron países en ese continente.\n")
    else:
        for p in filtrados:
            print(p["NOMBRE"], "- Población:", p["POBLACION"])
        print()


def filtrar_por_rango_poblacion():
    print("\n----------- Filtrar por Rango de Población -----------")
    minimo = input("Población mínima: ").strip()
    maximo = input("Población máxima: ").strip()

    if not minimo.isdigit() or not maximo.isdigit():
        print("\nDebe ingresar valores numéricos.\n")
        return

    minimo = int(minimo)
    maximo = int(maximo)

    paises = obtener_paises()
    filtrados = []
    for p in paises:
        if p["POBLACION"] >= minimo and p["POBLACION"] <= maximo:
            filtrados.append(p)

    if len(filtrados) == 0:
        print("\nNo se encontraron países en ese rango.\n")
    else:
        for p in filtrados:
            print(p["NOMBRE"], "- Población:", p["POBLACION"])
        print()


def filtrar_por_rango_superficie():
    print("\n----------- Filtrar por Rango de Superficie -----------")
    minimo = input("Superficie mínima (km²): ").strip()
    maximo = input("Superficie máxima (km²): ").strip()

    if not minimo.isdigit() or not maximo.isdigit():
        print("\nDebe ingresar valores numéricos.\n")
        return

    minimo = int(minimo)
    maximo = int(maximo)

    paises = obtener_paises()
    filtrados = []
    for p in paises:
        if p["SUPERFICIE"] >= minimo and p["SUPERFICIE"] <= maximo:
            filtrados.append(p)

    if len(filtrados) == 0:
        print("\nNo se encontraron países en ese rango.\n")
    else:
        for p in filtrados:
            print(p["NOMBRE"], "- Superficie:", p["SUPERFICIE"], "km²\n")
        print()


#Ordenar países
def ordenar_paises():
    print("\n----------- Ordenar Países -----------")
    print("1 - Por nombre")
    print("2 - Por población")
    print("3 - Por superficie")
    opcion = input("Seleccione una opción: ").strip()
    orden = input("Ascendente (A) o Descendente (D): ").strip().upper()

    paises = obtener_paises()
    if len(paises) == 0:
        print("\nNo hay datos cargados.\n")
        return

    ascendente = True
    if orden == "D":
        ascendente = False

    n = len(paises)
    for i in range(n - 1):
        for j in range(n - i - 1):
            match opcion:
                case "1":  #Ordena por nombre
                    if (ascendente and paises[j]["NOMBRE"] > paises[j + 1]["NOMBRE"]) or (not ascendente and paises[j]["NOMBRE"] < paises[j + 1]["NOMBRE"]):
                        aux = paises[j]
                        paises[j] = paises[j + 1]
                        paises[j + 1] = aux

                case "2":  #Ordena por población
                    if (ascendente and paises[j]["POBLACION"] > paises[j + 1]["POBLACION"]) or (not ascendente and paises[j]["POBLACION"] < paises[j + 1]["POBLACION"]):
                        aux = paises[j]
                        paises[j] = paises[j + 1]
                        paises[j + 1] = aux

                case "3":  #Ordena por superficie
                    if (ascendente and paises[j]["SUPERFICIE"] > paises[j + 1]["SUPERFICIE"]) or (not ascendente and paises[j]["SUPERFICIE"] < paises[j + 1]["SUPERFICIE"]):
                        aux = paises[j]
                        paises[j] = paises[j + 1]
                        paises[j + 1] = aux

                case _: 
                    print("\nOpción inválida.\n")
                    return

    for p in paises:
        print(p["NOMBRE"], "- Pob:", p["POBLACION"], "- Sup:", p["SUPERFICIE"], "km² -", p["CONTINENTE"])
    print()


#Estadísticas
def estadisticas():
    print("\n----------- Estadísticas -----------")
    paises = obtener_paises()
    if len(paises) == 0:
        print("No hay datos para mostrar.\n")
        return

    mayor = paises[0]
    menor = paises[0]
    suma_poblacion = 0
    suma_superficie = 0
    continentes = {}

    for p in paises:
        suma_poblacion += p["POBLACION"]
        suma_superficie += p["SUPERFICIE"]

        if p["POBLACION"] > mayor["POBLACION"]:
            mayor = p
        if p["POBLACION"] < menor["POBLACION"]:
            menor = p

        cont = p["CONTINENTE"]
        if cont in continentes:
            continentes[cont] += 1
        else:
            continentes[cont] = 1

    promedio_pob = suma_poblacion / len(paises)
    promedio_sup = suma_superficie / len(paises)

    print("País con mayor población:", mayor["NOMBRE"],"- ", mayor["POBLACION"])
    print("País con menor población:", menor["NOMBRE"], "- ", menor["POBLACION"])
    print("Promedio de población:", int(promedio_pob))
    print("Promedio de superficie:", int(promedio_sup), "km²")
    print("\nCantidad de países por continente:")
    for c in continentes:
        print(c + ":", continentes[c])
    print()

#Submenú de filtros
def filtrar():
    print("-" * 45)
    print("1 - Filtrar por continente")
    print("2 - Filtrar por rango de población")
    print("3 - Filtrar por rango de superficie\n")
    print("-" * 45)
    opcion = input("Seleccione una opción: ").strip()

    match opcion:
        case "1":
            filtrar_por_continente()
        case "2":
            filtrar_por_rango_poblacion()
        case "3":
            filtrar_por_rango_superficie()
        case _:
            print("\nOpción inválida.\n")


#Menú principal
def menu():
    opciones = [
        "1 - Agregar país",
        "2 - Actualizar país",
        "3 - Buscar país",
        "4 - Filtrar",
        "5 - Ordenar países",
        "6 - Mostrar estadísticas",
        "7 - Salir\n"
    ]

    while True:
        print("-" * 45)
        for o in opciones:
            print(o)
        print("-" * 45)
        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                agregar_pais()
            case "2":
                actualizar_pais()
            case "3":
                buscar_pais()
            case "4":
                filtrar()
            case "5":
                ordenar_paises()
            case "6":
                estadisticas()
            case "7":
                print("Saliendo del programa...")
                break
            case _:
                print("\nOpción inválida.\n")


#Programa principal
crear_archivo()
menu()
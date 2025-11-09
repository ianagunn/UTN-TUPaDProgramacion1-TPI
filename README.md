# Descripción del proyecto:

Este programa permite gestionar información sobre distintos países, aplicando los conceptos fundamentales de listas, diccionarios, funciones, estructuras condicionales y repetitivas vistos en la materia Programación 1.

El programa utiliza un archivo CSV (paises.csv) como base de datos, y ofrece un menú en consola que permite:

-Agregar, actualizar y buscar países.

-Filtrar por continente, rango de población o superficie.

-Ordenar los registros según diferentes criterios.

-Mostrar estadísticas generales (mayor/menor población, promedios y cantidad de países por continente).

# Datos de la Universidad y la cátedra:

Universidad Tecnológica Nacional (UTN) – Facultad Regional San Nicolás

Tecnicatura Universitaria en Programación (Modalidad a Distancia)

Materia: Programación 1

Trabajo Práctico Integrador (TPI)

Año: 2025

# Integrantes:

-Ian Gunn

Datos de profesores:

Docente Titular
-Sebastian Bruselario

Docente Tutor
-Flor Gubiotti

# Estructura del proyecto:

TPI/

paises.csv                 # Archivo CSV con los datos base

tpi_paises.py              # Código fuente principal

README.md                  # Documento explicativo del proyecto

/capturas/                 # Carpeta con imágenes de ejecución

# Instrucciones de ejecución

1. Requisitos previos:

-Python 3.x instalado.

-Editor o entorno de desarrollo (VSCode).

2. Ejecución:

-Colocar el archivo paises.csv en la misma carpeta del script.

-Ejecutar el programa desde la terminal: python tpi_paises.py

-El menú mostrará las siguientes opciones:

    1 - Agregar país

    2 - Actualizar país

    3 - Buscar país

    4 - Filtrar

    5 - Ordenar países

    6 - Mostrar estadísticas

    7 - Salir

3. Notas:

Si el archivo paises.csv no existe, el sistema lo creará automáticamente.
Los campos numéricos (población y superficie) deben ser enteros positivos.

# Librerías utilizadas

os: manejo de archivos y verificación de existencia.

csv: lectura y escritura de datos estructurados en formato CSV.

# Links

Video de presentación: [enlace pendiente]

Repositorio GitHub: https://github.com/ianagunn/UTN-TUPaDProgramacion1-TPI
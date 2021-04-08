"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import time
import tracemalloc
import config as cf
import tracemalloc
import time
import model
import csv
#memory and time counters
def getTime():
 """
 devuelve el instante tiempo de procesamiento en milisegundos
 """
 return float(time.perf_counter()*1000)

def getMemory():
 """
 toma una muestra de la memoria alocada en instante de tiempo
 """
 return tracemalloc.take_snapshot()

def deltaMemory(start_memory, stop_memory):
 """
 calcula la diferencia en memoria alocada del programa entre dos 
 instantes de tiempo y devuelve el resultado en kBytes (ej.: 2100.0 kB)
 """
 memory_diff = stop_memory.compare_to(start_memory, "filename")
 delta_memory = 0.0
# suma de las diferencias en uso de memoria
 for stat in memory_diff:
  delta_memory = delta_memory + stat.size_diff
# de Byte -> kByte
 delta_memory = delta_memory/1024.0
 return delta_memory










"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de videos
def startCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.CatalNuevo()
    return catalog
def startCategIndex():
    categcatalog=model.CategIndex()
    return categcatalog
# Funciones para la carga de datos
def startData(catalog,categcatalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    tracemalloc.start()
    delta_time = -1.0
    delta_memory = -1.0
    # toma de tiempo y memoria al inicio del proceso
    start_time = getTime()
    start_memory = getMemory()

    loadCategorias(categcatalog)
    loadVideos(catalog,categcatalog)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    return delta_time, delta_memory
    
    
    stop_time = getTime()
    stop_memory = getMemory()
    # finaliza el proceso para medir memoria
    tracemalloc.stop()
    # calculando la diferencia de tiempo y memoria
    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    return delta_time, delta_memory

def loadVideos(catalog,categcatalog):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    videosfile = cf.data_dir + 'videos-small.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video,categcatalog)


def loadCategorias(categcatalog):
    """
    Carga todas las categorias del archivo y las agrega a la lista de categorias
    """
    categfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(categfile, encoding='utf-8'), delimiter='\t')
    for categ in input_file:
        #print(categ)
        model.addCateg(categcatalog, categ)


# Funciones de ordenamiento
def videoSort(catalog, size,tiposort):
    """
    Ordena los videos
    """
    return model.sortVideos(catalog, size,tiposort)

# Funciones de consulta sobre el catálogo}
def trendingVideos(catalog, pais):
    return model.masDias(catalog, pais)
# Funciones de consulta sobre el catálogo
def tendenciaCateg(catalog, categ):
    return model.vidTendenciaCateg(catalog, categ)

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
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

import config as cf
import model
import csv


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

# Funciones para la carga de datos
def startData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadVideos(catalog)
    loadCategorias(catalog)
    

def loadVideos(catalog):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    videosfile = cf.data_dir + 'videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)


def loadCategorias(catalog):
    """
    Carga todas las categorias del archivo y las agrega a la lista de categorias
    """
    categfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(categfile, encoding='utf-8'), delimiter='\t')
    for categ in input_file:
        #print(categ)
        model.addCateg(catalog, categ)


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

"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2-Videos de mayor tendencia en un país segun la categoría ")
    print("3-Video de mayor duración como tendencia  según el país")
    print("4-Video de mayor duración como tendencia según la categoría")
    print("5-Videos con mayor cantidad de likes según su tag ")
    print("0-salir")
   


def initCatalog():
    """
    Inicializa el catalogo de videos
    """
    return controller.startCatalog()

def initCategCat():

    return controller.startCategIndex()    

def loadData(catalog,categcatalog):
    """
    Carga los videos en la estructura de datos
    """
    return controller.startData(catalog,categcatalog)
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog=initCatalog()
        categcatalog=initCategCat()
        answer=loadData(catalog,categcatalog)
        print("mensaje de confirmacion")
        
       # print(lt.lastElement(catalog["videos"]))
      #  print('Videos cargados: ' + str(lt.size(catalog['videos'])))
      #  print('Categorias cargadas: ' + str(lt.size(catalog['categorias'])))
        print("Tiempo [ms]: ", answer[0], "  ||  ",
              "Memoria [kB]: ", answer[1])
        print("se cargaron "+str(categcatalog["size"])+" categorías")
        print("se cargaron "+str(lt.size(catalog["videos"]))+" videos")
    elif int(inputs[0]) == 2:
        tamaño=int(input("Indique el tamaño de la muestra a analizar"))
        #tiposort=int(input("Indique 1 para shellsort,2 para insertionsort,3 para selectionsort"))
        pais=input("Introduzca un país a analizar")
        categoriaa=input("Introduzca una categoría a analizar")
        categoriaa=" "+categoriaa
        resultado=controller.videoSortTime(catalog,pais,categoriaa,2)
        for i in range(0,tamaño):
            x=resultado[0]["elements"][i]
            print("El video "+x["title"]+"del canal "+x["channel_title"]+" publicado el "+x["publish_time"]+" siendo trending el "+x["trending_date"]+" tiene la siguiente cantidad de likes,dislikes y visitas"+x["likes"]+","+x["dislikes"]+","+x["views"])
        print("Tiempo [ms]: ", resultado[1], "  ||  ",
              "Memoria [kB]: ", resultado[2])

    elif int(inputs[0]) == 3:
      pais=input("seleccione un país a analizar")
      countryTendency=controller.trendingVideosTime(catalog,pais,2)
      print("el video mas trending de "+pais+" fue "+str(countryTendency[0][0])+" con "+str(countryTendency[0][1])+" dias.")
      print("Tiempo [ms]: ", countryTendency[1], "  ||  ",
            "Memoria [kB]: ", countryTendency[2])

    elif int(inputs[0]) == 4:
        category_name = input("Indique la categoría del video de mayor tendencia.")
        category_name=" "+category_name
        categoryTendency=controller.trendingVideosTime(catalog,category_name,6)
        print("el video mas trending de la categoría "+category_name+" fue "+str(categoryTendency[0][0])+" con "+str(categoryTendency[0][1])+" dias.")
        print("Tiempo [ms]: ", categoryTendency[1], "  ||  ",
              "Memoria [kB]: ", categoryTendency[2])

    elif int(inputs[0]) == 5:
        tamaño=int(input("Indique el tamaño de la muestra a analizar"))
        pais=input("Introduzca un país a analizar")
        tagrequest=input("Introduzca un tag a revisar")
        result2=controller.videoSortTime(catalog,pais,None,3)
        filtered=controller.tagfiltering(result2[0],tagrequest)
        for i in range(0,tamaño):
          try:  
           y=filtered["videos"]["elements"][i]
           print(y["title"]+" del canal "+y["channel_title"]+" publicado el" +y["publish_time"]+" con la siguiented cantidad  de likes,dislikes y views"+y["likes"]+","+y["dislikes"]+","+y["views"]+" posee los siguientes tags"+y["tags"])
          except:
              break
        print("Tiempo [ms]: ", result2[1], "  ||  ",
              "Memoria [kB]: ", result2[2])
        
    else:
        sys.exit(0)
sys.exit(0)

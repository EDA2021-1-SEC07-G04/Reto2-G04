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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import copy as copy
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def CatalNuevo():
 catalog={"videos":None, "categories":None,"years":None,"country":None}                         
         
 catalog["videos"]=lt.newList('ARRAY_LIST')
 catalog['categories'] = mp.newMap(400000,19,maptype='PROBING',loadfactor=0.80,comparefunction=None)
 catalog["years"]=mp.newMap(10,19,maptype="PROBING",loadfactor=0.80,comparefunction=None)
 catalog["countries"]=mp.newMap(10,19,maptype="PROBING",loadfactor=0.80,comparefunction=None)
 return catalog

def CategIndex():
 categcatalog=mp.newMap(44,19,maptype="PROBING",loadfactor=0.80,comparefunction=None)
 return categcatalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video,categcatalog):
#creo una lista vacia para meter dentro del mapa
    lt.addLast(catalog["videos"],video)
    videospercategory=lt.newList("ARRAY_LIST")
    videospercountry=lt.newList("ARRAY_LIST")
    
    #lt.addLast(catalog["videos"],video)
    #reviso si existe  la categoria en el mapa
    if mp.contains(catalog["categories"],me.getValue(mp.get(categcatalog,video["category_id"]))) == False:
        #agrego el video a la lista intermedia
     lt.addLast(videospercategory,video)
      #hago un deepcopy de la lista intermedia  para separarla de la lista original  y lo meto al mapa
      #en este punto debería quedar la categoría creada como una llave-valor donde llave es la categoría
      #y  valor es la lista copiada donde esta 1 video(el que creo la categoria)
     mp.put(catalog['categories'], me.getValue(mp.get(categcatalog,video["category_id"])), copy.deepcopy(videospercategory))
    else:
        #ya que si existe la categoría,referencio la lista creada por deepcopy y le agrego el video
     lt.addLast(me.getValue(mp.get(catalog["categories"],me.getValue(mp.get(categcatalog,video['category_id'])))),video)   
    
    if mp.contains(catalog["countries"],video["country"]) == False:
        lt.addLast(videospercountry,video)
        mp.put(catalog["countries"],video["country"],copy.deepcopy(videospercountry))
    else:
     lt.addLast(me.getValue(mp.get(catalog["countries"])),video)   
        
def addCateg(categcatalog, categ):
    """
    Adiciona una categoria a la lista de categorias
    """
   # c = newCateg(categ['name'], categ['id'])
    #lt.addLast(catalog['categorias'], c)
    mp.put(categcatalog,categ["id"],categ["name"])




# Funciones de consulta


# Funciones utilizadas para comparar elementos dentro de una lista
def cmpVideosByViews(video1, video2):
 x=None
 if (float(video1['views']) < float(video2['views'])):
  x=True
  return x 
 else:
  x=False
  return x

def cmpVideosByLikes(video1, video2):
 x=None
 if (int(video1['likes']) < int(video2['likes'])):
  x=True
  return x 
 else:
  x=False
  return x


# Funciones de ordenamiento
def sortVideos(catalog, size,checker):
    sorted_list=[]
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    if checker == 2:
     sorted_list = sa.sort(sub_list, cmpVideosByViews)
    else:
     sorted_list = sa.sort(sub_list, cmpVideosByLikes)    
             
    return  sorted_list
#contar dias

def trendingdays(catalog,categ):
    videosincateg=me.getValue(mp.get(catalog,categ))
    titlesonly=[]
    for i in range(0,lst.size(videosincateg)):
        titlesonly.append(videosincateg[i]["title"])
            
    mostrepeated=max(titlesonly,key=videosincateg.count)
    number=count(mostrepeated)
    answer=(mostrepeated,number)
    return answer
    



    


    


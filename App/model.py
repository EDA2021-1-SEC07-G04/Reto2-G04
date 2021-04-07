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
catalog={
       "videos":None,
       "categories":None,
       "years":None,
       "country":None,
      # "tags":None,                            
       }
 categcatalog=mp.newMap(30,70531,maptype="CHAINING",loadfactor=1.0,comparefunction=None)
 catalog["videos"]=lt.newList('ARRAYLIST', compareBookIds)
 catalog['categories'] = mp.newMap(50,70351,maptype='CHAINING',loadfactor=2.0,comparefunction=None)
 catalog["years"]=mp.newMap(30,70531,maptype="CHAINING",loadfactor=2.0,comparefunction=None)
    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
#creo una lista vacia para meter dentro del mapa
    lt.addLast(catalog["videos"],video)
    videospercategory=lt.newList("ARRAYLIST")
    #lt.addLast(catalog["videos"],video)
    #reviso si existe  la categoria en el mapa
    if mp.contains(catalog[categories],me.getValue(mp.get(categcatalog,video["category_id"]))) == False:
        #agrego el video a la lista intermedia
     lt.addLast(videospercategory,video)
      #hago un deepcopy de la lista intermedia  para separarla de la lista original  y lo meto al mapa
      #en este punto debería quedar la categoría creada como una llave-valor donde llave es la categoría
      #y  valor es la lista copiada donde esta 1 video(el que creo la categoria)
     mp.put(catalog['categories'], me.getValue(mp.get(categcatalog,video["category_id"])), copy.deepcopy(videospercategory))
    else:
        #ya que si existe la categoría,referencio la lista creada por deepcopy y le agrego el video
     lt.addLast(me.getValue(mp.get(catalog["categories"],categcatalog[video['category_id'])),video)   

def addCateg(catalog, categ):
    """
    Adiciona una categoria a la lista de categorias
    """
   # c = newCateg(categ['name'], categ['id'])
    #lt.addLast(catalog['categorias'], c)
    mp.put(categcatalog,categ["name"],categ["id"])



def newCateg(name, Id):
    """
    Esta estructura almancena las categorias utilizadas para los videos.
    """
    categ = {}
    categ[Id] = name
    #categ['name'] = name
    #categ['categ_id'] = id
    return categ
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

def masDias(catalog,pais):
    used=[]
    counted=[]
    videostitulos=[]
    for i in range(0,lt.size(catalog["videos"])):
     if catalog["videos"]["elements"][i]["country"] == pais:
        
              videostitulos.append(catalog["videos"]["elements"][i]["title"])
    
    for i in videostitulos:
     if i not in used:  
        used.append(i)   
        trendingdays=videostitulos.count(i)    
        counted.append(trendingdays)      
    mastrending=max(counted)
    alah=counted.index(mastrending)
    correspondent=used[alah]
    for i in range(0,lt.size(catalog["videos"])):
        if catalog["videos"]["elements"][i]["title"] == correspondent:
            titulocanal=catalog["videos"]["elements"][i]["channel_title"]
    return correspondent,mastrending,titulocanal,pais
    

def vidTendenciaCateg(catalog, categ):
    #print(catalog['categorias'])
    lista_trend = {}
    lista_dias = []
    categ_id = hallarID(catalog, categ)
    info_video = []
    for x in catalog["videos"]["elements"]:
        if x["category_id"] == categ_id:
            if x["video_id"] in lista_trend and x["video_id"] != "#NAME?":
                lista_trend[x["video_id"]] += 1
            else:
                lista_trend[x["video_id"]] = 1
    for x in lista_trend:
        lista_dias.append(lista_trend[x])
    for x in lista_trend:
        if lista_trend[x] == max(lista_dias):
            vid_id = x
    for x in catalog["videos"]["elements"]:
        if x["video_id"] == vid_id and x["title"] not in info_video:
            info_video.append(x["title"])
            info_video.append(x["channel_title"])
            info_video.append(x["category_id"])
            info_video.append(max(lista_dias))
    return info_video
    

def hallarID(catalog, categ):
    categ_id = None
    for x in catalog["categorias"]["elements"]:
        for id in x:
            if x[id] == (" "+categ):
                categ_id = id
    return categ_id
    


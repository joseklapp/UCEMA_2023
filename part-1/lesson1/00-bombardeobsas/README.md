Objetivo del juego: Tu desafío es determinar el daño que tus ataques han infligido a las diversas ciudades de Buenos Aires. Los nombres de las ciudades a las que se ha lanzado cada misil se enumeran en un listado. Cada ciudad tiene un valor asignado de daño en un diccionario, representando el impacto de cada misil lanzado a esa ciudad.


Herramientas:
Código postal
Puntaje del ataque de un misil a una ciudad
Listado del grupo con nombres de ciudades atacadas (Cada mención es un misil)


codigos_postales = {
    "6640": "Bragado",
    "6646": "Junin",
    "6620": "Chivilcoy",
    "8000": "Bahía Blanca",
    "7600": "Mar del Plata",
    "1704": "Morón",
    "1824": "Lanús",
    "1871": "Avellaneda",
    "5500": "Mendoza",
    "5000": "Córdoba",
    "9400": "Río Gallegos"
}




Puntaje_por_ciudad = {
    "1871": 80,  
    "7600": 50,  
    "1824": 70,  
    "9400": 110,  
    "5000": 100, 
    "6640": 10,  
    "1704": 60,  
    "8000": 40,  
    "5500": 90,  
    "6620": 30,  
    "6646": 20
}



Listado_de_misiles_grupo2 = ["Mar del Plata", "Junin", "Avellaneda", "Mar del Plata", "Río Gallegos", "Córdoba", "Lanús", "Río Gallegos", "Junin", "Morón", "Morón", "Avellaneda", "Córdoba", "Bragado", "Río Gallegos", "Lanús", "Mar del Plata", "Río Gallegos", "Morón", "Bragado", "Bahía Blanca", "Chivilcoy", "Avellaneda", "Córdoba", "Lanús", "Chivilcoy", "Río Gallegos", "Bragado", "Mar del Plata", "Avellaneda", "Córdoba", "Lanús", "Bragado", "Bahía Blanca", "Mendoza", "Junin", "Río Gallegos", "Avellaneda", "Lanús", "Morón", "Mendoza", "Chivilcoy", "Bragado", "Bahía Blanca", "Río Gallegos", "Avellaneda", "Chivilcoy", "Morón", "Córdoba", "Bragado", "Mendoza"]



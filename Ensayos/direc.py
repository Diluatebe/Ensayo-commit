peliculas = [
    {"titulo": "El Padrino", "director": "Francis Ford Coppola", "año": 1972, "pais": "Estados Unidos"},
    {"titulo": "Parasite", "director": "Bong Joon-ho", "año": 2019, "pais": "Corea del Sur"},
    {"titulo": "Amores Perros", "director": "Alejandro González Iñárritu", "año": 2000, "pais": "México"},
    {"titulo": "Cinema Paradiso", "director": "Giuseppe Tornatore", "año": 1988, "pais": "Italia"},
    {"titulo": "El Secreto de sus Ojos", "director": "Juan José Campanella", "año": 2009, "pais": "Argentina"},
    {"titulo": "Inception", "director": "Christopher Nolan", "año": 2010, "pais": "Estados Unidos"},
    {"titulo": "Roma", "director": "Alfonso Cuarón", "año": 2018, "pais": "México"},
    {"titulo": "La Vita è Bella", "director": "Roberto Benigni", "año": 1997, "pais": "Italia"},
    {"titulo": "Pulp Fiction", "director": "Quentin Tarantino", "año": 1994, "pais": "Estados Unidos"},
    {"titulo": "Spirited Away", "director": "Hayao Miyazaki", "año": 2001, "pais": "Japón"}
]
#print(peliculas[-1])#-1 imprime el últimoelemento de la lista}
#print([g for g in peliculas])# imprime todas en lista por los []
#print([g["titulo"] for g in peliculas ])

# print(peliculas[0].keys())
# print(peliculas[0].values())
# print(peliculas[0].items())

# peliculas.pop()
# print([g for g in peliculas])
#print([(pelicula["titulo"], pelicula["año"]) for pelicula in peliculas if pelicula["año"]>2000])

# peliculas_2000=[]
# for pelicula in peliculas:
#     if pelicula["año"]>2000:
#         peliculas_2000.append(pelicula)
# print(peliculas_2000)


def imprimir_pelicula(peli):
    # print(peli)
    texto_pelicula = f"La película {peli["titulo"]} es del año {peli["año"]}"
    print(texto_pelicula)

def generar_texto_pelicula(peli):
    # print(peli)
    texto_pelicula = f"La película {peli["titulo"]} es del año {peli["año"]}"
    return texto_pelicula

# imprimir_pelicula(peliculas[4])

# for pelicula in peliculas:
#     imprimir_pelicula(pelicula)

# for pelicula in peliculas:
#     texto = generar_texto_pelicula(pelicula)
#     print(texto)


# def sumar(x: float, y: float) -> float:
#     return x + y


# print(sumar(3, 5.2))


texto = "Diego Atehortua"
print(texto[0])
print(texto[0:4])

for c in texto:
    print(c)

print(texto.split("o")) #separa el texto por el carácter elegido (o)
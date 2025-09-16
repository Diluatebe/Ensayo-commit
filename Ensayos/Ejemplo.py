# print("hola!!!")
# def saludar():
#     print("¡Hola!")
#     a=input("salúdame  ")
#     if a=="hola":
#         print("¡Hola!")
#     else:
#         print("No me saludaste.")
# saludar()

nombre=input("Escribe tu nombre aquí: ")
def saludar(x):
    print(f"¡Hola, {x}!")
saludar(nombre)
personas = ["Luisa", "Carlos", "Ana"]
for persona in personas:
    saludar(persona)
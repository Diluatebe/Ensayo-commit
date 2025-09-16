from Ensayos.tarea import create_student, get_all_students, students, students_aprob, delete_student_by_id
from Ensayos.tarea import print_student_data, age_student,get_Student_by_id, ad_notes
from datetime import date            
##############################
##### Programa principal #####
##############################
# students = [
#   {
#     "id": 1,
#     "first_name": "Esteban",
#     "last_name": "Contreras",
#     "birthday": date(2010, 10, 17),
#     "grades": [3.5, 4, 4.5]
#   },
#   {
#     "id": 2,
#     "first_name": "Margarita",
#     "last_name": "Peña",
#     "birthday": date(1990, 4, 2),
#     "grades": [3, 2.5, 1.5]
#   },  
# ]
"""
Tarea
- Escribir funciones para agregar un estudiante, eliminar un estudiante, listar todos los estudiantes y obtener los datos de un estudiante por id
- Listar todos los estudiantes
- Crear el estudiante Diego Armando Atehortúa, con fecha de nacimiento 27/06/1979 y id 3
- Crear el estudiante Mauricio Pineda Angel, con fecha de nacimiento 28/10/1982 y id 4
- Listar de nuevo todos los estudiantes
- Eliminar al estudiante con id 2
- Listar de nuevo todos los estudiantes
- Crear una función para calcular la edad de un estudiante (tener en cuenta solo el año)
- Crear una función para agregar una nota a un estudiante
- Agregar al estudiante Diego las notas 3, 4 y 5
- Crear una función para calcular el promedio de un estudiante (promedio simple de las notas)
- Crear una función que devuelva True si un estudiante aprueba o False si reprueba (La nota mínima aprobatoria es 3)
- Crear una función para imprimir los datos de un estudiante, ejemplo: "Diego Armando Atehortúa, de 46 años, tiene una nota promedio de 4.0."
- Imprimir los datos todos los estudiantes que no aprobaron
- Reto: Crear una función para calcular la edad de un estudiante, teniendo en cuenta día, mes y año.
- Reto: Crear un menú usando while e input que permita utilizar cualquiera de las funciones anteriores
- Reto: Leer y escribir los datos de los estudiantes desde un archivo json 
"""
print("Menú para procesamiento de estudiantes")
selección=0
print(
        "Las siguientes son las opciones disponibles:\n1:Agregar un estudiante\n2:Eliminar un estudiante\n3:Listar a todos"
        "los estudiantes\n4:Obtener los datos de un estudiante\n5:Determinar la edad de un estudiante\n"
        "6:Agregar una nota a un estudiante\n7:Promedio de un estudiante\n8:Listar los estudiantes que pierden"
          )
while selección<6:
    selección=int(input("Elija su opción:"))
    if selección == 1:
      name = input("Escribe el nombre: ")
      last_name = input("Escribe el apellido: ")
      year = int(input("Escribe el año de nacimiento: "))
      month = int(input("Escribe el mes de nacimiento: "))
      day = int(input("Escribe el día de nacimiento: "))
      id = int(input("Escribe el id: "))
      birthday = date(year, month, day) 
      grades = []
      create_student(
      id, name, last_name, birthday, grades)
    elif selección == 2:
      id=int(input("Introduzca id del estudiante a eliminar:"))
      borrado=delete_student_by_id(id)
      if borrado == False:
        print (get_all_students())
   
    elif selección == 3:
      get_all_students()
    elif selección == 4:
      id=int(input("Introduzca id del estudiante del que desea conocer sus datos:"))
      get_Student_by_id(id)
    elif selección == 5:
      id=int(input("Introduzca id del estudiante de que desea conocer su edad:"))
      age_student
    elif selección == 6:
      id=int(input("Introduzca id del estudiante al que va a agregar nota:"))
      ad_notes(id, grades)
    else:
      break
      
           
      
    

# ...
# name = "Diego Armando"
# last_name = "Atehortúa"
# date = date(1979, 6, 27)
# id = 3
#create_student(id, name, last_name, birthday)
#get_all_students()
##Imprimir los datos todos los estudiantes que no aprobaron            
# id_perdedores= []
# for lose in students:     
# 	if students_aprob is False:
#     id_perdedores.append=[{}]
#       print(id_perdedores)
# delete_student_by_id(2)         
# get_all_students()         
#print_student_data(2)           
#age_student(3)
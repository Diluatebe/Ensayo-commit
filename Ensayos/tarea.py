# Imports
from datetime import date

# Lista de estudiantes vacía
students = [
  {
    "id": 1,
    "first_name": "Esteban",
    "last_name": "Contreras",
    "birthday": date(2010, 10, 17),
    "grades": [3.5, 4, 4.5]
  },
  {
    "id": 2,
    "first_name": "Margarita",
    "last_name": "Peña",
    "birthday": date(1990, 4, 2),
    "grades": [3, 2.5, 1.5]
  } 
 ]

# CRUD: Create - Read - Update - Delete
# Crear un nuevo estudiante
def create_student(
  student_id: int, student_name: str, student_last_name: str, student_birthday: date, student_grades: float):
  """Recibe el id, nombre, apellido, y fecha de nacimiento, los guarda en un diccionario y agrega el diccionario a la lista."""
  # Supongamos que estos se leyeron por input
  new_student={
    "id":student_id,
    "first_name":student_name,
    "last_name":student_last_name ,
    "birthday":student_birthday ,
    "grades": []
  }
  students.append(new_student)
  # new_student = {
  #  "id": 
  # }
  # students.append(new_student)
  # return None

# Listar todos los estudiantes
def get_all_students():
  print("LISTA DE ESTUDIANTES")
  for student in students:
    print(f"{student['id']} : {student['first_name']} {student['last_name']} ({student['birthday']})")
    

# Obtener los datos de un estudiante, por id
def get_Student_by_id(id):
  for student in students:
    if student["id"]==id:
      print(f"{student['id']} : {student['first_name']} {student['last_name']} ({student['birthday']}){student['grades']}")



# Eliminar un estudiante

def delete_student_by_id(id):
  for student in students:
    if student["id"] == id:
      print(f"¿Está seguro que desea eliminar a:{student['first_name']} {student['last_name']}?")
      selección = input("S o N: ")
      if selección.lower() == 's':
        students.remove(student)
        print(f"el estudiante {student['first_name']} {student['last_name']} fue eliminado")
        return True # Exit the function after deletion
      else:
        return False
  print(f"Estudiante con ID {id} no encontrado.")

def print_student_data(id):
  for student in students:
    if student["id"]==id:
      print(f"La fecha de nacimiento del estudiante {student['first_name']} {student['last_name']}: {student['birthday']}")
      return None
            
def age_student(id):
  for student in students:
    if student["id"] == id:
      edad= date.today().year - student['birthday'].year 
      print(f"El estudiante {student['first_name']} {student['last_name']} tiene {edad} años.")

def ad_notes(id, grades):
    for student in students:
        if student["id"] == id:
            nueva_nota = float(input(
                f"Ingrese nueva nota para estudiante {student['first_name']} {student['last_name']}: "
            ))
            student['grades'].append(nueva_nota)
            print(
                f"Las notas del estudiante {student['first_name']} {student['last_name']} son: {grades}"
            )

def students_average(id, grades):
  for promedio in students:
    if promedio[id] == id:
      average=float(sum(grades)/len(grades))
      #print(f"El estudiante {promedio['first_name']} {promedio['last_name']} tiene un promedio de notas de {average}.")
  return average
            
def students_aprob(id, average):
  for aprobacion in students:
    if aprobacion[id] == id:
      if average>=3.0:
        return True
    return False

# def info_student (id, students_average, age_student):
#   for info in students:
#     if students[id] == id:
#       print(f"El estudiante {info['first_name']} {info['last_name']}, de {age_student} tiene un promedio de notas de {average}.")
#     return None
         
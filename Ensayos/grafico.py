import matplotlib.pyplot as plt

# Datos de ejemplo
categorias = ["A", "B", "C", "D", "E"]
valores = [10, 15, 7, 20, 12]

# Crear gráfico de barras
plt.bar(categorias, valores, color="skyblue")

# Agregar título y etiquetas
plt.title("Ejemplo de gráfico de barras")
plt.xlabel("Categorías")
plt.ylabel("Valores")

# Mostrar gráfico
plt.show()
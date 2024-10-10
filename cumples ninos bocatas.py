import pandas as pd

# Lista para almacenar los datos
datos = []

# Bucle para pedir nombres y bocadillos
while True:
    nombre = input(
        "Introduce el nombre del niño (o escribe 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    bocadillo = input(f"Introduce el bocadillo de {nombre}: ")
    datos.append([nombre, bocadillo])

# Crear un DataFrame con los datos
df = pd.DataFrame(datos, columns=['Nombre', 'Bocadillo'])

# Ordenar el DataFrame por la columna 'Bocadillo'
df = df.sort_values('Bocadillo').reset_index(drop=True)

# Mostrar la tabla
print("\nTabla de niños y sus bocadillos:")
print(df)

# Contar la cantidad de cada tipo de bocadillo
conteo_bocadillos = df['Bocadillo'].value_counts()

# Mostrar el resumen de bocadillos
print("\nResumen de bocadillos:")
for bocadillo, cantidad in conteo_bocadillos.items():
    print(f"{bocadillo}: {cantidad} niños")

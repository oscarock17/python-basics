"""
Entrada de datos en Python
--------------------------
Se utiliza la función input() para obtener datos del usuario.
⚠️ Nota: Todo lo que se ingresa por teclado se guarda como cadena (str).
"""

# Ejemplo 1: Entrada básica
print("\n--- Ejemplo 1 ---")
texto = input("Ingrese un texto: ")
print(f"El texto ingresado fue: {texto}")

# Ejemplo 2: Nombre y edad
print("\n--- Ejemplo 2 ---")
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
print(f"Nombre: {nombre}, Edad: {edad}")
print(f"Tipo de nombre: {type(nombre)}")
print(f"Tipo de edad: {type(edad)}")

# Ejemplo 3: Área de un triángulo
print("\n--- Ejemplo 3 ---")
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area = base * altura / 2
print(f"El área es: {area:.2f}")

# Ejemplo 4: Conversión de segundos a horas, minutos y segundos
print("\n--- Ejemplo 4 ---")
total_segundos = int(input("Ingrese la cantidad de segundos: "))
minutos = total_segundos // 60
segundos = total_segundos % 60
horas = minutos // 60
minutos_restantes = minutos % 60
print(f"{total_segundos} segundos → {horas}h {minutos_restantes}m {segundos}s")

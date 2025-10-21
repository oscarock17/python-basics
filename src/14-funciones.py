"""
=============================================================
📘 14 - FUNCIONES EN PYTHON
=============================================================
Las funciones en Python son bloques de código reutilizables
que realizan una tarea específica. Pueden aceptar entradas 
(argumentos) y devolver un valor como resultado.

Ventajas:
- Evitan la repetición de código.
- Mejoran la legibilidad y el mantenimiento.
- Permiten dividir un programa grande en partes pequeñas.
"""

# -------------------------------------------------------------
# 🧩 1. Crear una función básica
# -------------------------------------------------------------

def saludar():
    """Imprime un saludo básico."""
    print("Hola mundo")

saludar()


# -------------------------------------------------------------
# 🧮 2. Funciones sin parámetros pero con operaciones internas
# -------------------------------------------------------------

def sumar_1_al_5():
    """Suma los números del 1 al 5 e imprime el resultado."""
    suma = 1 + 2 + 3 + 4 + 5
    print(f"La suma es: {suma}")

sumar_1_al_5()


# -------------------------------------------------------------
# 🔁 3. Funciones con retorno de valores
# -------------------------------------------------------------

def saludar2():
    """Retorna un saludo en lugar de imprimirlo."""
    return "Hola mundo"

print(saludar2())

def factorial_de_5():
    """Calcula y retorna el factorial de 5."""
    return 1 * 2 * 3 * 4 * 5

print(f"El factorial de 5 es: {factorial_de_5()}")


# -------------------------------------------------------------
# 🧱 4. Varias funciones combinadas
# -------------------------------------------------------------

def hola():
    return "hola"

def mundo():
    return "mundo"

saludo = hola() + " " + mundo()
print(saludo)


# -------------------------------------------------------------
# 🎯 5. Parámetros y argumentos
# -------------------------------------------------------------

def saludar3(nombre):
    """Recibe un nombre y muestra un saludo personalizado."""
    print(f"Hola, {nombre}!")

saludar3("Juan")


# -------------------------------------------------------------
# ➕ 6. Función con parámetros numéricos
# -------------------------------------------------------------

def sumar_2_numeros(num1, num2):
    """Retorna la suma de dos números."""
    return num1 + num2

print(f"La suma es: {sumar_2_numeros(4, 6)}")


# -------------------------------------------------------------
# 🔎 7. Función para obtener el mayor de dos valores
# -------------------------------------------------------------

def mayor_2_numeros(a, b):
    """Retorna el mayor entre dos números."""
    return a if a > b else b

print(f"El valor mayor es: {mayor_2_numeros(10, 4)}")


# -------------------------------------------------------------
# 📐 8. Calcular la hipotenusa usando varias funciones
# -------------------------------------------------------------
from math import sqrt

def potencia(num, pot):
    return num ** pot

def raiz(num):
    return sqrt(num)

def hipotenusa(a, b):
    """Calcula la hipotenusa de un triángulo rectángulo."""
    return raiz(potencia(a, 2) + potencia(b, 2))

a, b = 3, 4
print(f"La hipotenusa de un triángulo con lados {a} y {b} es {hipotenusa(a, b)}")


# -------------------------------------------------------------
# 🧾 9. Argumentos posicionales y nominales
# -------------------------------------------------------------

def construir_diccionario(nombre, edad, estatura):
    """Crea un diccionario con los datos proporcionados."""
    return {"nombre": nombre, "edad": edad, "estatura": estatura}

# Llamada con argumentos posicionales
print(construir_diccionario("José", 29, 1.74))


# -------------------------------------------------------------
# ⚙️ 10. Parámetros por defecto
# -------------------------------------------------------------

def construir_diccionario2(nombre, edad, estatura, carrera="Sin especificar"):
    """Permite omitir el parámetro 'carrera'."""
    return {
        "nombre": nombre,
        "edad": edad,
        "estatura": estatura,
        "carrera": carrera
    }

print(construir_diccionario2("José", 29, 1.74))


# -------------------------------------------------------------
# 🧮 11. Funciones como parámetros (funciones de orden superior)
# -------------------------------------------------------------

def suma(a, b): return a + b
def resta(a, b): return a - b
def multiplicacion(a, b): return a * b
def division(a, b): return a / b

def aplicar_operacion(funcion, a, b):
    """Aplica una operación (función) a dos números."""
    return funcion(a, b)

num1, num2 = 9, 2
print(f"{num1} + {num2} = {aplicar_operacion(suma, num1, num2)}")
print(f"{num1} - {num2} = {aplicar_operacion(resta, num1, num2)}")
print(f"{num1} * {num2} = {aplicar_operacion(multiplicacion, num1, num2)}")
print(f"{num1} / {num2} = {aplicar_operacion(division, num1, num2)}")


# -------------------------------------------------------------
# 📖 12. Documentación de funciones
# -------------------------------------------------------------

def factorial_de_5_v2():
    """
    Calcula el factorial del número 5.

    Returns:
        int: Resultado del factorial de 5.
    """
    return 1 * 2 * 3 * 4 * 5

print(f"El factorial de 5 es: {factorial_de_5_v2()}")
# help(factorial_de_5_v2)  # Muestra la documentación


# -------------------------------------------------------------
# 🌍 13. Ámbito de variables (local y global)
# -------------------------------------------------------------

x = 5  # Variable global

def mi_funcion():
    """Ejemplo de ámbito local y acceso a variable global."""
    x = 10  # Variable local
    print(f"Variable local x dentro de la función: {x}")
    print(f"Variable global x dentro de la función: {globals()['x']}")

print(f"Variable global x fuera de la función: {x}")
mi_funcion()


# -------------------------------------------------------------
# ⚡ 14. Funciones anónimas (lambda)
# -------------------------------------------------------------
# Sintaxis: lambda argumentos: expresión

# Ejemplo 1: Suma
suma = lambda a, b: a + b
print(suma(5, 3))

# Ejemplo 2: Cuadrados con map()
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)

# Ejemplo 3: Filtrar números pares con filter()
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

# Ejemplo 4: Ordenar tuplas con sorted()
datos = [(3, "tres"), (1, "uno"), (2, "dos")]
ordenados = sorted(datos, key=lambda x: x[1])
print(ordenados)

# Ejemplo 5: Calcular producto de una lista con reduce()
from functools import reduce
numeros = [1, 2, 3, 4]
producto = reduce(lambda x, y: x * y, numeros)
print(producto)


# -------------------------------------------------------------
# 🔁 15. Funciones recursivas
# -------------------------------------------------------------

def suma_numeros(n):
    """Suma los primeros n números de forma recursiva."""
    if n <= 1:
        return n
    return n + suma_numeros(n - 1)

print(suma_numeros(5))


def factorial(n):
    """Calcula el factorial de un número usando recursividad."""
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

print(factorial(5))


def fibonacci_n_elementos(n, resultado=[]):
    """Genera los primeros n elementos de la serie Fibonacci recursivamente."""
    if n == 0:
        return resultado
    if len(resultado) == 0:
        resultado.append(0)
    elif len(resultado) == 1:
        resultado.append(1)
    else:
        resultado.append(resultado[-1] + resultado[-2])
    return fibonacci_n_elementos(n - 1, resultado)

print(fibonacci_n_elementos(10))

"""
===========================================================
📘 MANEJO DE ERRORES EN PYTHON
===========================================================

El manejo de errores en Python se basa en el uso de estructuras que permiten
detectar, controlar y responder a errores (excepciones) durante la ejecución
de un programa.

Python utiliza principalmente los bloques:
    - try
    - except
    - else
    - finally

Estructura general:
-------------------
try:
    # Código que puede generar un error
except TipoDeError:
    # Código que se ejecuta si ocurre una excepción
else:
    # Código que se ejecuta si no ocurre ningún error
finally:
    # Código que se ejecuta siempre (ocurra o no una excepción)

===========================================================
"""

# ==========================================================
# 🔹 Ejemplo 1: Manejo básico con try-except
# ==========================================================
print("\n-- Ejemplo 1: Manejo básico con try-except --")

numerador = 10
denominador = 0

try:
    division = numerador / denominador
except Exception as e:
    print(f"Error: {e}")

# ==========================================================
# 🔹 Ejemplo 2: Uso de try-except-else
# ==========================================================
print("\n-- Ejemplo 2: Manejo con try-except-else --")

numerador = 10
denominador = 2

try:
    division = numerador / denominador
except Exception as e:
    print(f"Error: {e}")
else:
    print(f"La división es: {division}")

# ==========================================================
# 🔹 Ejemplo 3: Uso de try-except-else-finally
# ==========================================================
print("\n-- Ejemplo 3: Manejo con try-except-else-finally --")

numerador = 10
denominador = 2

try:
    division = numerador / denominador
except Exception as e:
    print(f"Error: {e}")
else:
    print(f"La división es: {division}")
finally:
    print("El programa terminó exitosamente")

# ==========================================================
# 🔹 Ejemplo 4: Lanzar excepciones manualmente con raise
# ==========================================================
print("\n-- Ejemplo 4: Lanzar una excepción con raise --")

def dividir(numerador, denominador):
    """Divide dos números y lanza una excepción si el denominador es 0."""
    if denominador == 0:
        raise ValueError("El denominador no puede ser 0")
    return numerador / denominador

try:
    resultado = dividir(10, 0)
    print(f"Resultado: {resultado}")
except Exception as e:
    print(f"Error: {e}")

# ==========================================================
# 🔹 Ejemplo 5: Obtener todas las excepciones integradas
# ==========================================================
print("\n-- Ejemplo 5: Listado de excepciones integradas en Python --")

import builtins

# Filtrar las excepciones disponibles en el módulo builtins
excepciones = [
    exc for exc in dir(builtins)
    if isinstance(getattr(builtins, exc), type)
    and issubclass(getattr(builtins, exc), BaseException)
]

print(excepciones)

# También se pueden consultar en la documentación oficial:
# https://docs.python.org/3/library/exceptions.html


# ==========================================================
# 🧮 Ejercicio 1: Calcular la raíz cuadrada de un número
# ==========================================================
# El programa pide un índice para acceder a una lista de números y
# calcula la raíz cuadrada. Se manejan errores como índices inválidos,
# valores no numéricos o tipos no compatibles.
# ==========================================================
print("\n-- Ejercicio 1: Calcular raíz cuadrada de un número --")

from math import sqrt

lista = [4, 9, 16, 25, 36, "a"]

while True:
    try:
        indice = int(input("Introduce un índice para acceder a la lista: "))
        numero = lista[indice]
        resultado = sqrt(numero)
    except IndexError:
        print("Error: Índice fuera de rango.")
    except ValueError:
        print("Error: Entrada no válida. Por favor, introduce un número entero.")
    except TypeError:
        print("Error: El elemento seleccionado no es un número válido para esta operación.")
    else:
        print(f"La raíz cuadrada del número {lista[indice]} es: {resultado}")
        break
    finally:
        print("Operación terminada.")


# ==========================================================
# 🧾 Ejercicio 2: Procesamiento de puntuaciones de estudiantes
# ==========================================================
"""
Objetivo:
---------
1. Solicitar al usuario las puntuaciones de varios estudiantes separadas por comas.
2. Convertir la entrada en una lista de enteros.
3. Calcular el promedio y encontrar la puntuación máxima.
4. Manejar errores como valores no numéricos o lista vacía.
5. Usar finally para indicar que el procesamiento terminó.
"""
# ==========================================================

def obtener_puntuaciones():
    """Solicita puntuaciones al usuario y las convierte en enteros."""
    while True:
        try:
            entrada = input("\nIntroduce las puntuaciones separadas por comas: ")
            puntuaciones = entrada.split(",")
            puntuaciones_int = [int(x) for x in puntuaciones]
            return puntuaciones_int
        except ValueError:
            print("❌ Error: asegúrate de que todas las puntuaciones sean números enteros separados por comas.")

def calcular_promedio(puntuaciones_int):
    """Devuelve el promedio de una lista de puntuaciones."""
    return sum(puntuaciones_int) / len(puntuaciones_int)

def encontrar_maximo(puntuaciones_int):
    """Encuentra la puntuación máxima en una lista."""
    maximo = puntuaciones_int[0]
    for puntuacion in puntuaciones_int:
        if puntuacion > maximo:
            maximo = puntuacion
    return maximo

def procesar_puntuaciones():
    """Gestiona el flujo de procesamiento de puntuaciones con manejo de errores."""
    try:
        puntuaciones_int = obtener_puntuaciones()
        promedio = calcular_promedio(puntuaciones_int)
        maximo = encontrar_maximo(puntuaciones_int)
    except ZeroDivisionError:
        print("\nError: la lista está vacía. No se puede calcular el promedio.")
    except Exception:
        print("\nError: se produjo un error desconocido.")
    else:
        print(f"\n✅ El promedio de las puntuaciones es: {promedio}")
        print(f"🏆 La puntuación máxima es: {maximo}")
    finally:
        print("\nProcesamiento de puntuaciones completado.")

# Ejecutar el ejercicio
procesar_puntuaciones()

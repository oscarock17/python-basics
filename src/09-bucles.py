#while
#Un bucle while es una estructura de control de flujo en programación que permite repetir un
#bloque de código mientras se cumpla una condición determinada. La condición se evalúa antes
#de cada iteración del bucle, y si la condición es verdadera, el bloque de código se ejecuta. Este
#proceso se repite hasta que la condición se evalúa como falsa.
print("--- bucle while ---")
print("--- Ejemplo 1 ---")

contador = 0
while contador < 5:
    print(f"el contador es: {contador}")
    contador += 1

print("--- Ejemplo 2 ---")
#Verificar contraseña correcta
contraseña_correcta = "python123"
intento = ""
while intento != contraseña_correcta:
    intento = input("Ingrese la contraseña: ")
    if intento != contraseña_correcta:
        print("Contraseña incorrecta, intente de nuevo")
print("Contraseña correcta!")

print("--- Ejemplo 3 ---")
#Sumar Números hasta que el Usuario Decida Detenerse
suma = 0
continuar = True
while continuar:
    numero = float(input("Ingrese un número: "))
    suma += numero
    desea_continuar = input("Desea continuar añadiendo numeros?: (si/no)")
    if desea_continuar == "no":
        continuar = False
print(f"La suma es: {suma}")

print("--- Ejemplo 4 ---")
#Simulador de Cajero Automático

saldo = 1000.0
while True:
    print("\nOpciones del cajero automático:")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir del programa")
    opcion = int(input("Ingrese la opción deseada: "))
    if opcion == 1:
        print(f"Tu saldo es: {saldo}")
    elif opcion == 2:
        deposito = float(input("Ingrese su deposito: "))
        saldo += deposito
        print(f"Has depositado {deposito} con exito")
    elif opcion == 3:
        retiro = float(input("Ingrese la cantidad a retirar: "))
        if retiro <= saldo:
            saldo -= retiro
            print(f"Has retirado {retiro} con exito")
        else:
            print("Fondos insuficientes")
    elif opcion == 4:
        print("Gracias por usar el cajero automático, adiós")
        break
    else:
        print("Opción inválida. Elija otra opción")

#la estructura while-else es una característica especial que permite ejecutar un
#bloque de código adicional cuando el bucle while finaliza de forma normal (es decir, cuando la
#condición del while se evalúa como falsa). Si el bucle while se interrumpe con una declaración
#break, el bloque else no se ejecutará.
print("--- bucle while else ---")
print("--- Ejemplo 1 ---")
numeros = [5,3,4,2,0,1]
numero_buscando = 5
encontrado = False
indice = 0
while indice < len(numeros):
    if numeros[indice] == numero_buscando:
        encontrado = True
        break
    indice += 1
else:
    print(f"{numero_buscando} no se encontró en la lista")

if encontrado:
    print(f"{numero_buscando} se encuentra en la posición {indice}")

print("--- Ejemplo 2 ---")
#Intentos limitados de Contraseña
contraseña_correcta = "python123"
max_intentos = 3
intentos = 0
while intentos < max_intentos:
    contraseña_prueba = input("Ingrese la contraseña: ")
    if contraseña_prueba == contraseña_correcta:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta")
    intentos += 1
else:
    print("Haz alcanzado la cantidad máxima de intentos. Intente de nuevo más tarde")

#Un ciclo for en Python es una estructura de control de flujo que permite iterar sobre una
#secuencia de elementos, como una lista, una tupla, un diccionario, un conjunto o una cadena
#de caracteres. En cada iteración del ciclo, se asigna el siguiente elemento de la secuencia a una
#variable temporal, y se ejecuta un bloque de código utilizando ese elemento.
print("--- bucle for ---")

print("--- Ejemplo 1 ---")
#Iterar sobre una lista de elementos
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

print("--- Ejemplo 2 ---")
#Iterar sobre un rango de números
for numero in range(3, 10):
    print(numero)

print("--- Ejemplo 3 ---")
#Ejemplo: Calcular la Suma de los Números en una Lista

numeros = [1,2,3,4,5]
suma = 0

for numero in numeros:
    suma += numero
    print(f"La suma es: {suma}")

print("--- Ejemplo 4 ---")
#Ejemplo: Imprimir los Números Pares del 1 al 10
for num in range (1, 11):
    if num % 2 == 0:
        print(f"{num} es par")

#Los bucles anidados son estructuras en las que un bucle se encuentra dentro de otro bucle.
#Esto permite realizar iteraciones múltiples y combinadas, lo cual es útil para trabajar con
#estructuras de datos multidimensionales, como matrices, o para realizar operaciones complejas
#que requieren varias capas de repetición.
print("--- Bucles anidados ---")

print("--- Ejemplo 1 ---")
#El siguiente código combina cada nombre de una lista con cada apellido de otra lista, generando
#todas las combinaciones posibles de nombres y apellidos, y luego imprime cada combinación.
nombres = ["Ana", "Luis", "Carlos"]
apellidos = ["García", "Martínez", "Rodriguez"]
for nombre in nombres:
    for apellido in apellidos:
        print(f"{nombre} {apellido}")

print("--- Ejemplo 2 ---")
#Ejercicio: Crear una Tabla de Multiplicar
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")
    print()

print("--- Ejemplo 3 ---")
#Ejercicio: Contar las Vocales en Cada Cadena de una Lista
cadenas = [
    "hola",
    "mundo",
    "python",
    "programacion"
]

indice = 0
while indice < len(cadenas):
    cadena_actual = cadenas[indice]
    conteo_vocales = 0
    for caracter in cadena_actual:
        if caracter in "aeiou":
            conteo_vocales += 1
    print(f"La cadena {cadena_actual} tiene {conteo_vocales} vocales")
    indice += 1

#La comprensión de listas permite construir nuevas listas aplicando una expresión a cada
#elemento de una secuencia (como una lista, una tupla o un rango) y opcionalmente filtrando
#elementos mediante una condición.
#la sintaxis es: [nueva_lista for elemento in secuencia if condición]
print("--- Comprensión de listas ---")

print("--- Ejemplo 1 ---")
#Crear una lista de números que son el doble de los números del 1 al 10
digitos = [2*digito for digito in range(1, 11)]
print(digitos)

print("--- Ejemplo 2 ---")
#Crear una lista de los números pares del 1 al 10
pares = [elemento for elemento in range(1, 11) if elemento % 2 == 0]
print(pares)

print("--- Ejemplo 3 ---")
#Crear una lista de las longitudes de las palabras en una lista
palabras = ["manzana", "banana", "cereza"]
longitudes = [len(palabra) for palabra in palabras]
print(longitudes)




# ------------------------------
# BUCLES EN PYTHON
# ------------------------------

# Python soporta varios tipos de bucles:
# - while
# - while ... else
# - for
# - Bucles anidados
# - Comprensión de listas

print("=== Bucles en Python ===")

# ------------------------------
# WHILE
# ------------------------------
print("\n--- Ejemplo 1: while simple ---")
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

print("\n--- Ejemplo 2: Verificar contraseña ---")
contraseña_correcta = "python123"
intento = ""
while intento != contraseña_correcta:
    intento = input("Ingrese la contraseña: ")
    if intento != contraseña_correcta:
        print("Contraseña incorrecta, intente de nuevo")
print("¡Contraseña correcta!")

# ------------------------------
# WHILE ... ELSE
# ------------------------------
print("\n--- Ejemplo 3: while ... else ---")
numeros = [5, 3, 4, 2, 0, 1]
buscar = 5
indice = 0
while indice < len(numeros):
    if numeros[indice] == buscar:
        print(f"{buscar} encontrado en índice {indice}")
        break
    indice += 1
else:
    print(f"{buscar} no está en la lista")

# ------------------------------
# FOR
# ------------------------------
print("\n--- Ejemplo 4: for sobre lista ---")
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

print("\n--- Ejemplo 5: for con range ---")
for numero in range(3, 10):
    print(numero)

print("\n--- Ejemplo 6: suma de lista ---")
numeros = [1, 2, 3, 4, 5]
suma = 0
for n in numeros:
    suma += n
print(f"Suma total = {suma}")

# ------------------------------
# BUCLES ANIDADOS
# ------------------------------
print("\n--- Ejemplo 7: bucles anidados ---")
nombres = ["Ana", "Luis", "Carlos"]
apellidos = ["García", "Martínez", "Rodríguez"]
for nombre in nombres:
    for apellido in apellidos:
        print(f"{nombre} {apellido}")

# ------------------------------
# COMPRENSIÓN DE LISTAS
# ------------------------------
print("\n--- Ejemplo 8: comprensión de listas ---")
# Duplicar números
dobles = [2 * x for x in range(1, 11)]
print(dobles)

# Pares
pares = [n for n in range(1, 11) if n % 2 == 0]
print(pares)

# Longitudes de palabras
palabras = ["manzana", "banana", "cereza"]
longitudes = [len(p) for p in palabras]
print(longitudes)

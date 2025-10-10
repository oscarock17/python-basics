"""
Salida de datos en Python
-------------------------
Métodos principales para mostrar información:
1. Concatenación con comas (,): Aquí, las variables se concatenan usando comas dentro del
print. Cada parte de la cadena y variable se trata como un argumento separado. Python
agrega automáticamente espacios entre los argumentos. Es útil para combinar diferentes
tipos de datos sin necesidad de convertir explícitamente los números a cadenas.
2. Concatenación con operador +: En este caso, se utiliza el operador + para concatenar las
cadenas. Aquí es necesario convertir explícitamente los números a cadenas utilizando
str(). No se añaden espacios automáticamente entre los elementos, lo que da un mayor
control sobre el formato, pero requiere más cuidado en la conversión y la estructura.
3. Método .format(): se puede insertar variables en una cadena usando {} como
marcadores de posición. Esto permite un formato más claro y controlado, incluyendo la
posibilidad de especificar el formato de los números, como se hace con la altura ({:.1f}).
Es más legible y flexible que la concatenación manual.
4. F-strings (más moderno y recomendado): Los F-strings son una forma moderna y concisa de
formatear cadenas en Python. Permiten insertar expresiones directamente dentro de
una cadena utilizando {}. Es el método más directo y legible, combinando lo mejor
de .format() y la flexibilidad de concatenación. También permite el formato preciso de
valores numéricos, como en la altura.
"""

nombre = "Oscar Diaz"
edad = 34
altura = 1.76
ocupacion = "Ingeniero"

# Concatenación con comas
print("\n--- Concatenación con comas ---")
print("Nombre:", nombre, ", Edad:", edad, ", Altura:", f"{altura:.1f}", ", Ocupación:", ocupacion)

# Concatenación con operador +
print("\n--- Concatenación con + ---")
print("Nombre: " + nombre + ", Edad: " + str(edad) + ", Altura: " + str(round(altura, 1)) + ", Ocupación: " + ocupacion)

# Método .format()
print("\n--- Método .format() ---")
print("Nombre: {}, Edad: {}, Altura: {:.1f}, Ocupación: {}".format(nombre, edad, altura, ocupacion))

# F-strings
print("\n--- F-strings ---")
print(f"Nombre: {nombre}, Edad: {edad}, Altura: {altura:.1f}, Ocupación: {ocupacion}")

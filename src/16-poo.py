# ============================================================
# Programación Orientada a Objetos (POO) en Python
# ============================================================
# La Programación Orientada a Objetos (POO) es un paradigma que organiza
# el código en torno a “objetos”, que son instancias de “clases”.
# Cada clase define las propiedades (atributos) y comportamientos (métodos)
# de sus objetos.
#
# Conceptos clave:
# • Clase: Molde que define los atributos y métodos de un objeto.
# • Objeto: Instancia concreta de una clase.
# • Atributos: Propiedades de un objeto.
# • Métodos: Acciones que un objeto puede realizar.
# • Encapsulamiento: Oculta los detalles internos de un objeto.
# • Herencia: Permite crear nuevas clases basadas en otras.
# • Polimorfismo: Permite que distintas clases respondan de forma diferente al mismo método.
# • Abstracción: Simplifica sistemas complejos enfocándose en lo esencial.
# ============================================================


# ------------------------------------------------------------
# Clase y objeto básico
# ------------------------------------------------------------
class Persona:
    pass

# Crear objeto
persona1 = Persona()
print(type(persona1))


# ------------------------------------------------------------
# Atributos de clase
# ------------------------------------------------------------
class Persona2:
    estudia = False  # atributo de clase


# ------------------------------------------------------------
# Constructores (__init__)
# ------------------------------------------------------------
class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

tri1 = Triangulo(2, 1)
print(tri1.base)
print(tri1.altura)


# ------------------------------------------------------------
# Encapsulación
# ------------------------------------------------------------
class Triangulo2:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

tri = Triangulo2(1, 2)
print(tri._Triangulo2__base)
print(tri._Triangulo2__altura)


# ------------------------------------------------------------
# Métodos de instancia
# ------------------------------------------------------------
class Persona3:
    def respirar(self):
        print("La persona respira")

persona1 = Persona3()
persona1.respirar()


# Ejercicio: método de instancia para calcular el área
class Triangulo3:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def area(self):
        print(f"El área es: {self.__base * self.__altura / 2}")

tri = Triangulo3(3, 4)
tri.area()


# ------------------------------------------------------------
# Métodos de clase (@classmethod)
# ------------------------------------------------------------
class Saludo:
    mensaje_bienvenida = "Hola, bienvenido a clase"

    def __init__(self, nombre):
        self.__nombre = nombre

    @classmethod
    def obtener_mensaje_bienvenida(cls):
        return cls.mensaje_bienvenida

persona = Saludo("José")
print(Saludo.obtener_mensaje_bienvenida())


# Ejercicio: Conteo de objetos creados
class Estudiante:
    conteo_estudiantes = 0

    def __init__(self, nombre):
        self.__nombre = nombre
        Estudiante.conteo_estudiantes += 1

    @classmethod
    def obtener_conteo_estudiantes(cls):
        return cls.conteo_estudiantes

Estudiante("José")
Estudiante("Fidel")
Estudiante("Yazmin")
print(Estudiante.obtener_conteo_estudiantes())


# ------------------------------------------------------------
# Métodos estáticos (@staticmethod)
# ------------------------------------------------------------
class Calculadora:
    @staticmethod
    def sumar(x, y): return x + y

    @staticmethod
    def restar(x, y): return x - y

    @staticmethod
    def multiplicar(x, y): return x * y

    @staticmethod
    def dividir(x, y): return x / y

print(Calculadora.sumar(4, 7))
print(Calculadora.dividir(10, 2))


# Ejercicio: Biblioteca con métodos estáticos
class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.__titulo = titulo
        self.__autor = autor
        self.__año_publicacion = año_publicacion

class Biblioteca:
    @staticmethod
    def agregar_libro(titulo, autor, año, libros):
        libro = Libro(titulo, autor, año)
        libros.append(libro)
        return libros

    @staticmethod
    def mostrar_libros(libros):
        for libro in libros:
            print(f"Título: {libro._Libro__titulo}, Autor: {libro._Libro__autor}, Año: {libro._Libro__año_publicacion}")

libros = []
libros = Biblioteca.agregar_libro("Cien años de soledad", "Gabriel García Márquez", 1967, libros)
libros = Biblioteca.agregar_libro("Fundación", "Isaac Asimov", 1951, libros)
Biblioteca.mostrar_libros(libros)


# ------------------------------------------------------------
# Propiedades (@property)
# ------------------------------------------------------------
class Triangulo4:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    @property
    def base(self): return self.__base

    @base.setter
    def base(self, valor):
        if valor <= 0:
            raise ValueError("La base debe ser positiva")
        self.__base = valor

    @property
    def altura(self): return self.__altura

    @altura.setter
    def altura(self, valor):
        if valor <= 0:
            raise ValueError("La altura debe ser positiva")
        self.__altura = valor

    @property
    def area(self):
        return self.base * self.altura / 2


# Ejercicio: Cuenta Bancaria con propiedades
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular
        self.__saldo = 0
        self.saldo = saldo_inicial

    @property
    def titular(self): return self.__titular

    @property
    def saldo(self): return self.__saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo < 0:
            raise ValueError("El saldo no puede ser negativo")
        self.__saldo = nuevo_saldo

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.__saldo += cantidad
        print(f"Depositado: {cantidad}, saldo actual: {self.__saldo}")

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if cantidad > self.__saldo:
            raise ValueError("Fondos insuficientes")
        self.__saldo -= cantidad
        print(f"Retirado: {cantidad}, saldo actual: {self.__saldo}")

    def mostrar_info(self):
        print(f"Titular: {self.titular}, Saldo: {self.saldo}")

cuenta = CuentaBancaria("José Ortega", 1000)
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.mostrar_info()


# ------------------------------------------------------------
# Herencia
# ------------------------------------------------------------
class Vehiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    def informacion(self):
        print(f"Marca: {self.__marca}, Modelo: {self.__modelo}")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.__puertas = puertas

    def mostrar_puertas(self):
        print(f"Número de puertas: {self.__puertas}")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.__tipo = tipo

    def mostrar_tipo(self):
        print(f"Tipo de motocicleta: {self.__tipo}")

mi_coche = Coche("Toyota", "Corolla", 4)
mi_moto = Motocicleta("Harley", "Sportster", "Cruiser")
mi_coche.informacion()
mi_moto.mostrar_tipo()


# ------------------------------------------------------------
# Polimorfismo
# ------------------------------------------------------------
class Animal:
    def hablar(self):
        raise NotImplementedError("Debe implementarse en las subclases")

class Perro(Animal):
    def hablar(self): return "Guau!"

class Gato(Animal):
    def hablar(self): return "Miau!"

def hacer_hablar(animal):
    print(animal.hablar())

hacer_hablar(Perro())
hacer_hablar(Gato())


# ------------------------------------------------------------
# Polimorfismo de operadores
# ------------------------------------------------------------
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other): return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other): return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, scalar): return Vector(self.x * scalar, self.y * scalar)
    def __repr__(self): return f"({self.x}, {self.y})"

v1, v2 = Vector(1, 2), Vector(3, 4)
print(f"{v1} + {v2} = {v1 + v2}")
print(f"{v1} - {v2} = {v1 - v2}")
print(f"{v1} * 3 = {v1 * 3}")

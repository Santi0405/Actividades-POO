## Punto 1
import tkinter as tk

def ejercicio_6_4():
    salida = []
    try:
        salida.append("Ingresando al primer try")
        cociente = 10000 / 0
        salida.append("Después de la división")
    except ZeroDivisionError:
        salida.append("División por cero")
    finally:
        salida.append("Ingresando al primer finally")

    try:
        salida.append("Ingresando al segundo try")
        objeto = None
        objeto.toString()
        salida.append("Imprimiendo objeto")
    except ZeroDivisionError:
        salida.append("División por cero")
    except Exception:
        salida.append("Ocurrió una excepción")
    finally:
        salida.append("Ingresando al segundo finally")
    return salida

def propuesto_1():
    salida = []
    try:
        texto = "Programación"
        caracter = texto[14]
        salida.append(caracter)
    except IndexError:
        salida.append("Indice de string por fuera del límite")
    return salida

def propuesto_2():
    salida = []
    try:
        numero = int("Número")
        salida.append(str(numero))
    except ValueError:
        salida.append("Excepción de formato de número")
    finally:
        salida.append("Ingresando al finally")
    return salida

def mostrar(funcion):
    texto.config(state="normal")
    texto.delete("1.0", tk.END)
    texto.insert(tk.END, "\n".join(funcion()))
    texto.config(state="disabled")

ventana = tk.Tk()
ventana.title("Excepciones")
ventana.geometry("400x320")

tk.Button(ventana, text="Ejercicio 6.4", width=25,
          command=lambda: mostrar(ejercicio_6_4)).pack(pady=3)
tk.Button(ventana, text="Propuesto 1: fuera de límite", width=25,
          command=lambda: mostrar(propuesto_1)).pack(pady=3)
tk.Button(ventana, text="Propuesto 2: formato de número", width=25,
          command=lambda: mostrar(propuesto_2)).pack(pady=3)

texto = tk.Text(ventana, height=10, width=45, state="disabled")
texto.pack(padx=10, pady=10)

ventana.mainloop()

##Punto 2
import tkinter as tk
from tkinter import ttk
 
class Vendedor:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = 0
 
    def imprimir(self):
        return (f"Nombre del vendedor = {self.nombre}\n"
                f"Apellidos del vendedor = {self.apellidos}\n"
                f"Edad del vendedor = {self.edad}")
 
    def verificar_edad(self, edad):
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        if 0 <= edad < 120:
            self.edad = edad
        else:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")
 
class Persona:
    def __init__(self, nombre, edad):
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self.nombre = nombre
        self.edad = edad
 
class SimboloNoExiste(Exception):
    pass
 
class TablaASCII:
    def __init__(self):
        self.tabla = {chr(i): i for i in range(32, 127)}
 
    def get(self, simbolo):
        if simbolo is None:
            raise ValueError("El símbolo no puede ser nulo.")
        if simbolo not in self.tabla:
            raise SimboloNoExiste("El símbolo no existe en la tabla.")
        return self.tabla[simbolo]
 
    def set(self, simbolo, numero):
        if simbolo is None or numero is None:
            raise ValueError("El símbolo y el número no pueden ser nulos.")
        self.tabla[simbolo] = numero
 
def entero(texto):
    try:
        return int(texto)
    except ValueError:
        raise ValueError("Debe ingresar un número entero.")
 
def vacio_a_none(texto):
    return None if texto == "" else texto
 
def crear_pestana(cuaderno, titulo, campos, acciones, ocultar=()):
    marco = tk.Frame(cuaderno, padx=10, pady=10)
    cuaderno.add(marco, text=titulo)
    entradas = []
    for i, campo in enumerate(campos):
        tk.Label(marco, text=campo).grid(row=i, column=0, sticky="w", pady=2)
        entrada = tk.Entry(marco, width=30, show="*" if i in ocultar else "")
        entrada.grid(row=i, column=1, pady=2)
        entradas.append(entrada)
    botones = tk.Frame(marco)
    botones.grid(row=len(campos), column=0, columnspan=2, pady=8)
    salida = tk.Text(marco, height=9, width=52)
    salida.grid(row=len(campos) + 1, column=0, columnspan=2)
 
    def ejecutar(funcion):
        try:
            resultado = funcion([e.get() for e in entradas])
        except Exception as error:
            resultado = "Error: " + str(error)
        salida.delete("1.0", tk.END)
        salida.insert(tk.END, resultado)
 
    for texto, funcion in acciones:
        tk.Button(botones, text=texto,
                  command=lambda f=funcion: ejecutar(f)).pack(side="left", padx=4)
 
tabla_ascii = TablaASCII()
 
def verificar_vendedor(c):
    vendedor = Vendedor(c[0], c[1])
    vendedor.verificar_edad(entero(c[2]))
    return vendedor.imprimir()
 
def crear_persona(c):
    try:
        persona = Persona(c[0], entero(c[1]))
        return f"Objeto creado: {persona.nombre}, {persona.edad} años"
    except ValueError as error:
        return "Excepción detectada: " + str(error)
 
def obtener_simbolo(c):
    return f"Valor = {tabla_ascii.get(vacio_a_none(c[0]))}"
 
def asignar_simbolo(c):
    valor = entero(c[1]) if c[1] != "" else None
    tabla_ascii.set(vacio_a_none(c[0]), valor)
    return "Valor asignado correctamente."
 
ventana = tk.Tk()
ventana.title("Punto 2 - Ejercicio 6.5")
cuaderno = ttk.Notebook(ventana)
cuaderno.pack(padx=5, pady=5)
crear_pestana(cuaderno, "6.5 Vendedor", ["Nombre", "Apellidos", "Edad"],
              [("Verificar", verificar_vendedor)])
crear_pestana(cuaderno, "Propuesto 1", ["Nombre", "Edad"],
              [("Crear objeto", crear_persona)])
crear_pestana(cuaderno, "Propuesto 2", ["Símbolo", "Número"],
              [("Get", obtener_simbolo), ("Set", asignar_simbolo)])
ventana.mainloop()

##Punto 3
import math
import tkinter as tk
from tkinter import ttk
 
class CalculosNumericos:
    @staticmethod
    def logaritmo_neperiano(valor):
        if valor <= 0:
            raise ArithmeticError("El valor debe ser un número positivo para calcular el logaritmo.")
        return math.log(valor)
 
    @staticmethod
    def raiz_cuadrada(valor):
        if valor < 0:
            raise ArithmeticError("El valor debe ser un número positivo para calcular la raíz cuadrada.")
        return math.sqrt(valor)
 
    @staticmethod
    def pendiente(x1, y1, x2, y2):
        if x1 == x2:
            raise ZeroDivisionError("La pendiente no está definida (recta vertical).")
        return (y2 - y1) / (x2 - x1)
 
    @staticmethod
    def punto_medio(x1, y1, x2, y2):
        return (x1 + x2) / 2, (y1 + y2) / 2
 
    @staticmethod
    def raices_cuadraticas(a, b, c):
        if a == 0:
            raise ArithmeticError("El coeficiente a no puede ser cero.")
        discriminante = b * b - 4 * a * c
        if discriminante < 0:
            raise ArithmeticError("La ecuación no tiene raíces reales.")
        raiz_d = math.sqrt(discriminante)
        return (-b + raiz_d) / (2 * a), (-b - raiz_d) / (2 * a)
 
    @staticmethod
    def convertir_base(n, base):
        if base < 2 or base > 36:
            raise ValueError("La base debe estar entre 2 y 36.")
        if n == 0:
            return "0"
        digitos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        signo = "-" if n < 0 else ""
        n = abs(n)
        resultado = ""
        while n > 0:
            resultado = digitos[n % base] + resultado
            n //= base
        return signo + resultado
 
def numero(texto):
    try:
        return float(texto.replace(",", "."))
    except ValueError:
        raise ValueError("Debe ingresar un valor numérico.")
 
def entero(texto):
    try:
        return int(texto)
    except ValueError:
        raise ValueError("Debe ingresar un número entero.")
 
def crear_pestana(cuaderno, titulo, campos, acciones, ocultar=()):
    marco = tk.Frame(cuaderno, padx=10, pady=10)
    cuaderno.add(marco, text=titulo)
    entradas = []
    for i, campo in enumerate(campos):
        tk.Label(marco, text=campo).grid(row=i, column=0, sticky="w", pady=2)
        entrada = tk.Entry(marco, width=30, show="*" if i in ocultar else "")
        entrada.grid(row=i, column=1, pady=2)
        entradas.append(entrada)
    botones = tk.Frame(marco)
    botones.grid(row=len(campos), column=0, columnspan=2, pady=8)
    salida = tk.Text(marco, height=9, width=52)
    salida.grid(row=len(campos) + 1, column=0, columnspan=2)
 
    def ejecutar(funcion):
        try:
            resultado = funcion([e.get() for e in entradas])
        except Exception as error:
            resultado = "Error: " + str(error)
        salida.delete("1.0", tk.END)
        salida.insert(tk.END, resultado)
 
    for texto, funcion in acciones:
        tk.Button(botones, text=texto,
                  command=lambda f=funcion: ejecutar(f)).pack(side="left", padx=4)
 
def calcular(c):
    valor = numero(c[0])
    lineas = []
    metodos = (("Logaritmo neperiano", CalculosNumericos.logaritmo_neperiano),
               ("Raíz cuadrada", CalculosNumericos.raiz_cuadrada))
    for nombre, metodo in metodos:
        try:
            lineas.append(f"{nombre} = {metodo(valor)}")
        except ArithmeticError as error:
            lineas.append(str(error))
    return "\n".join(lineas)
 
def pendiente(c):
    x1, y1, x2, y2 = [numero(t) for t in c]
    return f"Pendiente = {CalculosNumericos.pendiente(x1, y1, x2, y2)}"
 
def punto_medio(c):
    x1, y1, x2, y2 = [numero(t) for t in c]
    x, y = CalculosNumericos.punto_medio(x1, y1, x2, y2)
    return f"Punto medio = ({x}, {y})"
 
def cuadratica(c):
    a, b, cc = [numero(t) for t in c]
    r1, r2 = CalculosNumericos.raices_cuadraticas(a, b, cc)
    return f"x1 = {r1}\nx2 = {r2}"
 
def cambio_base(c):
    resultado = CalculosNumericos.convertir_base(entero(c[0]), entero(c[1]))
    return f"Resultado = {resultado}"
 
ventana = tk.Tk()
ventana.title("Punto 3 - Ejercicio 6.6")
cuaderno = ttk.Notebook(ventana)
cuaderno.pack(padx=5, pady=5)
puntos = ["x1", "y1", "x2", "y2"]
crear_pestana(cuaderno, "6.6 Log y raíz", ["Valor"], [("Calcular", calcular)])
crear_pestana(cuaderno, "Pendiente", puntos, [("Calcular", pendiente)])
crear_pestana(cuaderno, "Punto medio", puntos, [("Calcular", punto_medio)])
crear_pestana(cuaderno, "Cuadrática", ["a", "b", "c"], [("Calcular", cuadratica)])
crear_pestana(cuaderno, "Base b", ["Número base 10", "Base b"], [("Convertir", cambio_base)])
ventana.mainloop()

##Punto 4
import tkinter as tk
from tkinter import ttk
 
 
class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
 
 
class EquipoMaraton:
    def __init__(self, nombre, universidad, lenguaje):
        self.nombre = nombre
        self.universidad = universidad
        self.lenguaje = lenguaje
        self.programadores = []
        self.tamano = 0
 
    def esta_lleno(self):
        return self.tamano == 3
 
    def anadir(self, programador):
        if self.esta_lleno():
            raise Exception("El equipo está completo. No se pudo agregar programador.")
        self.programadores.append(programador)
        self.tamano += 1
 
    @staticmethod
    def validar_campo(campo):
        if campo.strip() == "":
            raise ValueError("El campo no puede estar vacío.")
        for caracter in campo:
            if caracter.isdigit():
                raise ValueError("El campo no puede tener dígitos.")
        if len(campo) >= 20:
            raise ValueError("La longitud debe ser inferior a 20 caracteres.")
 
 
def crear_pestana(cuaderno, titulo, campos, acciones, ocultar=()):
    marco = tk.Frame(cuaderno, padx=10, pady=10)
    cuaderno.add(marco, text=titulo)
    entradas = []
    for i, campo in enumerate(campos):
        tk.Label(marco, text=campo).grid(row=i, column=0, sticky="w", pady=2)
        entrada = tk.Entry(marco, width=30, show="*" if i in ocultar else "")
        entrada.grid(row=i, column=1, pady=2)
        entradas.append(entrada)
    botones = tk.Frame(marco)
    botones.grid(row=len(campos), column=0, columnspan=2, pady=8)
    salida = tk.Text(marco, height=9, width=52)
    salida.grid(row=len(campos) + 1, column=0, columnspan=2)
 
    def ejecutar(funcion):
        try:
            resultado = funcion([e.get() for e in entradas])
        except Exception as error:
            resultado = "Error: " + str(error)
        salida.delete("1.0", tk.END)
        salida.insert(tk.END, resultado)
 
    for texto, funcion in acciones:
        tk.Button(botones, text=texto,
                  command=lambda f=funcion: ejecutar(f)).pack(side="left", padx=4)
 
 
estado_equipo = {"equipo": None}
 
 
def crear_equipo(c):
    estado_equipo["equipo"] = EquipoMaraton(c[0], c[1], c[2])
    return f"Equipo creado: {c[0]} - {c[1]} - {c[2]}"
 
 
def anadir_programador(c):
    equipo = estado_equipo["equipo"]
    if equipo is None:
        raise Exception("Primero debe crear el equipo.")
    EquipoMaraton.validar_campo(c[3])
    EquipoMaraton.validar_campo(c[4])
    equipo.anadir(Programador(c[3], c[4]))
    lineas = [f"{p.nombre} {p.apellidos}" for p in equipo.programadores]
    return "Integrantes:\n" + "\n".join(lineas)
 
 
def validar_contrasena(c):
    clave, confirmacion = c
    if len(clave) < 8:
        raise ValueError("La contraseña debe tener mínimo 8 caracteres.")
    if " " in clave:
        raise ValueError("La contraseña no debe tener espacios en blanco.")
    if not any(x.isalpha() for x in clave):
        raise ValueError("La contraseña debe tener al menos una letra.")
    if not any(x.isupper() for x in clave):
        raise ValueError("La contraseña debe tener al menos una mayúscula.")
    if not any(x.isdigit() for x in clave):
        raise ValueError("La contraseña debe tener al menos un número.")
    if clave.isalnum():
        raise ValueError("La contraseña debe tener al menos un carácter especial.")
    if clave != confirmacion:
        raise ValueError("Las contraseñas no son iguales.")
    return "Contraseña válida."
 
 
ventana = tk.Tk()
ventana.title("Punto 4 - Ejercicio 6.7")
cuaderno = ttk.Notebook(ventana)
cuaderno.pack(padx=5, pady=5)
crear_pestana(cuaderno, "6.7 Equipo",
              ["Nombre del equipo", "Universidad", "Lenguaje",
               "Nombre integrante", "Apellidos integrante"],
              [("Crear equipo", crear_equipo), ("Añadir programador", anadir_programador)])
crear_pestana(cuaderno, "Propuesto", ["Contraseña", "Confirmar contraseña"],
              [("Validar", validar_contrasena)], ocultar=(0, 1))
ventana.mainloop()

##Punto 5
import tkinter as tk
from tkinter import ttk
 
def leer_archivo(nombre):
    try:
        with open(nombre, "rb") as archivo:
            return archivo.read().decode("utf-8")
    except OSError:
        return "No se pudo leer el archivo."
 
def crear_pestana(cuaderno, titulo, campos, acciones, ocultar=()):
    marco = tk.Frame(cuaderno, padx=10, pady=10)
    cuaderno.add(marco, text=titulo)
    entradas = []
    for i, campo in enumerate(campos):
        tk.Label(marco, text=campo).grid(row=i, column=0, sticky="w", pady=2)
        entrada = tk.Entry(marco, width=30, show="*" if i in ocultar else "")
        entrada.grid(row=i, column=1, pady=2)
        entradas.append(entrada)
    botones = tk.Frame(marco)
    botones.grid(row=len(campos), column=0, columnspan=2, pady=8)
    salida = tk.Text(marco, height=9, width=52)
    salida.grid(row=len(campos) + 1, column=0, columnspan=2)
 
    def ejecutar(funcion):
        try:
            resultado = funcion([e.get() for e in entradas])
        except Exception as error:
            resultado = "Error: " + str(error)
        salida.delete("1.0", tk.END)
        salida.insert(tk.END, resultado)
 
    for texto, funcion in acciones:
        tk.Button(botones, text=texto,
                  command=lambda f=funcion: ejecutar(f)).pack(side="left", padx=4)
 
ventana = tk.Tk()
ventana.title("Punto 5 - Ejercicio 6.8")
cuaderno = ttk.Notebook(ventana)
cuaderno.pack(padx=5, pady=5)
crear_pestana(cuaderno, "6.8 Leer", [],
              [("Leer prueba.txt", lambda c: leer_archivo("prueba.txt"))])
crear_pestana(cuaderno, "Propuesto 1", ["Nombre del archivo"],
              [("Leer", lambda c: leer_archivo(c[0]))])
crear_pestana(cuaderno, "Propuesto 2", ["Nombre del archivo"],
              [("Leer en mayúsculas", lambda c: leer_archivo(c[0]).upper())])
ventana.mainloop()
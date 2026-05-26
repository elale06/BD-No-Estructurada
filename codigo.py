import os, json
from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017")
db = cliente["empresa"]
coleccion = db["empleados"]
print("Conexión exitosa")

def limpiar_pantalla():
    os.system("cls")

def ingresar_emp():
    limpiar_pantalla()
    rut = input("Ingrese RUT: ")
    nombre = input("Ingrese nombre: ")
    apellidos = input("Ingrese apellidos: ")
    sueldo = int(input("Ingrese sueldo: "))
    estatura = float(input("Ingrese estatura: "))
    emp = {
        "rut": rut,
        "nombre": nombre,
        "apellidos": apellidos,
        "sueldo": sueldo,
        "estatura": estatura
    }
    coleccion.insert_one(emp)

def ingresar_hijo():
    rut = input("Ingrese RUT del empleado: ")
    existe = coleccion.find_one({"rut": rut})
    if existe:
        nombre_hijo = input("Ingrese nombre del hijo: ")
        edad_hijo = int(input("Ingrese edad del hijo: "))
        sexo_hijo = input("Ingrese sexo del hijo (M/F): ")
        while sexo_hijo not in ["M", "F"]:
            input("Sexo inválido. Presiona ENTER para volver a intentarlo...")
            sexo_hijo = input("Ingrese sexo del hijo (M/F): ")
        coleccion.update_one({"rut": rut}, {"$push": {"hijos": {"nombre": nombre_hijo, "edad": edad_hijo, "sexo": sexo_hijo}}})
    else:
        input("Empleado no encontrado. Presiona ENTER para volver a intentarlo...")

def mostrar_emp():
    empleados = coleccion.find()
    for emp in empleados:
        print(f"RUT: {emp['rut']}")
        print(f"Nombre: {emp['nombre']} {emp['apellidos']}")
        print(f"Sueldo: {emp['sueldo']}")
        print(f"Estatura: {emp['estatura']}")
        if "hijos" in emp:
            print("Hijos:")
            for hijo in emp["hijos"]:
                print(f"  - {hijo['nombre']} ({hijo['edad']} años, sexo: {hijo['sexo']})")
        print("-" * 20)
    input("Presiona ENTER para continuar...")

def actualizar_emp():
    rut = input("Ingrese RUT del empleado a actualizar: ")
    existe = coleccion.find_one({"rut": rut})
    if existe:
        nombre = input("Ingrese nuevo nombre: ")
        apellidos = input("Ingrese nuevos apellidos: ")
        sueldo = int(input("Ingrese nuevo sueldo: "))
        estatura = float(input("Ingrese nueva estatura: "))
        coleccion.update_one({"rut": rut}, {"$set": {"nombre": nombre, "apellidos": apellidos, "sueldo": sueldo, "estatura": estatura}})
        if "hijos" in existe:
            print("¿Desea actualizar los datos de los hijos?")
            print("1) Sí")
            print("2) No")
            opcion = int(input("Ingrese opción: "))
            if opcion == 1:
                for hijo in existe["hijos"]:
                    print(f"Actualizando datos de {hijo['nombre']} ({hijo['edad']} años)")
                    nombre_hijo = input("Ingrese nuevo nombre del hijo: ")
                    edad_hijo = int(input("Ingrese nueva edad del hijo: "))
                    sexo_hijo = input("Ingrese nuevo sexo del hijo (M/F): ")
                    while sexo_hijo not in ["M", "F"]:
                        input("Sexo inválido. Presiona ENTER para volver a intentarlo...")
                        sexo_hijo = input("Ingrese nuevo sexo del hijo (M/F): ")
                    coleccion.update_one({"rut": rut, "hijos.nombre": hijo["nombre"]}, {"$set": {"hijos.$.nombre": nombre_hijo, "hijos.$.edad": edad_hijo, "hijos.$.sexo": sexo_hijo}})
            elif opcion == 2:
                pass
            else:
                input("Opción inválida. Presiona ENTER para volver a intentarlo...")
    else:
        input("Empleado no encontrado. Presiona ENTER para volver a intentarlo...")

while True:
    limpiar_pantalla()
    print("MENU")
    print("-" * 6)
    print("1) Ingresar empleado")
    print("2) Ingresar hijo")
    print("3) Mostrar empleados")
    print("4) Actualizar datos de un empleado")
    print("9) Salir")

    opcion = int(input("Ingrese opción: "))
    if opcion == 1:
        limpiar_pantalla()
        ingresar_emp()
    elif opcion == 2:
        limpiar_pantalla()
        ingresar_hijo()
    elif opcion == 3:
        limpiar_pantalla()
        mostrar_emp()
    elif opcion == 4:
        limpiar_pantalla()
        actualizar_emp()
    elif opcion == 9:
        limpiar_pantalla()
        print("Saliendo del programa...")
        break
    else:
        limpiar_pantalla()
        input("Opción inválida. Presiona ENTER para volver a intentarlo...")

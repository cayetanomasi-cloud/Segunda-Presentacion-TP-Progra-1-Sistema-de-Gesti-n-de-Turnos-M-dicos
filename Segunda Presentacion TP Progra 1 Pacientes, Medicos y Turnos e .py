
# Segunda Presentacion TP Progra 1

import json
from datetime import datetime
import os


# FUNCIONES PACIENTES: 

def buscar_paciente(ruta_archivo_pacientes):
    """
    Objetivo: Buscar un paciente por su CUIT
    Parametros: ruta_archivo_pacientes (ruta del archivo JSON)
    Retorno: Lista de pacientes encontrados
    """

    try:

        with open(ruta_archivo_pacientes, "r") as archivo:
            Pacientes = json.load(archivo)

        CUIT = input("Ingresar CUIT del paciente: ")
        encontrado = False

        for paciente in Pacientes:

            if CUIT == paciente["CUIT"]:
                encontrado = True
                print("Paciente encontrado.")
                print(paciente)

        if encontrado == False:
            print("Paciente No existente.")
            print("Debe Ingresarlo en la Opcion 1.2... ")


    except FileNotFoundError:

        print("El archivo no existe.")
        print("Debe ingresar a la opcion 10 para crearla... ")


    except Exception as e:
        print("Error:", e)



def cargar_paciente(ruta_archivo_pacientes):
    """
    Objetivo: Cargar un nuevo paciente en Archivo Json
    Parametros: ruta_archivo_pacientes
    Retorno: Archivo Json actualizado
    """

    try:

        with open(ruta_archivo_pacientes, "r") as archivo:
            Pacientes = json.load(archivo)

        paciente = {}

        paciente["CUIT"] = input("Ingresar CUIT: ")

        paciente["Apellido"] = input("Ingresar apellido: ").capitalize()

        paciente["Nombre"] = input("Ingresar nombre del paciente: ").capitalize()

        paciente["Edad"] = int(input("Ingresar edad: "))

        Pacientes.append(paciente)

        with open(ruta_archivo_pacientes, "w") as archivo:
            json.dump(Pacientes, archivo, indent=4, ensure_ascii=False)

            print("Paciente cargado correctamente.")
    
    except ValueError:
        print("La edad se debe ingresar en numeros enteros")
        
        
    except FileNotFoundError:

        print("El archivo no existe.")
        print("Debe ingresar a la opcion 9 para crearlo...")


    except Exception as e:
        print("Error:", e)



def buscar_y_cargar_paciente(ruta_archivo_pacientes):
    """
    Objetivo: Buscar un paciente por su CUIT
    Parametros: ruta_archivo_pacientes (ruta del archivo JSON)
    Retorno: Lista de pacientes encontrados
    """

    try:

        with open(ruta_archivo_pacientes, "r") as archivo:
            Pacientes = json.load(archivo)

        print("")
        print("VERIFICAR SI PACIENTE YA EXISTE: ")
        CUIT = input("Ingresar CUIT del paciente a buscar: ")
        encontrado = False

        for paciente in Pacientes:

            if CUIT == paciente["CUIT"]:
                encontrado = True
                print("Paciente encontrado.")
                print(paciente)

        if encontrado == False:
            print("Paciente no existente.")
            print("")
            print("CARGAR PACIENTE:")
            cargar_paciente(ruta_archivo_pacientes)


    except FileNotFoundError:

        print("El archivo no existe.")
        print("Debe ingresar a la opcion 9 para crearlo... ")

    except Exception as e:
        print("Error:", e)

def buscar_y_actualizar_paciente(ruta_archivo_pacientes):
    """
    Objetivo: Buscar y actualizar un paciente.
    Parametros: ruta_archivo_pacientes (ruta del archivo JSON).
    Retorno: Lista de pacientes actualizada.
    """

    try:

        with open(ruta_archivo_pacientes, "r") as archivo:
            Pacientes = json.load(archivo)

        CUIT = input("Ingresar CUIT del paciente: ")
        encontrado = False

        for paciente in Pacientes:

            if CUIT == paciente["CUIT"]:

                encontrado = True

                print("Paciente encontrado.")

                actualizar_paciente(paciente, Pacientes, ruta_archivo_pacientes)

                break

        if encontrado == False:
            print("Paciente inexistente.")


    except FileNotFoundError:

        print("El archivo no existe.")
        print("Debe ingresar a la opción 10 para crearlo...")

    except Exception as e:
        print("Error:", e)
        
        
        
def actualizar_paciente(paciente, Pacientes, ruta_archivo_pacientes):
    """
    Objetivo: Actualizar los datos de un paciente.
    Parametros: paciente, Pacientes, ruta_archivo_pacientes.
    Retorno: Archivo JSON actualizado.
    """


    try:
        paciente["Apellido"] = input("Ingresar apellido: ").capitalize()

        paciente["Nombre"] = input("Ingresar nombre del paciente: ").capitalize()

        paciente["Edad"] = int(input("Ingresar edad: "))

        with open(ruta_archivo_pacientes, "w") as archivo:

            json.dump(Pacientes, archivo, indent=4, ensure_ascii=False)

        print("Paciente actualizado correctamente.")

    
    except Exception as e:
        print("Error:", e)
        

def buscar_y_eliminar_paciente(ruta_archivo_pacientes):
    """
    Objetivo: Buscar y eliminar un paciente.
    Parametros: ruta_archivo_pacientes (ruta del archivo JSON).
    Retorno: Ninguno.
    """

    try:

        with open(ruta_archivo_pacientes, "r") as archivo:
            Pacientes = json.load(archivo)

        CUIT = input("Ingresar CUIT del paciente: ")
        encontrado = False

        for paciente in Pacientes:

            if CUIT == paciente["CUIT"]:

                encontrado = True

                print("Paciente encontrado y eliminado.")

                Pacientes.remove(paciente)

                break

        if encontrado == True:

            with open(ruta_archivo_pacientes, "w") as archivo:

                json.dump(Pacientes, archivo, indent=4, ensure_ascii=False)

        else:
            print("Paciente inexistente.")

    except FileNotFoundError:

        print("El archivo no existe.")
        print("Debe ingresar a la opción 10 para crearlo...")

    except Exception as e:
        print("Error:", e)

def crear_estructura_datos_paciente(ruta_archivo_pacientes):

    if os.path.exists(ruta_archivo_pacientes):

        print("El archivo Pacientes.json ya existe.")

    else:

        with open(ruta_archivo_pacientes, "w") as archivo:
            json.dump([], archivo, indent=4)

        print("EL archivo Pacientes.json fue creado correctamente.")


# FUNCIONES MEDICOS: 

def buscar_medico(ruta_archivo_medicos):
    """
    Objetivo: Buscar un medico por su CUIT
    Parametros: ruta_archivo_medicos (ruta del archivo JSON)
    Retorno: Lista de medicos encontrados
    """

    try:

        with open(ruta_archivo_medicos, "r") as archivo:
            medicos = json.load(archivo)

        CUIT = input("Ingresar CUIT del medico: ")
        encontrado = False

        for medico in medicos:

            if CUIT == medico["CUIT"]:
                encontrado = True
                print("medico encontrado.")
                print(medico)

        if encontrado == False:
            print("medico inexistente.")


    except FileNotFoundError:

        print("El archivo no existe.")
        print("Debe ingresar a la opcion 10 para crearla... ")

    except Exception as e:
        print("Error:", e)

def cargar_medico(ruta_archivo_medicos):
    """
    Objetivo: Cargar un nuevo medico en Archivo Json
    Parametros: ruta_archivo_medicos
    Retorno: Archivo Json actualizado
    """

    try:

        with open(ruta_archivo_medicos, "r") as archivo:
            medicos = json.load(archivo)

        medico = {}

        medico["CUIT"] = input("Ingresar CUIT: ")

        medico["Apellido"] = input("Ingresar apellido: ").capitalize()

        medico["Nombre"] = input("Ingresar nombre del medico: ").capitalize()

        medico["Edad"] = int(input("Ingresar edad: "))

        medicos.append(medico)

        with open(ruta_archivo_medicos, "w") as archivo:
            json.dump(medicos, archivo, indent=4, ensure_ascii=False)

            print("medico cargado correctamente.")
    
    except ValueError:
        print("La edad se debe ingresar en numeros enteros")
        
        
    except FileNotFoundError:

        print("El archivo no existe.")
        print("Debe ingresar a la opcion 9 para crearlo...")

    except Exception as e:
        print("Error:", e)
        

def buscar_y_cargar_medico(ruta_archivo_medicos):
    """
    Objetivo: Buscar un medico por su CUIT
    Parametros: ruta_archivo_medicos (ruta del archivo JSON)
    Retorno: Lista de medicos encontrados
    """

    try:

        with open(ruta_archivo_medicos, "r") as archivo:
            medicos = json.load(archivo)

        print("")
        print("VERIFICAR SI medico YA EXISTE: ")
        CUIT = input("Ingresar CUIT del medico a buscar: ")
        encontrado = False

        for medico in medicos:

            if CUIT == medico["CUIT"]:
                encontrado = True
                print("medico encontrado.")
                print(medico)

        if encontrado == False:
            print("medico no existente.")
            print("")
            print("CARGAR medico:")
            cargar_medico(ruta_archivo_medicos)


    except FileNotFoundError:

        print("El archivo no existe.")
        print("Debe ingresar a la opcion 9 para crearlo... ")
    
    except Exception as e:
        print("Error:", e)

def buscar_y_actualizar_medico(ruta_archivo_medicos):
    """
    Objetivo: Buscar y actualizar un medico.
    Parametros: ruta_archivo_medicos (ruta del archivo JSON).
    Retorno: Lista de medicos actualizada.
    """

    try:

        with open(ruta_archivo_medicos, "r") as archivo:
            medicos = json.load(archivo)

        CUIT = input("Ingresar CUIT del medico: ")
        encontrado = False

        for medico in medicos:

            if CUIT == medico["CUIT"]:

                encontrado = True

                print("medico encontrado.")

                actualizar_medico(medico, medicos, ruta_archivo_medicos)

                break

        if encontrado == False:
            print("medico inexistente.")


    except FileNotFoundError:

        print("El archivo no existe.")
        print("Debe ingresar a la opción 10 para crearlo...")
    
    except Exception as e:
        print("Error:", e)


def actualizar_medico(medico, medicos, ruta_archivo_medicos):
    """
    Objetivo: Actualizar los datos de un medico.
    Parametros: medico, medicos, ruta_archivo_medicos.
    Retorno: Archivo JSON actualizado.
    """


    try:
        medico["Apellido"] = input("Ingresar apellido: ").capitalize()

        medico["Nombre"] = input("Ingresar nombre del medico: ").capitalize()

        medico["Edad"] = int(input("Ingresar edad: "))

        with open(ruta_archivo_medicos, "w") as archivo:

            json.dump(medicos, archivo, indent=4, ensure_ascii=False)

        print("medico actualizado correctamente.")

    except Exception as e:
        print("Error:", e)
        

def buscar_y_eliminar_medico(ruta_archivo_medicos):
    """
    Objetivo: Buscar y eliminar un medico.
    Parametros: ruta_archivo_medicos (ruta del archivo JSON).
    Retorno: Ninguno.
    """

    try:

        with open(ruta_archivo_medicos, "r") as archivo:
            medicos = json.load(archivo)

        CUIT = input("Ingresar CUIT del medico: ")
        encontrado = False

        for medico in medicos:

            if CUIT == medico["CUIT"]:

                encontrado = True

                print("medico encontrado y eliminado.")

                medicos.remove(medico)

                break

        if encontrado == True:

            with open(ruta_archivo_medicos, "w") as archivo:

                json.dump(medicos, archivo, indent=4, ensure_ascii=False)

        else:
            print("medico inexistente.")

    except FileNotFoundError:

        print("El archivo no existe.")
        print("Debe ingresar a la opción 10 para crearlo...")

    except Exception as e:
        print("Error:", e)
        

def crear_estructura_datos_medico(ruta_archivo_medicos):
    
    try:

        if os.path.exists(ruta_archivo_medicos):

            print("El archivo medicos.json ya existe.")

        else:

            with open(ruta_archivo_medicos, "w") as archivo:
                json.dump([], archivo, indent=4)

            print("EL archivo medicos.json fue creado correctamente.")

    except Exception as e:
        print("Error:", e)

# TURNOS 


def buscar_paciente_para_cargar_turno(ruta_archivo_pacientes, ruta_archivo_medicos, ruta_archivo_turnos):
    """
    Objetivo: Buscar un paciente por su CUIT.
    """

    try:

        with open(ruta_archivo_pacientes, "r") as archivo:
            Pacientes = json.load(archivo)

        CUIT = input("Ingresar CUIT del paciente: ")
        encontrado = False

        for paciente in Pacientes:

            if CUIT == paciente["CUIT"]:

                encontrado = True
                print("Paciente encontrado.")
                print(paciente)

                buscar_medico_para_cargar_turno( paciente, ruta_archivo_medicos, ruta_archivo_turnos)

                return paciente

        if encontrado == False:
            print("Paciente No existente.")
            print("Debe ingresarlo en la opcion 1.2.")

    except FileNotFoundError:

        print("El archivo no existe.")
        print("Debe ingresar a la opcion 10 para crearlo.")
    
    except Exception as e:
        print("Error:", e)


def buscar_medico_para_cargar_turno(paciente, ruta_archivo_medicos, ruta_archivo_turnos):
    """
    Objetivo: Buscar un medico por su CUIT.
    """

    try:

        with open(ruta_archivo_medicos, "r") as archivo:
            medicos = json.load(archivo)

        CUIT = input("Ingresar CUIT del medico: ")
        encontrado = False

        for medico in medicos:

            if CUIT == medico["CUIT"]:

                encontrado = True
                print("Medico encontrado.")
                print(medico)

                crear_registro_turno( paciente, medico, ruta_archivo_turnos)

                return paciente, medico

        if encontrado == False:
            print("Medico inexistente.")

    except FileNotFoundError:

        print("El archivo no existe.")
        print("Debe ingresar a la opcion 10 para crearlo.")
    
    except Exception as e:

        print("Error:", e)


def crear_registro_turno(paciente, medico, ruta_archivo_turnos):
    """
    Objetivo: Crear un registro de turno.
    """

    try:

        fecha_texto = input("Ingrese una fecha (AAAA-MM-DD): ")

        fecha = datetime.strptime(fecha_texto, "%Y-%m-%d").date()

        with open(ruta_archivo_turnos, "a") as archivo:

            registro = f"{medico['CUIT']};{paciente['CUIT']};{fecha}\n"

            archivo.write(registro)

        print("Archivo generado con exito.")

    except ValueError:

        print("Formato de fecha incorrecto.")

    except FileNotFoundError:

        print("No se encontro el archivo o la ruta indicada.")
        

    except Exception as e:
        print("Error:", e)


def main():
    
    try:
    
        ruta_actual = os.path.dirname(__file__)

        ruta_archivo_pacientes = os.path.join(ruta_actual, "Pacientes_3.json")

        ruta_archivo_medicos = os.path.join(ruta_actual, "medicos_3.json")
        
        ruta_archivo_turnos = os.path.join(ruta_actual, "Turnos.csv")
        
        print()
        print(" MENU PRINCIPAL ")
        print()
        print("  Opciones:")
        print("  Opcion  1: PACIENTES ")
        print("  Opcion  2: MEDICOS ")
        print("  Opcion  3: TURNOS")
        print("  Opcion -1: Salir.")
        print()

        opcion = int(input("Ingresar opcion GENERAL: "))

        while opcion != -1:

            if opcion == 1:

                print("")
                print("OPCIONES DE PACIENTES:  ")
                print(" Opcion  1: Buscar Paciente por CUIT. ")
                print(" Opcion  2: Cargar Paciente. ")
                print(" Opcion  3: Actualizar Pacientes.  ")
                print(" Opcion  4: Eliminar Pacientes. ")
                print(" Opcion  5: BUSQUEDAS. ")
                print(" Opcion  6: Crear Estructuras de Datos Pacientes. ")
                print(" Opcion -1: SALIR ")
                
                print()

                opcion_paciente = int(input("Ingresar opcion de PACIENTES: "))
                
                while opcion_paciente != -1:
                    
                    if opcion_paciente == 1:
                        buscar_paciente(ruta_archivo_pacientes)

                    elif opcion_paciente == 2:
                        buscar_y_cargar_paciente(ruta_archivo_pacientes)
                    
                    elif opcion_paciente == 3:
                         buscar_y_actualizar_paciente(ruta_archivo_pacientes)
                    
                    elif opcion_paciente == 4:
                        buscar_y_eliminar_paciente(ruta_archivo_pacientes)
                    
                    elif opcion_paciente == 5:
                        pass
                        
                    elif opcion_paciente == 6:
                        crear_estructura_datos_paciente(ruta_archivo_pacientes)

                    else:

                        print("Opcion incorrecta")
                    
                    opcion_paciente = int(input("Ingresar opcion de PACIENTES: "))
                
            elif opcion == 2:
                
                print("")
                print("OPCIONES DE MEDICOS:  ")
                print("")
                print(" Opcion 1: Buscar medico por CUIT. ")
                print(" Opcion 2: Cargar medico. ")
                print(" Opcion 3: Actualizar medicos.  ")
                print(" Opcion 4: Eliminar medicos. ")
                print(" Opcion 5: BUSQUEDAS. ")
                print(" Opcion 6: Crear estructuras de datos medicos. ")
                print(" Opcion -1: SALIR ")
                print()

                opcion_medico = int(input("Ingresar opcion de MEDICOS: "))
                
                while opcion_medico != -1:
                
                    if opcion_medico == 1:
                        buscar_medico(ruta_archivo_medicos)

                    elif opcion_medico == 2:
                        buscar_y_cargar_medico(ruta_archivo_medicos)
                    
                    elif opcion_medico == 3:
                         buscar_y_actualizar_medico(ruta_archivo_medicos)
                    
                    elif opcion_medico == 4:
                        buscar_y_eliminar_medico(ruta_archivo_medicos)
                    
                    elif opcion_medico == 5:
                        pass
                        
                    elif opcion_medico == 6:
                        crear_estructura_datos_medico(ruta_archivo_medicos)
                    
                    else:
                        print("Opcion incorrecta")

                
                    opcion_medico = int(input("Ingresar opcion de MEDICOS: "))
                
            elif opcion == 3:
                print("")
                print("OPCIONES DE TURNOS:  ")
                print("")
                print(" Opcion 1: Buscar Turno por CUIT del paciente. ")
                print(" Opcion 2: Cargar Turno. ")
                print(" Opcion 3: Actualizar Turno.  ")
                print(" Opcion 4: Eliminar Turno. ")
                print(" Opcion 5: BUSQUEDAS. ")
                print(" Opcion -1: SALIR ")
                print("")
                opcion_turno = int(input("Ingresar opcion de TURNO: "))
                while opcion_turno != -1:    
                    
                    if opcion_turno == 1:
                        pass

                    elif opcion_turno == 2:
                        buscar_paciente_para_cargar_turno(ruta_archivo_pacientes, ruta_archivo_medicos, ruta_archivo_turnos)
                    
                    elif opcion_turno == 3:
                        pass
                    
                    elif opcion_turno == 4:
                        pass
                    
                    elif opcion_turno == 5:
                        pass
                    
                    else:
                        print("Opcion incorrecta")

                
                    opcion_turno = int(input("Ingresar opcion de TURNOS: "))
                
                
            print("")
            
            opcion = int(input("Ingresar opcion GENERAL: "))
            
        
    except Exception as e:
        print("Error:", e)        

main()
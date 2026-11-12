

import json
from datetime import datetime
import os
import csv


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
            print("Debe ingresar a la opcion correspondiente para crearlo...")


    except FileNotFoundError:

        print("El archivo no existe.")
        print("Debe ingresar la opcion correspondiente crear... ")


    except Exception as e:
        print("Error:", e)


def buscar_paciente_para_cargar(ruta_archivo_pacientes):
    """
    Objetivo: Buscar un paciente por su CUIT
    Parametros: ruta_archivo_pacientes (ruta del archivo JSON)
    Retorno: Paciente encontrado
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
            cargar_paciente(CUIT, ruta_archivo_pacientes)


    except FileNotFoundError:

        print("El archivo no existe.")
        print("Debe ingresar la opcion correspondiente para crearlo... ")

    except Exception as e:
        print("Error:", e)


def cargar_paciente(CUIT, ruta_archivo_pacientes):
    """
    Objetivo: Cargar un nuevo paciente en Archivo Json
    Parametros: ruta_archivo_pacientes
    Retorno: Archivo Json actualizado
    """

    try:

        with open(ruta_archivo_pacientes, "r") as archivo:
            Pacientes = json.load(archivo)

        paciente = {}

        paciente["CUIT"] = CUIT

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
        print("Debe ingresar a la correspondiente para crearlo...")


    except Exception as e:
        print("Error:", e)




def buscar_paciente_para_actualizar(ruta_archivo_pacientes):

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
        print("Debe ingresar a la correspondiente para crearlo...")

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
        

def buscar_para_remover_paciente(ruta_archivo_pacientes):
    """
    Objetivo: Buscar y eliminar un paciente.
    Parametros: ruta_archivo_pacientes (ruta del archivo JSON).
    Retorno: Archivo JSON sin el paciente seleccionado.
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
        print("Debe ingresar a la opción correspondiente para crearlo...")

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
        print("Debe ingresar a la opcion correspondiente para crearlo...")

    except Exception as e:
        print("Error:", e)


def buscar_medico_para_cargar(ruta_archivo_medicos):
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
            cargar_medico(CUIT, ruta_archivo_medicos)


    except FileNotFoundError:

        print("El archivo no existe.")
        print("Debe ingresar a la opcion correspondiente para crearlo...")
    
    except Exception as e:
        print("Error:", e)


def cargar_medico(CUIT, ruta_archivo_medicos):
    """
    Objetivo: Cargar un nuevo medico en Archivo Json
    Parametros: ruta_archivo_medicos
    Retorno: Archivo Json actualizado
    """

    try:

        with open(ruta_archivo_medicos, "r") as archivo:
            medicos = json.load(archivo)

        medico = {}

        medico["CUIT"] = CUIT

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
        print("Debe ingresar a la opcion correspondiente para crearlo...")

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
        print("Debe ingresar a la opcion correspondiente para crearlo...")
    
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
        print("Debe ingresar a la opcion correspondiente para crearlo...")

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
        print("Debe ingresar a la opcion correspondiente para crearlo...")
    
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
        print("Debe ingresar a la opcion correspondiente para crearlo...")
    
    except Exception as e:

        print("Error:", e)

# FUNCIONES DE TURNOS


def buscar_turno(ruta_archivo_turnos):

    try:

        CUIT = input("Ingresar CUIT del paciente: ")
        encontrado = False

        with open(ruta_archivo_turnos, "r") as archivo:

            turnos = csv.reader(archivo, delimiter=";")

            for turno in turnos:

                if CUIT == turno[0]:
                    encontrado = True
                    print("Turno encontrado.")
                    print(turno)

        if encontrado == False:
            print("Turno no existente.")
            print("Debe ingresarlo a la Opcion correspondiente... ")

    except FileNotFoundError:

        print("El archivo no existe.")
        print("Debe ingresarlo a la Opcion correspondiente... ")

    except Exception as e:
        print("Error:", e)




def crear_registro_turno(paciente, medico, ruta_archivo_turnos):
    """
    Objetivo: Generar un registro de fecha y hora del turno en un archivo CSV para un paciente con un medico.
    Parametros: un paciente, un medico y el archivo CSV de Turnos.
    Retorno: Registro del turno en archivo CSV
    """

    try:

        fecha_texto = input("Ingrese una fecha (AAAA-MM-DD): ")

        fecha = datetime.strptime(fecha_texto, "%Y-%m-%d").date()

        hora_texto = input("Ingrese una hora (HH:MM): ")

        hora = datetime.strptime(hora_texto, "%H:%M").time()

        with open(ruta_archivo_turnos, "a") as archivo:

            registro = f"{paciente['CUIT']};{medico['CUIT']};{fecha};{hora}\n"

            archivo.write(registro)

        print("Turno registrado con exito.")

    except ValueError:

        print("Formato de fecha u hora incorrecto.")

    except FileNotFoundError:

        print("No se encontro el archivo o la ruta indicada.")

    except Exception as e:

        print("Error:", e)




def buscar_turno_para_atualizar(ruta_archivo_turnos):
    """
    Objetivo: Buscar un turno por el CUIT del Paciente
    Parametros: ruta_archivo_turnos (ruta del archivo CSV)
    Retorno: Turno encontrado
    """

    try:

        CUIT = input("Ingresar CUIT del paciente: ")
        encontrado = False

        with open(ruta_archivo_turnos, "r") as archivo:

            turnos = csv.reader(archivo, delimiter=";")

            for turno in turnos:

                if CUIT == turno[0]:
                    encontrado = True
                    print("Turno encontrado.")
                    print(turno)
                    break

        if encontrado == True:
            actualizar_turno(turno, ruta_archivo_turnos)
            return turno

        else:
            print("Turno no existente.")
            print("Debe ingresarlo en la Opcion correspondiente... ")

    except FileNotFoundError:

        print("El archivo no existe.")
        print("Debe ingresar a la opcion correspondiente para crearlo...")

    except Exception as e:
        print("Error:", e)


        


def actualizar_turno(turno, ruta_archivo_turnos):
    """
    Objetivo: Actualizar fecha y hora de un turno.
    Parametros: turno y ruta_archivo_turnos.
    Retorno: Archivo CSV actualizado.
    """

    try:

        fecha_texto = input("Ingrese una fecha (AAAA-MM-DD): ")

        fecha = datetime.strptime(fecha_texto, "%Y-%m-%d").date()

        hora_texto = input("Ingrese una hora (HH:MM): ")

        hora = datetime.strptime(hora_texto, "%H:%M").time()

        with open(ruta_archivo_turnos, "r") as archivo:

            lector = csv.reader(archivo, delimiter=";")
            turnos = list(lector)

        actualizado = False

        for registro in turnos:

            if registro[0] == turno[0] and registro[1] == turno[1] and registro[2] == turno[2] and registro[3] == turno[3]:

                registro[2] = str(fecha)
                registro[3] = str(hora)
                actualizado = True

                break

        if actualizado == True:

            with open(ruta_archivo_turnos, "w", newline="") as archivo:

                escritor = csv.writer(archivo, delimiter=";")
                escritor.writerows(turnos)

            print("Turno actualizado con exito.")

        else:
            print("No se encontro el turno para actualizar.")

    except ValueError:

        print("Formato de fecha u hora incorrecto.")

    except FileNotFoundError:

        print("El archivo no existe.")

    except Exception as e:

        print("Error:", e)



def buscar_turno_para_remover(ruta_archivo_turnos):
    """
    Objetivo: Buscar un turno por el CUIT del Paciente y luego eliminar.
    Parametros: ruta_archivo_turnos (ruta del archivo CSV).
    Retorno: Archivo CSV sin el turno.
    """

    try:

        with open(ruta_archivo_turnos, "r") as archivo:

            turnos = list(csv.reader(archivo, delimiter=";"))

        CUIT = input("Ingresar CUIT del paciente: ")
        encontrado = False

        for turno in turnos:

            if CUIT == turno[0]:
                encontrado = True
                print("Turno encontrado.")
                print(turno)
                turnos.remove(turno)
                break

        if encontrado == True:

            with open(ruta_archivo_turnos, "w", newline="") as archivo:

                escritor = csv.writer(archivo, delimiter=";")
                escritor.writerows(turnos)

            print("Turno eliminado correctamente.")

        else:
            print("Turno no existente.")
            print("Debe ingresar la opcion correspondiente para crearlo... ")

    except FileNotFoundError:

        print("El archivo no existe.")
        print("Debe ingresar a la opcion correspondiente para crearlo... ")

    except Exception as e:
        print("Error:", e)

    

def main():
    
    try:
    
        ruta_actual = os.path.dirname(__file__)

        ruta_archivo_pacientes = os.path.join(ruta_actual, "Pacientes.json")

        ruta_archivo_medicos = os.path.join(ruta_actual, "Medicos.json")
        
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
                print(" Opcion  5: Buscar ")
                print(" Opcion  6: Crear Estructuras de Datos Pacientes. ")
                print(" Opcion -1: SALIR ")
                
                print()

                opcion_paciente = int(input("Ingresar opcion de PACIENTES: "))
                
                while opcion_paciente != -1:
                    
                    if opcion_paciente == 1:
                        buscar_paciente(ruta_archivo_pacientes)

                    elif opcion_paciente == 2:
                        buscar_paciente_para_cargar(ruta_archivo_pacientes)
                    
                    elif opcion_paciente == 3:
                         buscar_paciente_para_actualizar(ruta_archivo_pacientes)
                    
                    elif opcion_paciente == 4:
                        buscar_para_remover_paciente(ruta_archivo_pacientes)
                    
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
                print(" Opcion 5: Buscar. ")
                print(" Opcion 6: Crear estructuras de datos medicos. ")
                print(" Opcion -1: SALIR ")
                print()

                opcion_medico = int(input("Ingresar opcion de MEDICOS: "))
                
                while opcion_medico != -1:
                
                    if opcion_medico == 1:
                        buscar_medico(ruta_archivo_medicos)

                    elif opcion_medico == 2:
                        buscar_medico_para_cargar(ruta_archivo_medicos)
                    
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
                print(" Opcion -1: SALIR ")
                print("")
                opcion_turno = int(input("Ingresar opcion de TURNO: "))
                while opcion_turno != -1:    
                    
                    if opcion_turno == 1:
                        buscar_turno(ruta_archivo_turnos)

                    elif opcion_turno == 2:
                        buscar_paciente_para_cargar_turno(ruta_archivo_pacientes, ruta_archivo_medicos, ruta_archivo_turnos)
                    
                    elif opcion_turno == 3:
                        buscar_turno_para_atualizar(ruta_archivo_turnos)
                    
                    elif opcion_turno == 4:
                        buscar_turno_para_remover(ruta_archivo_turnos)
                
                    
                    else:
                        print("Opcion incorrecta")

                
                    opcion_turno = int(input("Ingresar opcion de TURNOS: "))
                
                
            print("")
            
            opcion = int(input("Ingresar opcion GENERAL: "))
            
        
    except Exception as e:
        print("Error:", e)        


main()

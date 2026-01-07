# main.py
# Programa principal del sistema de inscripciones

from gestion_charlas import inscribir, consultar

def menu():
    while True:
        print("\n=== Sistema de Inscripciones ===")
        print("1. Inscribirse en una charla")
        print("2. Consultar inscripciones")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            inscribir()
        elif opcion == "2":
            consultar()
        elif opcion == "3":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu()

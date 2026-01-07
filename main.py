from gestion_charlas import (
    listar_charlas,
    flujo_inscripcion,
    mostrar_inscripciones
)

def mostrar_menu():
    print("\n--- Sistema de Inscripciones ---")
    print("1. Inscribirse en una charla")
    print("2. Consultar inscripciones")
    print("3. Salir")

def leer_opcion():
    opcion = input("Seleccione una opción: ").strip()
    if opcion not in {"1", "2", "3"}:
        print("Opción inválida. Intente de nuevo.")
        return leer_opcion()  # recursividad ante opción inválida
    return opcion

def main():
    print("Bienvenido al Sistema de Inscripciones")
    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == "1":
            listar_charlas()
            flujo_inscripcion()
        elif opcion == "2":
            mostrar_inscripciones()
        elif opcion == "3":
            print("Saliendo del sistema... ¡Hasta pronto!")
            break

if __name__ == "__main__":
    main()

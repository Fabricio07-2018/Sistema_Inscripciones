
from manejo_archivos import (
    cargar_charlas,
    guardar_charlas,
    guardar_inscripcion,
    cargar_inscripciones
)

def listar_charlas():
    try:
        charlas = cargar_charlas()
        print("\n--- Charlas disponibles ---")
        for idx, (tema, datos) in enumerate(charlas.items(), start=1):
            print(f"{idx}. {tema} - Cupos restantes: {datos['cupos']}")
    except Exception as e:
        print(f"Error al listar charlas: {e}")

def _leer_no_vacio(mensaje: str) -> str:
    valor = input(mensaje).strip()
    if not valor:
        print("El campo no puede estar vacío. Intente nuevamente.")
        return _leer_no_vacio(mensaje)  # recursividad en entrada vacía
    return valor

def _seleccionar_charla():
    charlas = cargar_charlas()
    temas = list(charlas.keys())
    try:
        opcion = _leer_no_vacio("Ingrese el número de la charla a inscribirse: ")
        idx = int(opcion)
        if idx < 1 or idx > len(temas):
            print("Selección inválida. Intente nuevamente.")
            return _seleccionar_charla()
        return temas[idx - 1]
    except ValueError:
        print("Debe ingresar un número válido. Intente nuevamente.")
        return _seleccionar_charla()
    except Exception as e:
        print(f"Error al seleccionar charla: {e}")
        return _seleccionar_charla()

def validar_cupos(tema_charla: str) -> bool:
    charlas = cargar_charlas()
    datos = charlas.get(tema_charla)
    if not datos:
        print("La charla seleccionada no existe.")
        return False
    if datos["cupos"] > 0:
        return True
    print("No hay cupos disponibles para esta charla.")
    return False

def inscribir_usuario(nombre: str, correo: str, tema_charla: str) -> bool:
    try:
        if not validar_cupos(tema_charla):
            return False

        # Guardar inscripción
        guardar_inscripcion(nombre, correo, tema_charla)

        # Actualizar cupos
        charlas = cargar_charlas()
        charlas[tema_charla]["cupos"] -= 1
        guardar_charlas(charlas)

        print(f"Inscripción confirmada: {nombre} ({correo}) en '{tema_charla}'.")
        return True
    except Exception as e:
        print(f"Ocurrió un error al inscribir: {e}")
        return False

def flujo_inscripcion():
    print("\n--- Registro de inscripción ---")
    nombre = _leer_no_vacio("Ingrese su nombre: ")
    correo = _leer_no_vacio("Ingrese su correo: ")

    tema = _seleccionar_charla()

    confirmada = inscribir_usuario(nombre, correo, tema)
    if not confirmada:
        print("No se pudo completar la inscripción.")
    else:
        print("¡Gracias por inscribirse!")

def mostrar_inscripciones():
    try:
        inscripciones = cargar_inscripciones()
        if not inscripciones:
            print("\nNo hay inscripciones registradas.")
            return
        print("\n--- Inscripciones registradas ---")
        for linea in inscripciones:
            print(linea.strip())
    except Exception as e:
        print(f"Error al consultar inscripciones: {e}")

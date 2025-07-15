import os
from DAO import CRUDPelicula
from DTO.Pelicula import Pelicula
from utilidades import (traducir_genero, traducir_idioma, validar_fecha,
                        validar_titulo, validar_duracion, formatear_fecha, GENEROS, IDIOMAS)

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_principal():
    print("="*40)
    print("🎬 PROYECTO CRUD PELÍCULAS - MENÚ PRINCIPAL 🎬")
    print("="*40)
    print("1. Registrar Película")
    print("2. Listar Películas")
    print("3. Modificar Película")
    print("4. Eliminar Película")
    print("5. Salir")
    print("="*40)

def mostrar_menu_listar():
    print("="*40)
    print("📋 MENÚ LISTAR PELÍCULAS 📋")
    print("="*40)
    print("1. Listar Todas")
    print("2. Buscar por ID")
    print("3. Listar Parcial")
    print("4. Volver")
    print("="*40)

def mostrar_opciones(diccionario, titulo):
    print(f"\n{titulo}:")
    for k, v in diccionario.items():
        print(f"{k}. {v}")

def ingresar_pelicula():
    limpiar_pantalla()
    print("=== Registrar Nueva Película ===")

    while True:
        titulo = input("Título: ").strip()
        if validar_titulo(titulo):
            break
        print("⚠️ Título inválido. No puede estar vacío.")

    while True:
        duracion_str = input("Duración en minutos (máx 500): ").strip()
        if duracion_str.isdigit():
            duracion = int(duracion_str)
            if validar_duracion(duracion):
                break
        print("⚠️ Duración inválida. Debe ser un número entre 1 y 500.")

    while True:
        fecha = input("Fecha de estreno (AAAA-MM-DD): ").strip()
        if validar_fecha(fecha):
            break
        print("⚠️ Fecha inválida o futura.")

    mostrar_opciones(GENEROS, "Géneros disponibles")
    while True:
        genero_str = input("Seleccione el género por número: ").strip()
        if genero_str.isdigit() and int(genero_str) in GENEROS:
            genero = int(genero_str)
            break
        print("⚠️ Género inválido.")

    mostrar_opciones(IDIOMAS, "Idiomas disponibles")
    while True:
        idioma_str = input("Seleccione el idioma por número: ").strip()
        if idioma_str.isdigit() and int(idioma_str) in IDIOMAS:
            idioma = int(idioma_str)
            break
        print("⚠️ Idioma inválido.")

    director = input("Director: ").strip() or "Desconocido"

    pelicula = Pelicula(titulo, duracion, fecha, genero, idioma, director)
    CRUDPelicula.registrar_pelicula(pelicula)
    input("Presione Enter para continuar...")

def imprimir_tabla(peliculas):
    print("="*100)
    print(f"{'ID':<4} {'Título':<25} {'Duración':<9} {'Fecha Estreno':<20} {'Género':<15} {'Idioma':<15} Director")
    print("="*100)
    for p in peliculas:
        print(f"{str(p[0]):<4} {p[1]:<25} {str(p[2]):<9} {formatear_fecha(p[3]):<20} "
              f"{traducir_genero(p[4]):<15} {traducir_idioma(p[5]):<15} {p[6]}")

def listar_peliculas():
    while True:
        limpiar_pantalla()
        mostrar_menu_listar()
        opcion = input("Seleccione opción: ").strip()
        if opcion == '1':
            peliculas = CRUDPelicula.listar_peliculas()
            limpiar_pantalla()
            if peliculas:
                imprimir_tabla(peliculas)
            else:
                print("📭 No hay películas registradas.")
            input("Presione Enter para continuar...")

        elif opcion == '2':
            id_str = input("Ingrese ID de la película a buscar: ").strip()
            if id_str.isdigit():
                pelicula = CRUDPelicula.buscar_por_id(int(id_str))
                limpiar_pantalla()
                if pelicula:
                    imprimir_tabla([pelicula])
                else:
                    print("⚠️ Película no encontrada.")
            else:
                print("⚠️ ID inválido.")
            input("Presione Enter para continuar...")

        elif opcion == '3':
            todas = CRUDPelicula.listar_peliculas()
            if not todas:
                print("📭 No hay películas registradas.")
                input("Presione Enter para continuar...")
                continue
            max_cant = len(todas)
            while True:
                cant_str = input(f"¿Cuántas películas mostrar? (1-{max_cant}): ").strip()
                if cant_str.isdigit():
                    cant = int(cant_str)
                    if 1 <= cant <= max_cant:
                        parcial = CRUDPelicula.listar_parcial(cant)
                        limpiar_pantalla()
                        imprimir_tabla(parcial)
                        break
                    else:
                        print("⚠️ Número fuera de rango.")
                else:
                    print("⚠️ Entrada inválida.")
            input("Presione Enter para continuar...")

        elif opcion == '4':
            break
        else:
            print("⚠️ Opción inválida.")
            input("Presione Enter para continuar...")

def modificar_pelicula():
    limpiar_pantalla()
    peliculas = CRUDPelicula.listar_peliculas()
    if not peliculas:
        print("📭 No hay películas para modificar.")
        input("Presione Enter para continuar...")
        return

    imprimir_tabla(peliculas)
    while True:
        id_str = input("Ingrese ID de la película a modificar: ").strip()
        if id_str.isdigit():
            id_mod = int(id_str)
            pelicula = CRUDPelicula.buscar_por_id(id_mod)
            if pelicula:
                break
            else:
                print("⚠️ Película no encontrada.")
        else:
            print("⚠️ Entrada inválida.")

    titulo = input(f"Título [{pelicula[1]}]: ").strip() or pelicula[1]

    while True:
        duracion_str = input(f"Duración [{pelicula[2]}]: ").strip()
        if duracion_str == '':
            duracion = pelicula[2]
            break
        elif duracion_str.isdigit() and validar_duracion(int(duracion_str)):
            duracion = int(duracion_str)
            break
        else:
            print("⚠️ Duración inválida.")

    while True:
        fecha = input(f"Fecha estreno [{pelicula[3]}]: ").strip()
        if fecha == '':
            fecha_val = pelicula[3]
            break
        elif validar_fecha(fecha):
            fecha_val = fecha
            break
        else:
            print("⚠️ Fecha inválida.")

    mostrar_opciones(GENEROS, "Géneros disponibles")
    while True:
        genero_str = input(f"Género [{pelicula[4]}]: ").strip()
        if genero_str == '':
            genero = pelicula[4]
            break
        elif genero_str.isdigit() and int(genero_str) in GENEROS:
            genero = int(genero_str)
            break
        else:
            print("⚠️ Género inválido.")

    mostrar_opciones(IDIOMAS, "Idiomas disponibles")
    while True:
        idioma_str = input(f"Idioma [{pelicula[5]}]: ").strip()
        if idioma_str == '':
            idioma = pelicula[5]
            break
        elif idioma_str.isdigit() and int(idioma_str) in IDIOMAS:
            idioma = int(idioma_str)
            break
        else:
            print("⚠️ Idioma inválido.")

    director = input(f"Director [{pelicula[6]}]: ").strip() or pelicula[6]

    pelicula_actualizada = Pelicula(titulo, duracion, fecha_val, genero, idioma, director)
    CRUDPelicula.actualizar_pelicula(pelicula_actualizada, id_mod)
    input("Presione Enter para continuar...")

def eliminar_pelicula():
    limpiar_pantalla()
    peliculas = CRUDPelicula.listar_peliculas()
    if not peliculas:
        print("📭 No hay películas para eliminar.")
        input("Presione Enter para continuar...")
        return

    imprimir_tabla(peliculas)
    while True:
        id_str = input("Ingrese ID de la película a eliminar: ").strip()
        if id_str.isdigit():
            id_elim = int(id_str)
            pelicula = CRUDPelicula.buscar_por_id(id_elim)
            if pelicula:
                print("\nPelícula seleccionada:")
                print(f"ID: {pelicula[0]} | Título: {pelicula[1]} | Director: {pelicula[6]}")
                confirm = input("¿Confirma eliminar esta película? (S/N): ").strip().upper()
                if confirm == 'S':
                    CRUDPelicula.borrar_pelicula(id_elim)
                else:
                    print("Operación cancelada.")
                break
            else:
                print("⚠️ Película no encontrada.")
        else:
            print("⚠️ ID inválido.")
    input("Presione Enter para continuar...")

def main():
    while True:
        limpiar_pantalla()
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1':
            ingresar_pelicula()
        elif opcion == '2':
            listar_peliculas()
        elif opcion == '3':
            modificar_pelicula()
        elif opcion == '4':
            eliminar_pelicula()
        elif opcion == '5':
            print("Gracias por usar el sistema. ¡Hasta luego! 👋")
            break
        else:
            print("⚠️ Opción inválida.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()

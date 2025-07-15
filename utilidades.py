from datetime import datetime

GENEROS = {
    1: "Terror", 2: "Ciencia Ficción", 3: "Drama", 4: "Acción", 5: "Comedia",
    6: "Romance", 7: "Suspenso", 8: "Animación", 9: "Documental", 10: "Fantasía",
    11: "Bélico", 12: "Biográfico", 13: "Musical", 14: "Histórico", 15: "Deportivo"
}

IDIOMAS = {
    1: "Español", 2: "Inglés", 3: "Portugués", 4: "Francés", 5: "Alemán",
    6: "Italiano", 7: "Japonés", 8: "Coreano", 9: "Chino", 10: "Hindi",
    11: "Ruso", 12: "Árabe", 13: "Sueco", 14: "Polaco", 15: "Tailandés"
}

def traducir_genero(codigo):
    return GENEROS.get(codigo, "Desconocido")

def traducir_idioma(codigo):
    return IDIOMAS.get(codigo, "Desconocido")

def validar_fecha(fecha_str):
    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        if fecha > datetime.now().date():
            return False
        return True
    except:
        return False

def validar_titulo(titulo):
    return len(titulo.strip()) > 0

def validar_duracion(duracion):
    if isinstance(duracion, int):
        return 0 < duracion <= 500
    return False

def formatear_fecha(fecha):
    if isinstance(fecha, str):
        try:
            fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
        except:
            return fecha
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
             "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    return f"{fecha.day} de {meses[fecha.month - 1]} de {fecha.year}"

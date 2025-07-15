from DAO.Conexion import Conexion
from DTO.Pelicula import Pelicula

host = 'localhost'
user = 'root'
password = ''
db = 'bd_peliculas'

def registrar_pelicula(pelicula: Pelicula):
    try:
        con = Conexion(host, user, password, db)
        sql = ("INSERT INTO pelicula (titulo_pelicula, duracion, fecha_de_estreno, genero, idioma, director) "
               f"VALUES ('{pelicula.titulo}', {pelicula.duracion}, '{pelicula.fecha_estreno}', "
               f"{pelicula.genero}, {pelicula.idioma}, '{pelicula.director}')")
        con.ejecutar_consulta(sql)
        con.commit()
        con.desconectar()
        print("✅ Película registrada correctamente.")
    except Exception as e:
        print(f"⚠️ Error al registrar película: {e}")

def borrar_pelicula(id_pelicula: int):
    try:
        con = Conexion(host, user, password, db)
        sql = f"DELETE FROM pelicula WHERE id_pelicula={id_pelicula}"
        con.ejecutar_consulta(sql)
        con.commit()
        con.desconectar()
        print("✅ Película eliminada correctamente.")
    except Exception as e:
        print(f"⚠️ Error al eliminar película: {e}")

def actualizar_pelicula(pelicula: Pelicula, id_pelicula: int):
    try:
        con = Conexion(host, user, password, db)
        sql = ("UPDATE pelicula SET "
               f"titulo_pelicula='{pelicula.titulo}', duracion={pelicula.duracion}, "
               f"fecha_de_estreno='{pelicula.fecha_estreno}', genero={pelicula.genero}, "
               f"idioma={pelicula.idioma}, director='{pelicula.director}' "
               f"WHERE id_pelicula={id_pelicula}")
        con.ejecutar_consulta(sql)
        con.commit()
        con.desconectar()
        print("✅ Película actualizada correctamente.")
    except Exception as e:
        print(f"⚠️ Error al actualizar película: {e}")

def listar_peliculas():
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT * FROM pelicula"
        cursor = con.ejecutar_consulta(sql)
        datos = cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as e:
        print(f"⚠️ Error al listar películas: {e}")
        return []

def buscar_por_id(id_pelicula: int):
    try:
        con = Conexion(host, user, password, db)
        sql = f"SELECT * FROM pelicula WHERE id_pelicula={id_pelicula}"
        cursor = con.ejecutar_consulta(sql)
        dato = cursor.fetchone()
        con.desconectar()
        return dato
    except Exception as e:
        print(f"⚠️ Error al buscar película por ID: {e}")
        return None

def listar_parcial(cantidad: int):
    try:
        con = Conexion(host, user, password, db)
        sql = f"SELECT * FROM pelicula LIMIT {cantidad}"
        cursor = con.ejecutar_consulta(sql)
        datos = cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as e:
        print(f"⚠️ Error al listar películas parciales: {e}")
        return []

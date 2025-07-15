# MBravo_Proyecto_Peliculas_EV4

# 🎬 Proyecto CRUD de Películas

Este proyecto consiste en una aplicación de consola desarrollada en Python que permite **gestionar un registro de películas** conectándose a una base de datos MySQL. A través de un menú interactivo, el usuario puede **agregar, modificar, eliminar y consultar** películas registradas.

---

## ⚙️ Tecnologías utilizadas

- Python 3.x (3.13 fue utilizado)
- MySQL (WampServer fue utilizado)
- Biblioteca: `pymysql` para la conexión con la base de datos

---

## 🧱 Estructura del proyecto

```
Proyecto_Peliculas/
│
├── DAO/
│   ├── Conexion.py           # Para la conexión a la base de datos
│   └── CRUDPelicula.py       # Operaciones CRUD para películas
│
├── DTO/
│   └── Pelicula.py           # Modelo de datos (DTO)
│
├── main.py                   # Archivo principal con menú e interacción
├── utilidades.py             # Funciones auxiliares comunes
└── README.md                 
```

---

## 🗃️ Estructura de la base de datos
Usar lo siguiente para crear la base de datos:
```sql

CREATE DATABASE IF NOT EXISTS bd_peliculas CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci;
USE bd_peliculas;

CREATE TABLE IF NOT EXISTS pelicula (
    id_pelicula INT AUTO_INCREMENT PRIMARY KEY,
    titulo_pelicula VARCHAR(45) NOT NULL,
    duracion INT NOT NULL,
    fecha_de_estreno DATE NOT NULL,
    genero INT NOT NULL,
    idioma INT NOT NULL,
    director VARCHAR(45) NOT NULL
);
```
🎡 Funcionamiento principal

Agregar una película

Listar todas las películas registradas

Buscar una película por ID

Mostrar una cantidad limitada de películas

Modificar datos de una película existente (con posibilidad de conservar valores originales)

Eliminar películas con confirmación

🚀 Ejecución

Asegúrate de que el servidor MySQL esté activo.

Ejecuta el archivo main.py desde consola:

python main.py

Usa el menú para gestionar las películas desde la terminal.

ℹ️ Notas importantes

La conexión está configurada para host localhost y puerto 3308. Si tu puerto MySQL es distinto, ajusta el valor en Conexion.py.

El sistema ha sido probado en Windows con WampServer, pero es compatible con cualquier sistema que soporte Python y MySQL.

Se implementó el módulo utilidades.py para organizar funciones reutilizables como:

Validación de fechas

Traducción de códigos de género e idioma

Limpieza de pantalla

Formato de fechas para mejor legibilidad

Las validaciones aseguran que el usuario no ingrese fechas o números incorrectos.

El sistema incluye confirmación antes de eliminar registros para evitar eliminaciones accidentales.

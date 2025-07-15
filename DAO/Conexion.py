import pymysql

class Conexion:
    def __init__(self, host, user, password, db):
        self.db = pymysql.connect(
            host=host,
            port=3308,
            user=user,
            password=password,
            db=db
        )
        self.cursor = self.db.cursor()

    def ejecutar_consulta(self, sql):
        self.cursor.execute(sql)
        return self.cursor

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()

    def desconectar(self):
        self.db.close()

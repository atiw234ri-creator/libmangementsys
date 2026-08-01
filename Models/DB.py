from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
import os

class DB(object):
    host = os.getenv("MYSQL_HOST", "mysql")
    user = os.getenv("MYSQL_USER", "root")
    password = os.getenv("MYSQL_PASSWORD", "password")
    db = os.getenv("MYSQL_DATABASE", "lms")
    table = ""

    def __init__(self, app):
        app.config["MYSQL_DATABASE_HOST"] = self.host
        app.config["MYSQL_DATABASE_USER"] = self.user
        app.config["MYSQL_DATABASE_PASSWORD"] = self.password
        app.config["MYSQL_DATABASE_DB"] = self.db

        self.mysql = MySQL(app, cursorclass=DictCursor)

    def cur(self):
        return self.mysql.get_db().cursor()

    def query(self, q):
        h = self.cur()

        if len(self.table) > 0:
            q = q.replace("@table", self.table)

        h.execute(q)
        return h

    def commit(self):
        self.query("COMMIT;")
import sqlite3 as lite
from hashlib import sha256
class Database(object):
    """Class wrapper, which will make interface to SQL datavase"""
    def __init__(self, database):
        self.name_of_database = database #type of database what we want f: mysql...
        self.conn = lite.connect(database)
        self.conn.create_function("sha", 1, Database.sha)

    @staticmethod
    def sha(str):
        """return sha256 of string

        :str: string
        :returns: sha256 hexdigiset string

        """
        return sha256(str.encode("UTF-8")).hexdigest()

    def close(self):
        self.conn.close() 

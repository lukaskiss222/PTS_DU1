import sqlite3 as lite
from hashlib import sha256
class database(object):
    """Class wrapper, which will make interface to SQL datavase"""
    def __init__(self, databse):
        self.databse = databse
        self.conn = lite.connect(databse)
        self.conn.create_function("sha", 1, database.sha)

    @staticmethod
    def sha(str):
        """return sha256 of string

        :str: string
        :returns: sha256 hexdigiset string

        """
        return sha256(str.encode("UTF-8")).hexdigest()

    def close(self):
        self.conn.close() 

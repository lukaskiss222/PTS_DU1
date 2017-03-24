import sqlite3 as lite
class Database(object):
    """Class wrapper, which will make interface to SQL datavase"""
    def __init__(self, database):
        self.name_of_database = database # type of database what we want f: mysql...
        self.conn = lite.connect(database)

    def close(self):
        self.conn.commit() # I commit all changes,
        # what i have done. It is necessery, if you want save changes
        self.conn.close()

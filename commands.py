from decorator import login_class
import sys
class Command(object):

    """
    Abstract Class Command.
    This is Command Design pattern
    """

    def __init__(self, database):
        """Initialize Command Abstract Class
        Should be override
        Also create variable database, which holds refernce to class database

        :database: on this we can perform SQL statment
        """
        self.database = database

    def execute(self):
        """This function execute command 

        """
        raise NotImplementedError("Function execute is not overrided")


class CommandHistory(object):

    """This class will have list of all command.
    It will also add to list and execute the command"""

    def __init__(self):
        """Initialize Class """
        self.history = list()
    
    def addAndExecute(self, command):
        """Function will add Command to history and execute it

        :command: Extented class from Class Command

        """
        self.history.append(command)
        command.execute()
@login_class
class CommandQuit(Command):

    """QUIT Command"""

    def __init__(self, database):
        """Initialize QUIT

        :database: pointer to database
        :

        """
        Command.__init__(self,database)
    def execute(self):
        """QUIT program if password is correct

        """
        self.database.close()
        sys.exit(0)

class CommandPoints(Command):

    """Points Command
    add player name number of points"""

    def __init__(self, database, name, points):
        """Initialize Points

        :database: pointer to database
        :name: name of player
        :number: how many points add to player
        """
        Command.__init__(self, database)
        self.name = name
        self.points = points
    
    def execute(self):
        
        cur = self.database.conn.cursor()
        # get player points
        cur.execute("SELECT id, points from players where name=:name", {"name" :self.name })
        row = cur.fetchone()
        if row is None:
            print("Wrong name!")
            return
        row_id = row[0]
        points = row[1]
        points += self.points
        cur.execute("UPDATE players SET points=:points WHERE id=:id", {"points": points, "id": row_id})

class CommandReduce(Command):

    """Reduce all players points by percentage"""

    def __init__(self, database, percentage):
        """Initialize Reduce

        :database: database
        :percentage: how meny percentage

        """
        Command.__init__(self, database)
        self.percentage = percentage
        
    
    def execute(self):
        cur = self.database.conn.cursor()
        cur.execute("SELECT id,points from players")
        array = cur.fetchall()
        percentage = self.percentage/100
        iterator = map(lambda player: (int(player[1]*percentage), player[0]), array) # reduce all players
        cur.executemany("Update players SET points=(?) WHERE id=(?)", iterator)


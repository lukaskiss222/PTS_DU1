class Command(object):

    """
    Abstract Class Command.
    This is Command Design pattern
    """

    def __init__(self, cursor):
        """Initialize Command Abstract Class
        Should be override
        Also create variable database, which holds refernce to class database

        :cursor: on this we can perform SQL statment
        """
        self.cursor = cursor
        #Setting atributes of functions, which i would like to decorate
        for temp in Command.__dict__:
            if type(Command.__dict__[temp])==type(Command.__init__):
                setattr(Command.__dict__[temp],'decorate',True)
            
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


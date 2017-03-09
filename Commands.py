class Command(object):

    """
    Abstract Class Command.
    This is Command Design pattern
    """

    def __init__(self, database):
        """Initialize Command Abstract Class
        Should be override

        :database: TODO
        :returns: TODO

        """
        raise NotImplementedError("subclass must override __init__")

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


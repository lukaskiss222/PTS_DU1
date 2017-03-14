import getpass
import hashlib

class Login(object):

    """Login singleton class, warapper of login
    It will also decorate Command class, which need password before executing"""
    passwd = ''
    __instance = None
    def __init__(self):
        """will initialize static variable password"""
        if self.__initialized: return
        self.login()
        self.__initialized = True
    def __new__(self):
        """Making it singleton.
        it must be singleton,because when decorator will be creating
        own login object it should do initialize only once.
        :returns: instance
        """
        if self.__instance is None:
            self.__instance = object.__new__(self)
            self.__instance.name = "Singleton login"
            self.__instance.__initialized = False
        return self.__instance


    def login(self):
        """Core function, which will login you.
        :returns: True if login is  succesful

        """
        temp = getpass.getpass()
        temp = temp.encode()
        temp = hashlib.sha256(temp)
        temp = temp.hexdigest()
        if Login.passwd == '': #password is not initialized
            Login.passwd = temp
            return True
        else:
            return Login.passwd == temp

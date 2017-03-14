import login

def login_class(Cls):
    """decorate class, make it login

    :Cls: input class
    :returns: decorated class

    """
    class NewCls(object):
    
        """decorated class"""
    
        def __init__(self,*args,**kwargs):
            """ Constructor"""
            self.login = login.Login()
            self.oInstance = Cls(*args,**kwargs)
        def __getattribute__(self, s):
            """this is called whenever any attribute of a NewCls object is accessed. This function first tries to 
            get the attribute off NewCls. If it fails then it tries to fetch the attribute from self.oInstance (an
            instance of the decorated class).
            :arg1: what we want to get
            :returns: return attribute
            """
            try:
                x = super(NewCls,self).__getattribute__(s)
            except:
                pass #not find in my class, should look in instance
            else:
                return x #i find the attribute in my class, just return it

            x = self.oInstance.__getattribute__(s)
            return x

        def execute(self):
            if self.login.login():
                self.oInstance.execute()
            else:
                print("Wrong Password")
    return NewCls

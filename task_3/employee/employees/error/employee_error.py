class Error(Exception):
    """The myexception class is userdefined  exception, it derives from the base class Exception."""
    pass
class EmployeeDataIsEmpty(Error):
    """The Employee data is empty class is a userdefined exception class for empty employee data.  """
    def __init__(self,agrs):
        self.msg = agrs
    def __str__(self):
        return self.msg 

class NameValueError(Error):
    """The name valid error is a userdefined exception for the invalid name. """
    def __init__(self, args):        
        self.msg = args

    def __str__(self):
        return self.msg        

class IdValueError(Error):
    """This id value error class is a userdefined exception class for the invalid id. """
    def __init__(self, args):        
        self.msg = args

    def __str__(self):
        return self.msg        
class MailIdValueError(Error):
    """ This Mailid value rror class is userdefined exception class for the invalid mailid. """
    def __init__(self,args):
        self.msg = args

    def __str__(self):
        return self.msg 

class SalaryValueError(Error):
    """This salary value error class is a userdefined exception class for the salary. """
    def __init__(self, args):        
        self.msg = args

    def __str__(self):
        return self.msg        

 
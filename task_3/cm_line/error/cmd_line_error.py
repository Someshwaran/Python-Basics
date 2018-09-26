class Error(Exception):
    """The myexception class is userdefined  exception, it derives from the base class Exception."""
    pass
class InvalidInputError(Error):
    """The Invalid Input error is userdefined exception for the invalid input in processing. """
    def __init__(self, args):        
        self.msg = args

    def __str__(self):
        return self.msg  

class EmptyInputError(Error):
    """The Empty  Input error is a userdefined exception for the empty input is given. """
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg
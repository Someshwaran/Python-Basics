class Employee:
    """This class is template to stored data of the employee data. 
    
    They are in private variable so we used setters and getters 
    """
    def __init__(self):
        self.__name = ''
        self.__id = ''
        self.__salary = ''
        self.__mailid = ''

    # setter for all attributes 
    def set__name(self,name):
        self.__name = name
    def set__id(self,id):
        self.__id = id
    def set__salary(self,salary):
        self.__salary = salary
    def set__mailid(self,mailid):
        self.__mailid = mailid
        
    # getter for all attributes 
    def get__name(self):
        return self.__name
    def get__id(self):
        return self.__id
    def get__salary(self):
        return self.__salary
    def get__mailid(self):
        return self.__mailid


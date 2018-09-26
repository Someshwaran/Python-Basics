class AnnotationsClass:
    """AnnotationClass for testing the annotation in python cls. """
    string = 'class variables string'
    def __init__(self):
        self.ob_string = ' instance string'

    @classmethod
    def method_for_class_method(cls_object):
        print('Entered in the class method')
        print(' class variables ',cls_object.string,' instance variable is not avialable ')
    
    @staticmethod
    def defining_static_method():
        print('static method called ')
        print(' class variables ',AnnotationsClass.string,' instance variable is not avialable ')

def main():
    object_anno = AnnotationsClass()
    #calling by object 
    object_anno.method_for_class_method()
    #calling by class name
    AnnotationsClass.method_for_class_method()
    #static method call by class name
    AnnotationsClass.defining_static_method()
    #static method call by object 
    object_anno.defining_static_method()


if __name__ == '__main__':
    main()
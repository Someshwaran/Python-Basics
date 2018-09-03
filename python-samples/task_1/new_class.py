class testing_class:
     
    def test_method(self):
        return "hello world"
#here we going to testing the class and function oject and the method
ob_c = testing_class() 
function_ob = ob_c.test_method 
#new_var = ob_c.test_method()
#print(new_var)
#print(type(testing_class.test_method))
#print(type(ob_c.test_method))
print(function_ob())
#print(new_var.test_method('summa da'))
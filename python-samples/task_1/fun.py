def concat(*args,regx="/"):
    return regx.join(args)
    #print('in concat method ')
    newstring=''
    for inx in range(len(args)):
        newstring+=args[inx]
        #print(inx,newstring)
    return newstring
     
print(concat("one","two","three","four"))
#print("in the method py")
# lambda function
def fundex(arg):
    return lambda x: x+arg
funx = fundex(12)
print(funx(1))
print(funx(2))     
#doc string method 
def mothDoc():
    """
    this is for testing the file level testing 
    """
    pass

print(mothDoc.__doc__)   
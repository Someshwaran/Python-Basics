i=12
def rex1(p_list=i):
     print(p_list,'in the method definition') 
i=5
rex1()
print(i,'the value checking ')
for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,'is not a prime ')
#            rex(n)
            break
    else:
        print(n,'is a Prime')        
if 2==2:
    pass
    #print('pass tesing')   

string = " testing string "
print()

def main_m(string):
    sp_stirng = string.split(' ')
    
    for st in sp_stirng:
        print(st,end=' -- ')
    #ending of the list
    length = len(sp_stirng)
    print('length ',length)
    print(sp_stirng[0],' end ',sp_stirng[length-1])
    
    np_string = sp_stirng[0].capitalize()
    for index in range(1,length-1):
        np_string += ' '+sp_stirng[index]
    if length != 1:
        np_string += ' ' + sp_stirng[length-1].capitalize()
    print('final  string ',np_string)
#end

def main():
    main_m(input())

if __name__ == '__main__':
    main()


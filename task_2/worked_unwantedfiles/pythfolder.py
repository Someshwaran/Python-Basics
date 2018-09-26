import os 

def main(fpath):    
    value = 0
    print('fpath ',fpath,'\n')
    count = 0
    for f in os.listdir(fpath):
        count += 1 
        if os.path.isfile(f):
            print(os.path.getsize(f))
            print('file ',f)
            value += os.path.getsize(f)
        elif os.path.isdir(f):
            print('folder ',os.path.abspath(f))
            value += main(os.path.abspath(f))
    print(' total count file of the folder ',fpath,' count ',count)
    return value
    print('Total value ',value)

if __name__ == '__main__':
    value = main('E:\\python-samples\\')
    print(value)
             

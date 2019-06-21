# this code to find the strings in file or folder path given as input 
import os
import re  
FILE = False
FOLDER = False
total_strings = list()
def print_total_strings():
    # This method is used to print the total strings 
    count =0 
    total_strings_re = set(total_strings)
    for string in total_strings_re:
        print(string,"\t")
        count = count + 1
        if count == 10:
            print("\n")
            count =0 
    # writing strings into the file :
    file_path = os.getcwd()+"\\strings_new_text.txt"
    count =0 
    with open(file_path, "w") as file_pointer:
        for strings in total_strings:
            if "file path " in strings:
                file_pointer.write("\n\n {}\n".format(str(strings)))
            else:
                print(" the writring strings {}".format(strings))
                file_pointer.write("{strings}\n".format(strings= str(strings)))
                count = count +1 
    print("total strings count {}".format(str(len(total_strings))))
    
def string_finder(file_path=None):
    # This method is used to read all strings from the file path given 
    print("Finding the strings*********************************************")
    total_strings.append("file path {}".format(str(file_path)))
    with open(file_path,"r+") as file_p:
        try:
            line = file_p.readline()        
            quoted = re.compile('"[^"]*"')
            quoteds = re.compile('\'[^\']*\'')
            # print("line {}".format(str(line)))
            while not len(line) == 0:         
                # print("line {}".format(str(line)))   
                try:
                    for value in quoted.findall(line):
                        # print("\n ",str(value))
                        total_strings.append(value)
                    for value in quoteds.findall(line):
                        # print("\n ",str(value))
                        total_strings.append(value)
                    line = file_p.readline()
                except UnicodeDecodeError as why:
                    print("Exception {why}".format(why=str(why)))
                    total_strings.append("\n"+line+"\n")
        except Exception as why:
            print("unbale to read the file  Error {}".format(str(why)))
            return None     

def walker_over_dir(folder_path=None):
    # This method is used travase the all the folder and files inside the folder path given 
    with os.scandir(folder_path) as iterator:
        for the_path in iterator:
            print("the path {}".format(str(the_path.path)))
            if the_path.is_file():
                string_finder(the_path.path)
            elif the_path.is_dir():
                walker_over_dir(the_path.path)

def main():
    # read the input 
    f_path = input("Enter the file or folder path:> ")
    if os.path.isdir(f_path):
        global FOLDER
        FOLDER = True
        walker_over_dir(f_path)
    elif os.path.isfile(f_path):
        global  FILE
        FILE = True
        string_finder(f_path)
    else:
        print("Enter path is neither File or Folder")
    # global FILE , FOLDER
    if FILE or FOLDER:
        print("The total words  are \n *****************************************************************************************\n")
        print_total_strings()

if __name__ == "__main__":
    main()
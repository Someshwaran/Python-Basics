def main():
    # reading the string input
    try:
        length_s = int(input())
        m_string = input()
        sub_string = input()
        dir_list = []
        print(" length ",length_s)
        for index in range(1,length_s+1):
            #print(index,' infront ')                    
            dir_list.append([int(input()),int(input())])
            #print(index)
        
        count = 0
        #printing the dir_list
        for list_value in dir_list:
            print(list_value[0],' ',list_value[1])
            x = int(list_value[0])
            y = int(list_value[1])
            t_str = m_string[x] + m_string[y]
            for inn in dir_list:
                if x != inn[0] and y != inn[1]:
                    t_str += m_string[int(inn[0])] + m_string[int(inn[1])]
                    print(t_str,' generated string ')
                    if len(t_str) == len(sub_string):
                        if t_str == sub_string:
                            count += 1
                    elif len(t_str) > len(sub_string):
                        break

                 
    except Exception as identifier:
        print('error ',identifier)
    


if __name__ == '__main__':
    main()
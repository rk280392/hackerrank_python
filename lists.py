if __name__ == '__main__':
    my_list = []
    N = int(input())
    for i in range(0,N):
        my_cmd = input().split()
        if my_cmd[0] == "insert":
            my_list.insert(int(my_cmd[1]),int(my_cmd[2]))
        elif my_cmd[0] == "append":
            my_list.append(int(my_cmd[1]))
        elif my_cmd[0] == "pop":
            my_list.pop()
        elif my_cmd[0] == "remove" :
            my_list.remove(int(my_cmd[1]))
        elif my_cmd[0] == "sort":
            my_list.sort()
        elif my_cmd[0] == "reverse":
            my_list.reverse()
        elif my_cmd[0] == "print":
            print(my_list)




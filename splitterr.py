def mutate_string(string, position, character):
    my_list = list(string)
    my_list[position] = character
    my_string = ''.join(my_list)
    return my_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

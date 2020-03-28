import string
def print_rangoli(size):
    # your code goes here
    alphabet = string.ascii_lowercase[:n]
    my_list = []

    for i in range(size):
        my_str = "-".join(alphabet[i:n])
        my_list.append(my_str[::-1]+my_str[1:])
        
    width = len(my_list[0])

    for i in range(n-1, 0 , -1):
        print(my_list[i].center(width, '-'))

    for i in range(n):
        print(my_list[i].center(width,'-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

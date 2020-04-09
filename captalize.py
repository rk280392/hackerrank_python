import os

def solve(s):
    my_list = s.split()
    return ' '.join((word.capitalize() for word in my_list))
if __name__ == '__main__':

    s = input()
    result = solve(s)
    print(result)

import re

def count_substring(string, sub_string):
    a = len(string)
    b = len(sub_string)
    ocurrence = 0
    for i in range(0, a):
        if string[i:i+b] == sub_string:
            ocurrence += 1
    return ocurrence

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

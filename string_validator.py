#The any() function returns True if any item in an iterable are true, otherwise it returns False.

#If the iterable object is empty, the any() function will return False.

def main():
    s = input()
    print(any(map(str.isalnum, s)))
    print(any(map(str.isalpha, s)))
    print(any(map(str.isdigit, s)))
    print(any(map(str.isupper, s)))
    print(any(map(str.islower, s)))

main()

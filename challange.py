n = int(input("first number: "))
b = input( ).split()
if len(b) < n:
    print(f"please enter {n} values seperated by spaces")
else:
    arr = list(map(int, b))
    arr.sort()
    my_arr = list(set(arr))
    my_arr.remove(max(my_arr))
    print(max(my_arr))

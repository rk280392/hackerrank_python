def mostrecurring(a):
    count = 0
    element = 0
    for i in range(len(a)):
        temp = a[i]
        tempcount = 0
        for p in range(len(a)):
            if a[p] == temp:
                tempcount += 1
        if tempcount > count:
            element = temp
            count = tempcount
    return count


n = int(input())
a = []
for i in range(n):
    my_val = int(input())
    a.append(my_val)
result = mostrecurring(a)
print(result)


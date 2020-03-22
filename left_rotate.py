
def rotLeft(a, k):
    res = [0] * len(a)
    for i in range(0, len(a)):
        if i+k < len(a):
            res[i+k] = a[i]
        else:
            new_index = (i+ k) % len(a)
            res[new_index] = a[i]
    return res




n = int(input())

a = []
for i in range(n):
    my_val = int(input())
    a.append(my_val)

k = int(input())

result = rotLeft(a,k)

for i in result:
    print(i)

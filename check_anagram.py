from collections import Counter

my_str1 = input().upper()
print(my_str1)
my_str2 = input().upper()
print(my_str2)
cnt_1 , cnt_2 = Counter(my_str1), Counter(my_str2)
if cnt_1 == cnt_2:
    print("YES")
else:
    print("NO")

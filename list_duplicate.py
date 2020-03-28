my_list = [int(e) for e in input().split()]
duplicate_dict = {i:my_list.count(i) for i in my_list}
print(duplicate_dict)

duplicate_list = []
for i in range(len(my_list)):
    if my_list[i] not in duplicate_list:
        duplicate_list.append(my_list[i])
print(duplicate_list)

my_list.sort()
for i in range(len(my_list)-1):
    if my_list[i] == my_list[i+1]:
        print(my_list[i])

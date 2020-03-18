name_list = []
score_list = []
for _ in range(int(input())):
    name = input("Please enter student name: ")
    name_list.append(name)
    score = abs(float((input("Please enter student marks: "))))
    score_list.append(score)
mapped = list(zip(name_list, score_list))
second_low_score = sorted(score_list)[1]
mapped.sort(key =  lambda x: x[1])
my_val = []
for name in mapped:
    if name[1] == second_low_score:
        my_val.append((name[0]))
my_val.sort()
for i in my_val:
    print(i)


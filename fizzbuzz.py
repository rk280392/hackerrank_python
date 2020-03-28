num = int(input(""))
my_nums = [int(i) for i in input().split()]
for i in range(1, my_nums[-1]+1):
#    if i%3 != 0 and i%5 !=0:
#        print(i)
    if i % 15 == 0:
        print("FizzBuzz")
        continue
    elif i % 3 == 0:
        print("Fizz")
        continue
    elif i % 5 == 0:
        print("Buzz")
        continue
    print(i)

def average(array):
    # your code goes here
    my_set = set(array)
    average = sum(my_set)/len(my_set)
    return average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

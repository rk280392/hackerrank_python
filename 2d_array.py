import sys

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().split(' ')]
    arr.append(arr_t)
    
def _hourglassSum(matrix, row, col):
    my_sum = 0
    my_sum += matrix[row-1][col-1]
    my_sum += matrix[row-1][col]
    my_sum += matrix[row-1][col+1]
    my_sum += matrix[row][col]
    my_sum += matrix[row+1][col-1]
    my_sum += matrix[row+1][col]
    my_sum += matrix[row+1][col+1]
    return my_sum



max_glashour_sum = -63
for i in range(1,5):
    for j in range(1,5):
        current_sum = _hourglassSum(arr, i, j)
        print(current_sum)
        if current_sum > max_glashour_sum:
            max_glashour_sum = current_sum
print(max_glashour_sum)


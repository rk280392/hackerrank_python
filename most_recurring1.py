def most_frequent(List): 
    counter = 0
    num = List[0] 
      
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
  
    return num 

n = int(input())
List = []
for i in range(n):
    my_val = int(input())
    List.append(my_val)
result = most_frequent(List)
print(result)

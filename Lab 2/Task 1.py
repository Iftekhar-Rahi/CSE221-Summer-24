num,target=map(int,input().split())
my_array=list(map(int,input().split()))
def target_sum_finder(my_array,target):
    left = 0
    right = len(my_array) - 1
    while left < right:
        current_sum = my_array[left] + my_array[right]
        if current_sum == target:
            index=str(left+1)+" "+str(right+1)
            return(index)
        elif current_sum < target:
            left += 1
        elif current_sum < target:
            right -= 1
        else:
            return("IMPOSSIBLE")
value=target_sum_finder(my_array,target)
print(value)
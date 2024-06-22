first_len=int(input())
first_list=list(map(int,input().split()))
second_len=int(input())
second_list=list(map(int,input().split()))

def two_sorted_list_to_one_sorted_list(first_len,first_list,second_len,second_list):
    new_list=[]
    i=0
    j=0
    while i<first_len and j<second_len:
        if first_list[i]<second_list[j]:
            new_list.append(first_list[i])
            i+=1
        else:
            new_list.append(second_list[j])
            j+=1
    while i<first_len:
        new_list.append(first_list[i])
        i += 1
    while j<second_len:
        new_list.append(second_list[j])
        j += 1
    return new_list
stored=two_sorted_list_to_one_sorted_list(first_len,first_list,second_len,second_list)
print(stored)

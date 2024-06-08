my_list=[2,8,5,3,9,4,1]
for i in range(len(my_list)):
    for j in range(len(my_list)-1):
        if my_list[j]>my_list[j+1]:
            temp=my_list[j]
            my_list[j]=my_list[j+1]
            my_list[j+1]=temp
        else:
            pass
print(my_list)
# commom items
list1 = [1, 342, 75, 23, 98]

list2 = [75, 23, 98, 12, 78, 10, 1]

for i in range(0,len(list1)):
    for j in range(0,len(list2)):
        if list1[i]==list2[j]:
            print(list1[i])


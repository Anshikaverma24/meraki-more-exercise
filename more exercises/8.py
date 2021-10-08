# unique values from 2 lists
# list1 = [1, 5, 10, 12, 16, 20,20]

# list2 = [1, 2, 10, 13, 16]
def unique(list1,list2):
    new=[]
    list_set=set(list1)
    list_set2=set(list2)
    new.append(list_set)
    new.append(list_set2)
    print(new)



unique([1, 5, 10, 12, 16, 20,20],[1, 2, 10, 13, 16])


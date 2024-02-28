l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def merge_sort(list1,list2):
    list3 = list1 + list2
    list3.sort()
    return list3
    
print(merge_sort(l_1,l_2))
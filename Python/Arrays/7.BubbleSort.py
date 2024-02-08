"""
Create a sorting algorithm (like bubble sort) and use it to sort a list of integers.
"""
def bubblesort(list1):
    end = len(list1)
    for x in range(end):
        for y in range(end-x-1):
            if list1[y] > list1[y+1]:
                temp = list1[y]
                list1[y] = list1[y+1]
                list1[y+1] = temp
    return print(f"Sorted List: {list1}")
list1 = [1,4,2,8,3,9,0,11,64,21]
print(f"Unsorted List: {list1}")
bubblesort(list1)



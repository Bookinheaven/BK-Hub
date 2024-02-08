mylist = [1,2,3,4,5,6,7,8,9]
modified_list = [(lambda x : x ** 2)(x) for x in mylist]
print(modified_list)
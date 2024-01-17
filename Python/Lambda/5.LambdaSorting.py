my_list = [("apple", 50), ("banana", 10), ("cherry", 30)]
sorted_list = sorted(my_list, key=lambda x : x[1])   #sorted(iterable, key=None, reverse=False)
print(sorted_list)
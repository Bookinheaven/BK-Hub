def add(nums):
    y = 0
    for num in nums:
        y += num
    return y

nums = [int(x) for x in (input("Enter how many numbers you want to find arithmetic: ")).split()]
print(add(nums))

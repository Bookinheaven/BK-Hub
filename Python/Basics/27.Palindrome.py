def isPalindrome(x: int) -> bool:
        x = str(x)
        return True if x == x[::-1] else False
    
print(isPalindrome(-121))

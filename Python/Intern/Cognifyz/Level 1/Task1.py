"""
Task: String Reversal

Create a Python function that takes a string as input and returns the reverse of
that string. For example, if the input is "hello," the function should return "olleh.
"""

# The Function for string reversal
def Reversal(string: str):
    # Try Except Block to check if any unexpected errors occurs
    try:
        # Checking if user provided empty string
        if string == "":
            raise Exception("Input String should be provided!")
        else:
            return string[::-1]
    except Exception as e: 
        print(f"Exception: {e}")

word : str = Reversal("Tanvik")
print(word)
print(type(word))
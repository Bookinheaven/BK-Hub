"""
Read the input from the console and write it into a file until the word end of the line reaches.
"""
def write_file(file_path):
    with open(file_path, 'w') as file:
        while True:
            user_input = input("Enter a line (type 'end of the line' to stop): ")
            if user_input.lower() == 'end of the line':
                break
            file.write(user_input + '\n')
write_file("desB.txt")
print("Lines written to file successfully.")

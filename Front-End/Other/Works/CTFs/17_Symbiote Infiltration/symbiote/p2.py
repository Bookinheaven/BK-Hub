import base64

def encode_text(text, times):
    encoded_text = text.encode() 
    for _ in range(times):
        encoded_text = base64.b64encode(encoded_text)  
    return encoded_text.decode() 

text = input("Enter the text to encode: ")
times = int(input("Enter the number of times to encode: "))

encoded_result = encode_text(text, times)
print("\nEncoded Text:")
print(encoded_result)

# import base58

# flag = "{MC_CTF:Never_Miss_A_Secret}"

# base58_encoded_flag = base58.b58encode(flag.encode()).decode()
# print(f"Base58 Encoded Flag: {base58_encoded_flag}")

# from stegano.lsb import hide

# image_path = "./trickshot_l2.png"

# hidden_data = "2GZCLNQJGsabAAy14heoLvvYMzCXZrawjcijLrx"

# new_image_path = "trickshot_l3.png"
# secret_image = hide(image_path, hidden_data)
# secret_image.save(new_image_path)
# print(f"Hidden Base58 string inside {new_image_path}")

from stegano.lsb import reveal

hidden_message = reveal("trickshot_l3.png")
print("Hidden Message:", hidden_message)

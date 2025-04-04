import base64

def decode_until_flag(file_path):
    try:
        with open(file_path, "r") as file:
            encoded_text = file.read().strip()

        decode_count = 0 

        while True:
            try:
                decoded_bytes = base64.b64decode(encoded_text)
                decoded_text = decoded_bytes.decode("utf-8")

                decode_count += 1  
                print(f"[{decode_count}] Decoded: {decoded_text}")

                if decoded_text.startswith("{"):
                    print(f"\n🎉 Found the flag after {decode_count} decodings: {decoded_text}")
                    break

                encoded_text = decoded_text  
            except Exception as e:
                print(f"\n❌ Decoding failed after {decode_count} attempts:", e)
                break

    except FileNotFoundError:
        print("\n❌ Error: File not found.")

file_path = "code.txt"  
decode_until_flag(file_path)

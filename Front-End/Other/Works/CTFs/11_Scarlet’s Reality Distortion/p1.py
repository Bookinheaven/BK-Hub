from PIL import Image, PngImagePlugin

image_path = "./real_image_wanda.jpg" 
img = Image.open(image_path).convert("RGB") 

meta = PngImagePlugin.PngInfo()
hidden_flag = "FLAG: {MC_CTF:No_More_Secrets_Reality_Broken}"
meta.add_text("reality_warp", hidden_flag.encode("utf-8")) 

new_image_path = "wanda_reality_hidden.png"
img.save(new_image_path, format="PNG", pnginfo=meta)

print(f"Modified image saved as: {new_image_path}")

# from PIL import Image

# img = Image.open("wanda_reality_hidden.png")
# metadata = img.info  

# print(metadata)  

from PIL import Image, PngImagePlugin

image_path = "trickshot.png"  # Replace with your actual image filename
img = Image.open(image_path)

# Add metadata with the hidden hint
meta = PngImagePlugin.PngInfo()
hidden_hint = "Look deeper. LSB is your friend."
meta.add_text("XMP-metadata", hidden_hint)

# Save the modified image with metadata
new_image_path = "trickshot_l2.png"  # Save with a different name to preserve the original
img.save(new_image_path, pnginfo=meta)

print(f"Modified image saved as: {new_image_path}")

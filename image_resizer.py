from PIL import Image

image = Image.open("soccer_practice.jpg")

print(f"Current Size: {image.size}")

resized_image = image.resize((500,500))

resized_image.save('soccer-500.jpg')
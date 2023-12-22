from PIL import Image

image = Image.open("soccer_practice.jpg")


def resize_image(size1, size2):
    resized_image = image.resize((size1, size2))

    # NOTE: Does NOT incorporate the aspect ratio/proportion
    resized_image.save(f"soccer-{size1}x{size2}.jpg")
    print(f"Image resized to {size1}x{size2}")

print(f"Current Size: {image.size}")

size1 = int(input("Enter Width: "))
size2 = int(input("Enter Height: "))

resize_image(size1, size2)
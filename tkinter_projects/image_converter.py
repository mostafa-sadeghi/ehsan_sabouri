from PIL import Image


def convert_image(path, image_mode, file_name):
    print("from converted_image_function", path, image_mode, file_name)

    image = Image.open(path)
    img = image.convert("RGB")
    # print(image.mode)
    img.save(f"{file_name}.{image_mode}",
             format=image_mode, size=[(32, 32)])

from PIL import Image
import io

def resize(image_path, width=0, height=0):
    image = Image.open(image_path)
    
    width = int(float(width))
    height = int(width * (image.size[1] / image.size[0]))
    resize_image = image.resize((width, height))
    
    file_object = io.BytesIO()
    resize_image.save(file_object, format=image.format)
    file_object.seek(0)
    return file_object
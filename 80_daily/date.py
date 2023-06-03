from PIL import Image
from PIL.ExifTags import TAGS

def get_date_taken(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if exif_data is not None:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag)
                if tag_name == 'DateTimeOriginal':
                    return value
    except (AttributeError, KeyError, IndexError):
        pass

    return None

# 示例用法
image_path = 'C:\\Users\\FENG\\Desktop\\aa\\20230601_203407-COLLAGE.jpg'
date_taken = get_date_taken(image_path)
if date_taken is not None:
    print(f"Date taken: {date_taken}")
else:
    print("Unable to retrieve date taken.")

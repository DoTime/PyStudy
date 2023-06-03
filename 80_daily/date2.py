import os
from PIL import Image
from PIL.ExifTags import TAGS
import shutil
from datetime import datetime


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


def copy_files_with_date_taken(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            # print(file_path)
            date_taken = get_date_taken(file_path)

            if date_taken is not None:
                date_taken = datetime.strptime(date_taken, "%Y:%m:%d %H:%M:%S")
                new_filename = date_taken.strftime("%Y%m%d_%H%M%S") + os.path.splitext(file)[1]
                destination_path = os.path.join(destination_dir, new_filename)
                shutil.copy2(file_path, destination_path)
                print(destination_path)


# 示例用法
source_directory = 'H:/20230602/aa'
destination_directory = source_directory + "_tar"

copy_files_with_date_taken(source_directory, destination_directory)

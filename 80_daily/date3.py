import os
import re
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS
import shutil

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
            date_taken = get_date_taken(file_path)

            # 移除不需要的文件
            #
            # if file.endwith("MP") | file.endwith("gif"):
            #     continue
            #




# mmexp微信导出图片 没有date_taken

            if file.endswith("mp4") :
                file_number = int(file[8:])
                date_taken = datetime.fromtimestamp(file_number).strftime("%Y%m%d_%H%M%S")
                new_filename = f"{date_taken}{os.path.splitext(file)[1]}"

            elif file.startswith("mmexport") and file.endswith("jpg") and re.match(r'^\d+$', file[8:]):
                file_number = int(file[8:])
                date_taken = datetime.fromtimestamp(file_number).strftime("%Y%m%d_%H%M%S")
                new_filename = f"{date_taken}{os.path.splitext(file)[1]}"


            # 普通photo导出的文件
            elif date_taken is not None:
                date_taken = datetime.strptime(date_taken, "%Y:%m:%d %H:%M:%S")
                new_filename = date_taken.strftime("%Y%m%d_%H%M%S") + os.path.splitext(file)[1]





            else:

                continue

            destination_path = os.path.join(destination_dir, new_filename)
            shutil.copy2(file_path, destination_path)

# 示例用法
source_directory = 'H:/20230602/aa'
destination_directory = source_directory + "_tar"


copy_files_with_date_taken(source_directory, destination_directory)

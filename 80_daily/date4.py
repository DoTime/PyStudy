import os
import re
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS
import shutil

def get_date_taken(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() in ['.jpg', '.jpeg', '.png']:
        try:
            image = Image.open(file_path)
            exif_data = image._getexif()
            if exif_data is not None:
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag)
                    if tag_name == 'DateTimeOriginal':
                        return value
        except (AttributeError, KeyError, IndexError):
            pass
    return None

def process_files(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            _, file_extension = os.path.splitext(file_path)

            if file_extension.lower() in ['.mp', '.gif']:
                # Skip processing for MP and GIF files
                continue
            elif file_extension.lower() == '.mp4':
                # Extract 8-18 characters from file name and convert to datetime format
                timestamp = file[8:18]
                try:
                    timestamp = int(timestamp)
                    date_taken = datetime.fromtimestamp(timestamp).strftime("%Y%m%d_%H%M%S")
                    new_filename = f"{date_taken}{file_extension}"
                except ValueError:
                    continue
            else:
                date_taken = get_date_taken(file_path)
                if date_taken is not None:
                    try:
                        # timestamp = int(date_taken)
                        # date_taken = datetime.fromtimestamp(timestamp).strftime("%Y%m%d_%H%M%S")

                        dt = datetime.datetime.strptime(date_taken, "%Y:%m:%d %H:%M:%S")
                        date_taken = dt.strftime("%Y%m%d_%H%M%S")



                        new_filename = f"{date_taken}{file_extension}"


                    except ValueError as e:
                        print(f"Error processing file: {file} - {e}")
                        continue
                else:
                    # Extract 8-18 characters from file name and convert to datetime format
                    timestamp = file[8:18]
                    try:
                        timestamp = int(timestamp)
                        date_taken = datetime.fromtimestamp(timestamp).strftime("%Y%m%d_%H%M%S")
                        new_filename = f"{date_taken}{file_extension}"
                    except ValueError:
                        # Remove unwanted strings from file name
                        new_filename = re.sub(r'-COLLAGE|PXL_|IMG_|MV|Screenshot_|-COLLAGE|VID_', '', file)
                        destination_path = os.path.join(destination_dir, new_filename)
                        shutil.copy2(file_path, destination_path)
                        print(f"Copied file: {file} -> {new_filename}")
                        continue

            destination_path = os.path.join(destination_dir, new_filename)
            shutil.copy2(file_path, destination_path)
            print(f"Copied file: {file} -> {new_filename}")

# 示例用法
source_directory = 'H:/20230602/20230603_1903/aa'
# source_directory = 'H:/20230602/20230603/aa'

destination_directory= source_directory+'_tar'


process_files(source_directory, destination_directory)

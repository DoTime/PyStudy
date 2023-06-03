import os
import shutil
import datetime
from PIL import Image

source_folder = "H:/20230603/movie"
target_folder = source_folder + "_tar"

if not os.path.exists(target_folder):
    os.makedirs(target_folder)

for root, dirs, files in os.walk(source_folder):
    for file in files:
        file_path = os.path.join(root, file)
        file_extension = os.path.splitext(file)[1].lower()

        # 跳过处理MP和gif结尾的文件
        if file_extension in [".mp", ".gif"]:
            continue

        # 处理mp4文件
        if file_extension == ".mp4":
            filename = os.path.splitext(file)[0]
            timestamp = filename[8:18]
            try:
                timestamp = int(timestamp)
                date_taken = datetime.datetime.fromtimestamp(timestamp).strftime("%Y%m%d_%H%M%S")
                new_filename = f"{date_taken}{file_extension}"
            except ValueError as e:
                print(f"Error processing file: {file} - {e}")
                continue

        # 处理图片文件
        elif file_extension in [".jpg", ".jpeg", ".png"]:
            img = Image.open(file_path)
            exif_data = img._getexif()

            if exif_data and 36867 in exif_data:
                date_taken = exif_data[36867]
                try:
                    dt = datetime.datetime.strptime(date_taken, "%Y:%m:%d %H:%M:%S")
                    date_taken = dt.strftime("%Y%m%d_%H%M%S")
                    new_filename = f"{date_taken}{file_extension}"
                except ValueError as e:
                    print(f"Error processing file: {file} - {e}")
                    continue
            else:
                filename = os.path.splitext(file)[0]
                timestamp = filename[8:18]
                try:
                    timestamp = int(timestamp)
                    date_taken = datetime.datetime.fromtimestamp(timestamp).strftime("%Y%m%d_%H%M%S")
                    new_filename = f"{date_taken}{file_extension}"
                except ValueError as e:
                    print(f"Error processing file: {file} - {e}")
                    continue

        # 移除字符中的-COLLAGE、PXL_或IMG_
        else:
            new_filename = file.replace("-COLLAGE", "").replace("PXL_", "").replace("IMG_", "").replace("IMG_", "").replace("MV", "").replace("Screenshot_", "").replace("VID_", "")

        target_file_path = os.path.join(target_folder, new_filename)
        # print(f"Copied file: {file_path} -> {target_file_path}")
        shutil.copyfile(file_path, target_file_path)

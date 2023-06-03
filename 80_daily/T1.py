import os
import re
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS
import shutil


date_taken = get_date_taken(file_path)
try:
    timestamp = int(date_taken)
    date_taken = datetime.fromtimestamp(timestamp).strftime("%Y%m%d_%H%M%S")
    new_filename = f"{date_taken}{file_extension}"
except ValueError as e:
    print(f"Error processing file: {file} - {e}")

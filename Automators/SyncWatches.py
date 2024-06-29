# This should sync all images, folders into the photography Watches Folder
# 
# 

import os
import shutil

source_dir = r"C:\Users\jessie\Desktop\Finalized Images DONE\Watches"
destination_dir = r"M:\Photography Dept\Watches"

# Copy files from source to destination
shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)

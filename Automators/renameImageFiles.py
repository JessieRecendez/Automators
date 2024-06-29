# This should do a rename of image files. I may have to play with webp and jfif to make sure they're now jpg and such
# Working as of 2023-09-06


import os
import shutil


def rename_files_from_list(folder_path, list_file_path):
    renamed_files = {}  # Store renamed file names
    with open(list_file_path, 'r') as list_file:
        for line in list_file:
            parts = line.strip().split('\t')  # Split using tab as the separator
            if len(parts) == 2:
                current_name, new_name = parts
                current_path = os.path.join(folder_path, current_name)
                new_path = os.path.join(folder_path, new_name)
                if os.path.exists(current_path):
                    os.rename(current_path, new_path)
                    renamed_files[current_name] = new_name
                    print(f"Renamed: {current_name} -> {new_name}")
                else:
                    print(f"File not found: {current_name}")

    # After renaming, convert remaining .jfif files to .png
    # After renaming, convert remaining .webp files to .png
    for filename in os.listdir(folder_path):
        if filename.endswith('.png') and filename not in renamed_files:
            jfif_path = os.path.join(folder_path, filename)
            png_path = os.path.join(folder_path, os.path.splitext(filename)[0] + '.jpg')
            # Rename the extension from .jfif to .png
            shutil.move(jfif_path, png_path)
            renamed_files[filename] = os.path.splitext(filename)[0] + '.jpg'
            print(f"Converted: {filename} to {os.path.basename(png_path)}")
        elif filename.endswith('.webp') and filename not in renamed_files:
            webp_path = os.path.join(folder_path, filename)
            png_path = os.path.join(
                folder_path, os.path.splitext(filename)[0] + '.jpg')
            # Rename the extension from .webp to .png
            shutil.move(webp_path, png_path)
            renamed_files[filename] = os.path.splitext(filename)[0] + '.jpg'
            print(f"Converted: {filename} to {os.path.basename(png_path)}")


if __name__ == "__main__":
    folder_path = r"c:\Users\recen\Downloads"
    list_file_path = r"Automators/PHOTO-RENAME.txt"
    rename_files_from_list(folder_path, list_file_path)

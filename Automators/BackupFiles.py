# Sometimes I just don't have the time to transfer every file, and remember which is all the stuff I updated since last week.
# Working perfectly since 2023-12-21

# This backs up all my selected files to my folder in the destination_folder

import os
import shutil
import datetime

def backup_data(source_folders, destination_folder, last_backup_file):
    try:
        # Ensure the destination folder exists
        if not os.path.exists(destination_folder):
            print(f"Destination folder '{destination_folder}' does not exist.")
            return

        # Load the last backup timestamp from a file
        last_backup_timestamp = load_last_backup_timestamp(last_backup_file)

        # Iterate over each source folder
        for source_folder in source_folders:
            # Ensure the source folder exists
            if not os.path.exists(source_folder):
                print(f"Source folder '{source_folder}' does not exist.")
                continue

            # Get the last part of the source folder path
            source_folder_name = os.path.basename(os.path.normpath(source_folder))

            # Iterate over all files and subdirectories in the source folder
            for root, dirs, files in os.walk(source_folder):
                for file in files:
                    source_path = os.path.join(root, file)
                    relative_path = os.path.relpath(source_path, source_folder)
                    destination_path = os.path.join(destination_folder, source_folder_name, relative_path)

                    # Check if the item is a file
                    if os.path.isfile(source_path):
                        # Check the last modified timestamp of the file
                        last_modified_timestamp = os.path.getmtime(source_path)

                        # If the file has been modified since the last backup, copy it
                        if last_modified_timestamp > last_backup_timestamp:
                            # Create the necessary subdirectories in the destination folder
                            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                            shutil.copy2(source_path, destination_path)
                            print(f"Copied: {source_path} to {destination_path}")

        # Update the last backup timestamp
        update_last_backup_timestamp(last_backup_file)

        print("Backup completed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

def load_last_backup_timestamp(last_backup_file):
    # Load the last backup timestamp from a file
    try:
        with open(last_backup_file, 'r') as file:
            timestamp_str = file.read().strip()
            return float(timestamp_str) if timestamp_str else 0
    except FileNotFoundError:
        return 0

def update_last_backup_timestamp(last_backup_file):
    # Update the last backup timestamp in a file
    try:
        timestamp = str(datetime.datetime.now().timestamp())
        with open(last_backup_file, 'w') as file:
            file.write(timestamp)
    except Exception as e:
        print(f"Unable to update last backup timestamp: {e}")

# Replace these paths with your actual source and destination paths
# Keep it broken down by lines to read it easier in case I get a smaller screen
source_folders = [r"c:\Users\jessie\Desktop\AHK Stuff", 
                  r"c:\Users\jessie\Desktop\DataScrape", 
                  r"c:\Users\jessie\Desktop\Finalized Images DONE", 
                  r"c:\Users\jessie\Desktop\Images to fix", 
                  r"c:\Users\jessie\Desktop\Python Scrapers",  
                  r"c:\Users\jessie\Desktop\chromedriver.exe", 
                  r"c:\Users\jessie\Desktop\LICENSE.chromedriver"]

# destination_folder = r"M:\Jessie" # backup location to back things up to/this was my Zadok folder
destination_folder = r"D:\Work" # Should go to flash drive D
last_backup_file = r"C:\Users\jessie\Desktop\Python Scrapers\last_backup_timestamp.txt" #should be made on its own/my current device

# Call the function to perform the backup
backup_data(source_folders, destination_folder, last_backup_file)
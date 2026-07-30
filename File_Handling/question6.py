# Import shutil library to copy files
import shutil
# Import os library to work with files and folders
import os
# Import Path from pathlib for working with file paths
from pathlib import Path

# Ask user to enter the filename they want to backup
filename = input("Enter the filename to backup: ")

# Check if the file exists in the system
if not os.path.exists(filename):
    # If file does not exist, print error message
    print(f"Error: File '{filename}' not found.")
else:
    # If file exists, create a backup folder name
    backup_folder = "backup"
    # Check if backup folder already exists
    if not os.path.exists(backup_folder):
        # If backup folder does not exist, create it
        os.makedirs(backup_folder)
    
    # Get only the filename from the full path (remove directory part)
    file_basename = os.path.basename(filename)
    
    # Create the full path where the backup file will be stored
    backup_path = os.path.join(backup_folder, file_basename)
    # Copy the file to the backup folder with the same name
    shutil.copy2(filename, backup_path)
    
    # Print success message showing where file was backed up
    print(f"File '{filename}' has been successfully backed up to '{backup_path}'")

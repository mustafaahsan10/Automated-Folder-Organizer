import os
import shutil

def organize_by_extension(folder_path):
    # Check if the folder path exists
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return

    # Dictionary to keep track of extensions and their respective files
    ext_dict = {}

    # List all files in the directory
    for item in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, item)):
            ext = os.path.splitext(item)[1].lower()
            if ext not in ext_dict:
                ext_dict[ext] = []
            ext_dict[ext].append(item)

    # Create subfolders and move files
    for ext, files in ext_dict.items():
        if ext:  # Skip files without an extension
            # Folder name for the extension
            ext_folder = os.path.join(folder_path, ext[1:])  # remove the dot from extension
            if not os.path.exists(ext_folder):
                os.makedirs(ext_folder)

            # Move files into their respective folders
            for file in files:
                shutil.move(os.path.join(folder_path, file), os.path.join(ext_folder, file))

    print("Organizing complete.")

# Replace with the user's folder path
folder_path = r'C:\Users\musta\Downloads'

# Run the function with the provided path
organize_by_extension(folder_path)

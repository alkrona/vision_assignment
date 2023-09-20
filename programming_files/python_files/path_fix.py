import os

# Get the current working directory
current_directory = os.getcwd()

# Construct the absolute path to the file
file_path = os.path.join(current_directory, 'image_data', 'AppleTree.png')

# Check if the file exists
if os.path.exists(file_path):
    print(f"The file exists at: {file_path}")
else:
    print(f"No file found at: {file_path}")
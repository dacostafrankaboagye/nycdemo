import os
import shutil

import kagglehub

# Step 1: Download dataset (default cache location)
print("Downloading dataset...")
download_path = kagglehub.dataset_download("dgomonov/new-york-city-airbnb-open-data")
print("Downloaded to:", download_path)

# Step 2: Set destination folder (your current working directory)
destination = os.getcwd()

# Optional
destination = os.path.join(os.getcwd(), "data")
os.makedirs(destination, exist_ok=True)

print("Moving dataset files to:", destination)

# Step 3: Move all files from cache folder to destination
for file_name in os.listdir(download_path):
    src = os.path.join(download_path, file_name)
    dst = os.path.join(destination, file_name)
    if os.path.exists(dst):
        print(f"File already exists, skipping: {dst}")
    else:
        shutil.move(src, dst)
        print(f"Moved: {file_name}")

print("Done! All files are now in:", destination)

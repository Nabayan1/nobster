#My Personal Favourite!

from pathlib import Path
import shutil

target_folder = Path("C:/Users/Nabayan Chakma/Downloads")
destination_folder_1 = Path("C:/Users/Nabayan Chakma/OneDrive/Documents/pdfs")
destination_folder_2 = Path("C:/Users/Nabayan Chakma/Downloads/Programs")
destination_folder_3 = Path("C:/Users/Nabayan Chakma/Downloads/Zips")

files = []

for file_path in target_folder.iterdir():
    if file_path.is_file():
        #print(file_path.name)
        files.append(file_path)

#Categorizing/moving the files

destination_folder_1.mkdir(parents=True, exist_ok=True)

for file in files:
    if file.suffix == ".pdf" or file.suffix == ".png": 
        shutil.move(file, destination_folder_1/file.name)

for file in files:
    if file.suffix == ".exe": 
        
        shutil.move(file, destination_folder_2/file.name)

for file in files:
    if file.suffix == ".zip": 
        shutil.move(file, destination_folder_3/file.name)
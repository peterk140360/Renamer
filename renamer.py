# Fehlerquellen: Bindestrich oder Punkt im originalen Dateinamen. 
# Beispiel: EGIRAFFE Biophysik UE - anitnelav - Pruefungsfragenausarbeitung - 2.TK alle Beispiele
#           EGIRAFFE Biophysik UE - nannerl - Klausurangabe - 2017.05.15 - - erste Teilklausur

#%%

#changed "-" to " - "
 
import os



# get the current working directory
source_folder = input("Enter the path to your folder: ")
# cwd = os.getcwd()

# define the path to the directory containing the files
# folder_path = os.path.join(cwd, "Egiraffe")
folder_path = source_folder

# get all the filenames in the directory
files = os.listdir(folder_path)

# iterate over each file
for filename in files:
    # check if the filename has at least two dashes
    print(filename.count(" - "))
    if filename.count(" - ") == 2:
        # split the filename into parts
        parts = filename.split(" - ")
        # split the last part by '.'
        doctype = filename.split('.')[-1]
        print(f"parts: {parts}")
        print(f"filename_parts: {doctype}")
        # extract the first part
        first_part = parts[0]
        # extract the second part
        second_part = parts[1]
        # extract the last part
        if parts[-1].count(".") > 1:
            last_part = parts[-1].split(".")[:3]
            last_part = f"{last_part[0]}.{last_part[1]}.{last_part[2]}"
        else:
            last_part = parts[-1].split(".")[0]
        # create the new filename
        new_filename = f"{first_part} - {last_part} - {second_part}.{doctype}"
        # rename the file
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
    elif filename.count(" - ") == 3:
        # split the filename into parts
        parts = filename.split(" - ")
        # split the last part by '.'
        doctype = filename.split('.')[-1]
        print(f"parts: {parts}")
        print(f"filename_parts: {doctype}")
        # extract the first part
        first_part = parts[0]
        # extract the second part
        second_part = parts[1]
        # extract the third part
        third_part = parts[2]
        # extract the last part
        if parts[-1].count(".") > 1:
            last_part = parts[-1].split(".")[:3]
            last_part = f"{last_part[0]}.{last_part[1]}.{last_part[2]}"
        else:
            last_part = parts[-1].split(".")[0]
        print(f"last_part: {last_part}")
        # create the new filename
        new_filename = f"{first_part} - {third_part} - {last_part} - {second_part}.{doctype}"
        # rename the file
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
    elif filename.count(" - ") == 4:
        # split the filename into parts
        parts = filename.split(" - ")
        # split the last part by '.'
        doctype = filename.split('.')[-1]
        print(f"parts: {parts}")
        print(f"filename_parts: {doctype}")
        # extract the first part
        first_part = parts[0]
        # extract the second part
        second_part = parts[1]
        # extract the third part
        third_part = parts[2]
        # extract the fourth part
        fourth_part = parts[3]
        # extract the last part
        if parts[-1].count(".") > 1:
            last_part = parts[-1].split(".")[:3]
            last_part = f"{last_part[0]}.{last_part[1]}.{last_part[2]}"
        else:
            last_part = parts[-1].split(".")[0]
        print(f"last_part: {last_part}")
        # create the new filename
        new_filename = f"{first_part} - {third_part} - {fourth_part} - {second_part}.{doctype}"
        # rename the file
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
    else:
        print("Filename is not compartible")
# %%

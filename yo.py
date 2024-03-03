import os
import chardet
import re
folder_path = "sub_sub"
output_file = "all_in_one.txt"

# Open the output file in write mode with UTF-8 encoding
with open(output_file, "w", encoding="utf-8") as outfile:
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Check if there are any files in the folder
    if len(files) == 0:
        outfile.write("لا توجد ملفات في المجلد.")
    else:
        # Convert the path to the absolute folder path
        folder_path = os.path.abspath(folder_path)

        # Merge the contents of the files into the output file
        for file_name in files:
            # Add the file name to the output file
            outfile.write(f"--------------------------------------------------------------{file_name}--------------------------------------------------------------\n")

            # Open the file and merge its contents
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())

            # Add an empty line between each file
            outfile.write("\n")
    
    print("تم دمج الملفات بنجاح.")
    

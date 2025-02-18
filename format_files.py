import os

directory = r'C:\Users\nibra\OneDrive\Desktop\thanasis\ΠΕΙΡΑΙΑΣ-1 (PIR)\2021-2023'

def rename_files(directory):
    for filename in os.listdir(directory):
        # Check if the file contains '#' and has an extension
        if '#' in filename and '.' in filename:
            # Split the filename into name and extension
            name, ext = os.path.splitext(filename)
            # Replace '#' with '_'
            new_name = name.replace('#', '_')
            # Add the new extension
            new_filename = new_name + '.csv'
            # Get the full paths
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            # Rename the file
            os.rename(old_file, new_file)
            print(f'Renamed: {old_file} to {new_file}')

# Specify the directory containing the files

# Call the function to rename files
rename_files(directory)
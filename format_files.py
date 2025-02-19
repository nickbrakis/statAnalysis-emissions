import os

directory = r'C:\Users\nibra\OneDrive\Desktop\thanasis\ΠΕΙΡΑΙΑΣ-1 (PIR)\2021-2023'

def rename_files(directory):

    for filename in os.listdir(directory):

        if '#' in filename and '.' in filename:

            name, ext = os.path.splitext(filename)
            new_name = name.replace('#', '_')
            new_filename = new_name + '.csv'
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            os.rename(old_file, new_file)
            print(f'Renamed: {old_file} to {new_file}')
            
rename_files(directory)
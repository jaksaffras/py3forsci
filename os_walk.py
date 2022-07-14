import os

#   virtual_list_of_tuples =  os.walk(starting_dir)

start_folder = "."

git_folder = '.git'

for folder, subfolders, files in os.walk(start_folder):
    if git_folder in subfolders:
        subfolders.remove(git_folder)
    print(folder)
    for file_name in files:
        if file_name.endswith('.py'):
            file_path = os.path.join(folder, file_name)
            file_size = os.path.getsize(file_path)
            print(f"   {file_size:10d} {file_name}")


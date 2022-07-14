import os

for entry in os.scandir('DATA'):
    if entry.is_file():
        if entry.name.endswith('.txt'):
            # print(entry.path)
            file_size = os.path.getsize(entry.path)
            print(f"{file_size:8d} {entry.path}")
            # print("      ", entry.stat())

from datetime import datetime
import os   #  os.path

folder = "DATA"
file_name = "alice.txt"

file_path = os.path.join(folder, file_name)
print("file_path: {}".format(file_path))

file_size = os.path.getsize(file_path)
print("file_size: {}".format(file_size))

file_folder = os.path.dirname(file_path)
file_basename = os.path.basename(file_path)
print("file_folder: {}".format(file_folder))
print("file_basename: {}".format(file_basename))
abs_path = os.path.abspath(file_path)
print("abs_path: {}".format(abs_path))

raw_ts = os.path.getmtime(file_path)
print("raw_ts: {}".format(raw_ts))
ts = datetime.fromtimestamp(raw_ts)
print("ts: {}".format(ts))
print()

print(dir(os.path))
print()





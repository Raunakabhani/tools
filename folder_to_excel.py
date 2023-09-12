import os
import pandas as pd

directory_path = "C:/Users/Admin/"
file_list = []
file_names = []

for root, dirs, files in os.walk(directory_path):
    for file in files:
        file_list.append(os.path.join(root, file))
        file_names.append(os.path.basename(file))

data = {"File Path": file_list, "File Name": file_names}
df = pd.DataFrame(data)
df.to_excel("file_list.xlsx", index=False)

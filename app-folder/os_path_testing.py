import os
import pandas as pd
import datetime

list1 = ["a", "b", "c"]
list2 = ["x", "y", "z"]
data = list(zip(list1, list2))

df = pd.DataFrame(data, columns=["col1", "col2"])

now = datetime.datetime.now()
folder_name = f"{now.month}-{now.day}-{now.year}-{now.hour}-{now.minute}-{now.second}/"

filepath = "C:/Users/Danie/OneDrive/Computer Science/billionaire_search_engine/files_not_yet_pushed_to_es/"
csvname = "test_csv.csv"
filename = os.path.join(filepath, csvname)

df.to_csv(filename)

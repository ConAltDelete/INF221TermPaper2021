import pandas as pd
import glob

path = '../../data/csv_files'
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=0, usecols=(0, 5))
    name = filename.rsplit("\\")[1].rsplit(".")[0]
    df.rename(columns={'random': name}, inplace=True)
    li.append(df)

frame = pd.concat(li, axis=1)
frame = pd.DataFrame.transpose(frame)
print(frame)
frame.to_csv('../../data/tables/table.csv')

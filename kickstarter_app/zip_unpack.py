import pandas as pd
import zipfile


zf = zipfile.ZipFile('ks-projects-201801.csv.zip')
df = pd.read_csv(zf.open('ks-projects-201801.csv.zip'))


print(df.head())

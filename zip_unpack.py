import pandas as pd
import zipfile

# Unzipping the File
zf = zipfile.ZipFile('ks-projects-201801.csv.zip')

# Declaring the unzipped file as a DataFrame
unzipped = pd.read_csv(zf.open('ks-projects-201801.csv'))

# Creating Working copy of our DataFrame
df = unzipped.copy()

x = 2
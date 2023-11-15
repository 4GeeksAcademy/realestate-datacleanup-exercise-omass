import pandas as pd
import numpy as np

data_frame = pd.read_csv('assets/real_estate.csv', sep=';')
df = pd.DataFrame(data_frame)

df.head()



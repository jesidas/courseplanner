import pandas as pd
import numpy as np

df = pd.read_csv('./FinalDataset.csv')



msk = np.random.rand(len(df)) <= 0.6

train = df[msk]
test = df[~msk]

np.savetxt(r'./train.txt', train.values, fmt='%s', delimiter=',')
np.savetxt(r'./test.txt', test.values, fmt='%s', delimiter=',')

import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

data_path = '/Users/anishmeka/Desktop/CS196/Team_21/Project6500.csv'
with open(data_path, 'rb') as f:
    contents = f.read()
train, test = train_test_split(contents, test_size=0.2, random_state=42, shuffle=True)
np.savetxt('/Users/anishmeka/Desktop/CS196/Team_21/train.txt', train, delimiter=',')
np.savetxt('/Users/anishmeka/Desktop/CS196/Team_21/test.txt', test, delimiter=',')

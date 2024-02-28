import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print("Исходный DataFrame:")
print(data.head())

categories = pd.unique(data['whoAmI'])
one_hot_encoded = pd.DataFrame(0, columns=categories, index=data.index)

for category in categories:
    one_hot_encoded[category] = (data['whoAmI'] == category).astype(int)

data = pd.concat([data, one_hot_encoded], axis=1).drop('whoAmI', axis=1)

print("\nDataFrame после one-hot кодировки:")
print(data.head())

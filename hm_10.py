import pandas as pd
import random

lst = ['robot'] * 5 + ['human'] * 5
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data['tmp'] = 1
data.set_index([data.index, 'whoAmI'], inplace=True)
data = data.unstack(level=1, fill_value=0) 
# data.columns = data.columns.droplevel()
data.columns.name = None
data.index.name = None
data.index += 1

print(data)
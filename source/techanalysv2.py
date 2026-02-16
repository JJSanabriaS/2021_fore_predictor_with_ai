from datetime import datetime
from forex_python.converter import get_rate
import pandas as pd
import numpy as np

#t = datetime(2001, 10, 18)  # the 18th of October, 2001
#print(get_rate("USD", "GBP", t))
#print(get_rate("GBP", "USD", t))
#print('verification  ',1 / get_rate("GBP", "USD", t))   # check
#289947382997
t = datetime(2006, 6, 26)  # June 26th, 2006
print(get_rate("GBP", "USD", t))

rng = pd.date_range('2021-02-24', '2021-03-28',freq='D')
df = pd.DataFrame({ 'Date': rng,'ratio':''})
print(df)
s=df. iloc[:, 0]
rat=[ ]
print('columna dias  ', s , type(s))
for i, v in s.items():
    print('value: ', v)
    print(get_rate("USD", "GBP", v))
    np.transpose(rat.append(get_rate("USD", "GBP", v)))


print(df)
print(rat)
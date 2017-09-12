# pandas pricing commands

import pandas as pd

s1 = pd.Series(range(1, 10, 2), name='s1')
s2 = pd.Series(range(2, 7), name='s2')

df = pd.concat([s1, s2], axis=1)
df['t1'] = df['s1'] > df['s2']


# compare two columns, return the greater
def t2(x):
    if x['s1'] > x['s2']:
        return x['s1']
    else:
        return x['s2']


# apply function to dataframe
# column-wise (axis=1)
# return answer to new column 't2'
df['t2'] = df.apply(t2, axis=1)

print(df.dtypes)
print(df)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('excel.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()

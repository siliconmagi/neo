# pandas commands

import pandas as pd

# create new dataframe
df = pd.DataFrame(
    {
        'A': range(0, 10),
        'B': range(10, 30, 2),
        'C': range(1, 11)
    }
)

# convert 'B' to string
# return slice of string beginning from index 1
df['trim'] = df['B'].astype(str).str[1:]

# concat columns
df['cat'] = df['A'].map(str) + df['B'].map(str)

# replace
rp = {10: "X", 12: "Y"}
rd = df.replace({"B": rp})

print(df)
print(rd)

# replace df inplace
df.replace({"C": rp}, inplace=True)
print(df)

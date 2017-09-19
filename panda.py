# pandas commands

import pandas as pd

df = pd.DataFrame(
    {
        'A': range(0, 10),
        'B': range(0, 20, 2),
        'C': range(1, 11)
    }
)

print(df)

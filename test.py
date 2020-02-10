import pandas as pd

df = pd.DataFrame({'x here': [1,20,270,500], 'y': [2,4,5,6]})

print(df.query("`x here` > 260"))

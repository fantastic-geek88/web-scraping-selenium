import pandas as pd

data = {"fruits": ["apple", "banana", "cherry"], "colors": ["red", "yellow", "purple"]}
df = pd.DataFrame(data)

df.head(2)
df.replace({"red": "green"}, inplace=True)

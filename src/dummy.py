import pandas as pd

data = {
    "fruits": ["apple", "banana", "cherry", "guava"],
    "colors": ["red", "yellow", "purple", "pink"],
}
df = pd.DataFrame(data)

df.head(2)
df.replace({"red": "green"}, inplace=True)

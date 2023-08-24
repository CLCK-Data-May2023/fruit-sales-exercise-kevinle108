import pandas as pd

data = {
    "Apples": [35, 41],
    "Bananas": [21, 34]
}

index = ["2017 Sales", "2018 Sales"]

df = pd.DataFrame(data, index)

# print(df)

df.to_csv('fruit.csv')
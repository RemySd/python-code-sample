import pandas as pd

df = pd.read_csv("sample.csv")

times = pd.to_datetime(df.timestamp)

df = df.groupby([times.dt.hour]).agg({'price':'sum','amount':'sum'})

df["vwap"] = df.price / df.amount

print(df)

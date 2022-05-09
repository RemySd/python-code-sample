import pandas as pd

df = pd.read_csv("sample.csv")

times = pd.to_datetime(df.timestamp)

print(times.dt.hour)

df = df.groupby([times.dt.hour]).agg({'price':'sum ','amount':'sum'})
print(df)
print("---")
print(df.price * df.amount)

df["vwap"] = df.price / df.amount

print("---", df)

#for index, row in df.iterrows():
#    print(pandas.to_datetime(row['timestamp']))

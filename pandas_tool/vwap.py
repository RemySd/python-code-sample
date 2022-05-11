import pandas as pd

pd.options.display.float_format = '{:.3f}'.format

df=pd.concat(map(pd.read_csv,['sample_2.csv','sample.csv']))

times = pd.to_datetime(df.timestamp)

df = df.groupby([times.dt.hour]).agg({
    'price': 'sum',
    'amount': 'sum'
})

print("---")

cumulativeVolume = df["amount"].sum()

df["vwap"] = df.price * df.amount / cumulativeVolume

print(df)

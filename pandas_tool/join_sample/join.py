import pandas as pd

df_brand = pd.read_csv("vehicle_brand.csv")
print(df_brand.head())
print("---")
df_model = pd.read_csv("vehicle_model.csv")
print(df_model.head())
print("---")




df = pd.merge(df_model, df_brand, left_on="brand_id", right_on="brand_id")

# df = pd.merge(df, df_name, on="brand_id")

print(df.head())

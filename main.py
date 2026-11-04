from src.data.clean import load_and_clean
data=load_and_clean("data/sample/train.csv")
print(data.shape)
print(f"\n{data.columns.tolist()}")
print(f"{data.groupby('store_nbr')['date'].min().head(10)}")
print(f"{data.groupby('store_nbr')['sales'].min().head(10)}")

print((data["sales"]==0).mean())
zero_share = (data["sales"]==0).groupby(data["family"]).mean()
print(zero_share.sort_values(ascending=False).head(10))
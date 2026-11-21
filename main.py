from src.data.clean import load_and_clean
data=load_and_clean("data/sample/train.csv")
print(data.shape)
print(f"\n{data.columns.tolist()}")
print(f"{data.groupby('store_nbr')['date'].min().head(10)}")
print(f"{data.groupby('store_nbr')['sales'].min().head(10)}")

print((data["sales"]==0).mean())
zero_share = (data["sales"]==0).groupby(data["family"]).mean()
print(zero_share.sort_values(ascending=False).head(10))


test_start = "2017-07-31"
train_Set = data[data["date"]<test_start]
test_Set = data[data["date"]>=test_start]

print(f"\n trainset:{train_Set.shape}")
print(f"\n testset:{test_Set.shape}")

print(len(train_Set))
print(len(test_Set))
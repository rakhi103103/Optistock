import pandas as pd

train=pd.read_csv("data/sample/train.csv")
print(train.head())
print("\n shape of data\n")
print(train.shape)
print("\n missing value table\n")
print(train.isnull().sum())
print("\n datatypes: \n")
print(train.dtypes)

#converting data from string to datetime 
train["date"] = pd.to_datetime(train["date"])
print(train.dtypes)
print("\n unique stores: \n")
print(train["store_nbr"].unique())
print("\ncount the unique stores: \n")
print(train["store_nbr"].nunique())
print("\n count the unique family product: \n")
print(train["family"].nunique())
print("\n earliest date in data: \n")
print(train["date"].min())
print("\nthe latest date in the data: \n")
print(train["date"].max())

#understanding sales column
print("\n smallest sales record: \n")
print(train["sales"].min())
print("\n highest sale record: \n")
print(train["sales"].max())
print("\navg sales: \n")
print(train["sales"].mean())
print("\nmedian of sales: \n")
print(train["sales"].median())
print("\n standard deviation of sales: \n")
print(train["sales"].std())

#extracting day of week from the date column
train["weekday"]= train["date"].dt.day_of_week

print(train["weekday"])

print("\n calculate each day average sales by day of week: \n")
print(train.groupby("weekday")["sales"].mean())

print("\n\n")
print(train["date"].iloc[0])
print(train["weekday"].iloc[0])

#extracting month from the date
train["month"]=train["date"].dt.month
print(train["month"])

print("\nmontly sales averages: \n")
print(train.groupby("month")["sales"].mean())

#sales report of each stores
avg_sales_per_store=train.groupby("store_nbr")["sales"].mean()
print(f"\n the avg sales per stores are: \n{avg_sales_per_store}")


#lowest and heighest sales
lowest_sales_per_stores = avg_sales_per_store.min()
highest_sales_per_stores = avg_sales_per_store.max()

print(f"\n lowest sales per store: \n{lowest_sales_per_stores}")
print(f"\n highest sales per store: \n{highest_sales_per_stores}")

#sorting the stores from highest to lowest
sorting_store=avg_sales_per_store.sort_values(ascending=False)
print(f"\n sorting values from highest to lowest: \n {sorting_store}")

stores = pd.read_csv("data/sample/stores.csv")
print(f"\n {stores.head()}")
print(f"\n {train.head()}")

#joining train dataset and stores dataset
merge_tb = pd.merge(train,stores,on="store_nbr")

store_44 = stores[stores["store_nbr"]== 44]
print(f"\n printing store_44: \n {store_44}")

store_52 = stores[stores["store_nbr"]==52]
print(f"\n printing store_52: \n {store_52}")

sales_city = merge_tb.groupby("city")["sales"].mean()
sales_State = merge_tb.groupby("state")["sales"].mean()
sales_type= merge_tb.groupby("type")["sales"].mean()

print(f"\n sales by city: \n {sales_city} \n sales by state: \n{sales_State}\nsales by type :\n{sales_type}")

counts_stores = stores["city"].value_counts()
print(f"\n{counts_stores}")

#to figure our what two stores manta has since shop52 is in manta city
mantas_stores = stores[stores["city"]=="Manta"]
print(f"\n Manta stores:\n {mantas_stores}")

filter_store52 = train[(train["store_nbr"]==52) & (train["sales"]>0)].min()
print(f"\n filtering dtore 52 data:\n {filter_store52}")

before_open=train[(train["store_nbr"]==52)&(train["date"]<="2017-04-20")]
print(f"\n printing data of store 52 dated 2017-04-20: \n{before_open}")

after_open = train[(train["store_nbr"]==52)&(train["date"]>="2017-04-20")]
print(f"result of store 52 after the date 2017-04-20: \n{after_open} ")
mean_after = after_open["sales"].mean()
print(f"\n this is the result after the average sales after opening the shop: \n{mean_after}")
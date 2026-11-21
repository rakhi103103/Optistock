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

#checking max sales before 2017-04-20 i store 52
sales_before = train[(train["date"]<"2017-04-20")&(train["store_nbr"]==52)]
print(f"\nsales before 2017-04-20: \n{sales_before}")
max_sales = sales_before["sales"].max()
print(f"\n {max_sales}\n")

#keeping ponly the sales >0 from the other store
sales_row = train[train["sales"]>0]
print(f"\nsales_row:\n{sales_row}")
first_Sales = sales_row.groupby("store_nbr")["date"].min()
print(f"\n sales date:\n{first_Sales}")
print(f"\n{len(first_Sales)}")
print(f"\n{train.shape}")

first_table = first_Sales.reset_index()
first_table.columns = ["store_nbr", "first_sale_date"]
print(first_table.head())
cleaned = pd.merge(train, first_table, on="store_nbr")
print(cleaned.shape)

before = len(cleaned)
cleaned = cleaned[cleaned["date"] >= cleaned["first_sale_date"]]
after = len(cleaned)
print(before, after, before - after)

print(f"\n{cleaned.groupby('store_nbr')['date'].min().head(10)}")
print(f"\n{cleaned[cleaned['store_nbr'] == 52]['date'].min()}")

#exploring oil csv
oil = pd.read_csv("data/sample/oil.csv")
print(f"head: {oil.head(10)}")
print(f"\n shape of column and rows: {oil.shape}")
print(f"\n datatypes in this oil dataset: \n {oil.dtypes}")


#converting date column from string to datetime
oil["date"] = pd.to_datetime(oil["date"])
print(f"\n searching null values: \n{oil.isnull().sum()}")

print(f"\n oil date earlier: {oil['date'].min()}")
print(f"\n oil date latest: {oil['date'].max()}")
print(f"\n train date earlier: {train['date'].min()}")
print(f"\n train date latest: {train['date'].max()}")

total_days = (train["date"].max()-train["date"].min()).days+1
print(f"\n total days: \n {total_days}")

print(f"\n {oil[oil['dcoilwtico'].isnull()]}")

#holiday_csv
holiday = pd.read_csv("data/sample/holidays_events.csv")
print(f"head: {holiday.head(10)}")
print(f"\n shape of column and rows: {holiday.shape}")
print(f"\n datatypes in this holiday dataset: \n {holiday.dtypes}")


#converting date column from string to datetime
holiday["date"] = pd.to_datetime(holiday["date"])
print(f"\n searching null values: \n{holiday.isnull().sum()}")

print(f"\n{holiday['date'].min(), holiday['date'].max()}")
print(f"\n{holiday['type'].value_counts()}")
print(f"\n{holiday['locale'].value_counts()}")
print(f"\n{holiday[holiday['transferred'] == True].head(10)}")

print(f"\n\n\noil details: {oil.head()}")
oil_null = oil[oil["dcoilwtico"].isnull()]
print(f"\n {oil_null}")

names = oil_null["date"].dt.day_name().value_counts()
print(f"\n names of the day oil is null: \n{names}")

#how many oil rows comes after 2017-08-15
oil_after = oil[oil["date"]>"2017-08-15"]
print(f"\n {oil_after}")

dates_range = pd.date_range(start="2013-01-01", end="2017-08-15")
dates_missing = dates_range.difference(train["date"])

#what are the top 5 family product by shares of zero sales row
print(train.head())
# 1. Zero share by family 
zero_share = (cleaned['sales'] == 0).groupby(cleaned['family']).mean()
print(f"\ntop 5 families by zero-sales share: \n{zero_share.sort_values(ascending=False).head(5)}")

# 2. Transferred holidays
print(f"\nrows with transferred = True: \n{holiday['transferred'].sum()}")
print(f"\nTransfer rows: \n{holiday[holiday['type'] == 'Transfer']}")

# 3. Bridge, Work Day, Event
print(f"\nBridge rows: \n{holiday[holiday['type'] == 'Bridge']}")
print(f"\nWork Day rows: \n{holiday[holiday['type'] == 'Work Day']}")
print(f"\ntop Event descriptions: \n{holiday[holiday['type'] == 'Event']['description'].value_counts().head(10)}")

# 4. Do holiday places match store places?
local_names = holiday[holiday['locale'] == 'Local']['locale_name']
regional_names = holiday[holiday['locale'] == 'Regional']['locale_name']
print(f"\nlocal holiday places not in store cities: \n{local_names[~local_names.isin(stores['city'])].unique()}")
print(f"\nregional holiday places not in store states: \n{regional_names[~regional_names.isin(stores['state'])].unique()}")

# 5. Transactions
transactions = pd.read_csv("data/sample/transactions.csv")
transactions['date'] = pd.to_datetime(transactions['date'])
print(f"\ntransactions head: \n{transactions.head()}")
print(f"\ntransactions shape: \n{transactions.shape}")
print(f"\ntransactions datatypes: \n{transactions.dtypes}")
print(f"\ntransactions missing values: \n{transactions.isnull().sum()}")
print(f"\ntransactions date range: \n{transactions['date'].min()} to {transactions['date'].max()}")
print(f"\nunique stores in transactions: \n{transactions['store_nbr'].nunique()}")
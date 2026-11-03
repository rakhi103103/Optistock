import pandas as pd

def load_and_clean(path):
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])

    #find each store first sales date
    sales = df[df["sales"]>0]
    first_Sales = sales.groupby("store_nbr")["date"].min()

    #turn it into a table with reset index and rename the columns
    first_table = first_Sales.reset_index()
    first_table.columns = ["store_nbr","first_Sales_date"]

    #merge it into in df
    cleaned = pd.merge(df,first_table,on="store_nbr")

    #keep only rows on and after the store first day sales
    cleaned = cleaned[cleaned["date"]>=cleaned["first_Sales_date"]] 

    # drop the  first_Sales_date column as i dont need later
    cleaned=cleaned.drop(columns=["first_Sales_date"])

 


    
    return cleaned
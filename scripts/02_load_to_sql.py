import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("data/nifty_raw.csv", header=[0, 1], index_col=0, skiprows=[2])

df.columns = df.columns.get_level_values(0)
df.index.name = "Date"

engine = create_engine("sqlite:///db/nifty.db")

df.to_sql("nifty_daily", engine, if_exists="replace", index=True)

print(df.head())
print("Data loaded into SQL successfully")
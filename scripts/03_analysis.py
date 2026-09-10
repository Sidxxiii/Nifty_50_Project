import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///db/nifty.db")

query = """
SELECT
    strftime('%Y-%m', Date) AS month,
    ROUND(AVG(Close), 2) AS avg_close
FROM nifty_daily
GROUP BY month
ORDER BY month
"""

with engine.connect() as conn:
    result = pd.read_sql(text(query), conn)

print(result)
query2 = """
SELECT
    Date,
    Close,
    ROUND((Close - Open) / Open * 100, 2) AS pct_change
FROM nifty_daily
ORDER BY pct_change DESC
LIMIT 5
"""

query3 = """
SELECT
    Date,
    Close,
    Volume
FROM nifty_daily
ORDER BY Volume DESC
LIMIT 5
"""

with engine.connect() as conn:
    best_days = pd.read_sql(text(query2), conn)
    top_volume = pd.read_sql(text(query3), conn)

print("\nTop 5 best days (by % change):")
print(best_days)

print("\nTop 5 highest volume days:")
print(top_volume)
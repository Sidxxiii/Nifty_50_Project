import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///db/nifty.db")

query1 = """
SELECT
    strftime('%Y-%m', Date) AS month,
    ROUND(AVG(Close), 2) AS avg_close
FROM nifty_daily
GROUP BY month
ORDER BY month
"""

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

query4 = """
SELECT * FROM nifty_daily
ORDER BY Date
"""

with engine.connect() as conn:
    monthly_avg = pd.read_sql(text(query1), conn)
    best_days = pd.read_sql(text(query2), conn)
    top_volume = pd.read_sql(text(query3), conn)
    raw_data = pd.read_sql(text(query4), conn)

with pd.ExcelWriter("output/nifty_dashboard.xlsx", engine="xlsxwriter") as writer:
    raw_data.to_excel(writer, sheet_name="Raw Data", index=False)
    monthly_avg.to_excel(writer, sheet_name="Monthly Avg", index=False)
    best_days.to_excel(writer, sheet_name="Best Days", index=False)
    top_volume.to_excel(writer, sheet_name="Top Volume", index=False)

print("Excel dashboard created successfully at output/nifty_dashboard.xlsx")
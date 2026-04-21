import sqlite3

def insert_data(df):
    conn = sqlite3.connect("solar.db")
    df.to_sql("solar_data", conn, if_exists="append", index=False)
    conn.close()

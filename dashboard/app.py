import streamlit as st
import pandas as pd
import sqlite3
import time

st.title("Solar Dashboard")

placeholder = st.empty()

while True:
    conn = sqlite3.connect("solar.db")
    try:
        df = pd.read_sql("SELECT * FROM solar_data", conn)
    except:
        df = pd.DataFrame()

    with placeholder.container():
        if df.empty:
            st.warning("No data yet...")
        else:
            st.metric("Records", len(df))
            st.line_chart(df["power_kw"])
            st.line_chart(df["temperature_c"])
            st.dataframe(df.tail(5))

    time.sleep(5)

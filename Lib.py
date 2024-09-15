import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime
import jdatetime
from jdatetime import datetime as jalali_datetime
st.set_page_config(page_title="dashboard", page_icon="📝", layout="wide")

menu = st.sidebar.radio(
    "منو",
    ["صفحه اصلی", "کتابخانه","تجهیزات", "آموزش", "لوازم یدکی"]
)

conn = sqlite3.connect('Library.db')

query = "SELECT * FROM Library"
df = pd.read_sql_query(query, conn)
query1 = "SELECT * FROM Library where NameEn  "
df1 = pd.read_sql_query(query, conn)
conn.close()

if menu == "صفحه اصلی":
    st.header("در حال راه اندازی")
    # محتوای صفحه اصلی

if menu == "کتابخانه":
    st.header("کتابخانه")
    col1, col2, col3 = st.columns(3)
    with col1:
        BNameEn_filter = col1.text_input("Equipment Name")
    with col2:
        code_filter = col2.text_input("کد کتاب")
    with col3:
        BNameFa_filter = col3.text_input("نام دستگاه فارسی")    
    df_display = df.copy()
   
    if BNameFa_filter:
        df_display = df_display[df_display['NameFa'].str.contains(BNameFa_filter)]
    if code_filter:
        df_display = df_display[df_display['Code'].str.contains(code_filter)]
    if BNameEn_filter:
        df_display = df_display[df_display['NameEn'].str.contains(BNameEn_filter)]


    selected_columns = df_display.loc[:, ["Code", "NameEn","NameFa"]]
    st.write(selected_columns)

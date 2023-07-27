from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


# 设置页面布局
st.set_page_config(page_title="My Streamlit App", layout="wide")

# 设置侧边栏宽度
st.markdown(
    f"""
    <style>
    .sidebar .sidebar-content {{
        width: 300px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# 设置主体宽度
st.markdown(
    f"""
    <style>
    .main .block-container {{
        max-width: 1200px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# 在侧边栏中添加组件
st.sidebar.header("侧边栏")
st.sidebar.slider("选择一个值", 0, 100)

# 在主体中添加组件
st.header("主体")
st.write("这是一个 Streamlit 应用程序。")


col1, col2, col3 = st.columns(3)


if st.button('打开新页面'):
    url = "<a href='/mypages/chat.py'>new page</a>"
    st.write(url,unsafe_allow_html=True)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

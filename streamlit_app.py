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

hide_menu_style = """
        <style>
        #stSidebarNav {display: none;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# 在主体中添加组件
st.header("主体")
st.write("这是一个 Streamlit 应用程序。")

# 在侧边栏中添加组件
st.sidebar.header("侧边栏")
st.sidebar.slider("选择一个值", 0, 100)

st.sidebar.header("栏位2")
with st.sidebar: 
    url = "<a href='/chat' target='_blank'>Chat</a>"
    st.write(url,unsafe_allow_html=True)

    

col1, col2, col3 = st.columns(3)




with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

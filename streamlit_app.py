from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st




# 设置页面布局
st.set_page_config(page_title="My Streamlit App", layout="wide")


# 隐藏streamlit自带的sidebarnav并设置背景和字体颜色
hide_menu_style = """
        <style>
            div[data-testid='stSidebarNav'] 
            {
              display: none;
            }
            
            section[data-testid='stSidebar'] 
            {
               background-color:purple;
               color:#ffffff;
            }
            .mymenu:link,
            .mymenu:hover,
            .mymenu:active,
            .mymenu:visited
            {
                 color:#fff;
                 text-decoration:none;
            }
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# 在主体中添加组件
st.header("主体")
st.write("这是一个 Streamlit 应用程序。")

# 设置Logo
st.sidebar.header("")
with st.sidebar:
    img="<img width='100' height='80' src='https://static.streamlit.io/examples/cat.jpg'/>"
    st.write(img,unsafe_allow_html=True)
    
# 在侧边栏中添加组件
st.sidebar.header("GPT Practice")
with st.sidebar: 
            
    url = "<a class='mymenu' href='/chat' target='_self'>OpenAI Queries</a>"
    st.write(url,unsafe_allow_html=True)
    
    url = "<a class='mymenu' href='/chat' target='_self'>Chat</a>"
    st.write(url,unsafe_allow_html=True)
    
    url = "<a class='mymenu' href='/chat' target='_self'>Add Document</a>"
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

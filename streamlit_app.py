from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


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

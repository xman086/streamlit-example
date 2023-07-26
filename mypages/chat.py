from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


col1, col2 = st.beta_columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)

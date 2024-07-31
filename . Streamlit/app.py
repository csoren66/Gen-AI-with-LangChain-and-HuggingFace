import streamlit as st
import numpy as np
import pandas as pd

st.title("hello Chandan")
st.write("This is simple text")

#create dataframe
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40] 
})
#display dataframe
st.write("here is the dataframe")
st.write(df)

#create line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart()

###run streamlit app.py

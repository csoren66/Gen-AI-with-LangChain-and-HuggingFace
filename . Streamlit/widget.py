import streamlit as st
import pandas as pd
st.title("Streamlit text input")

name=st.text_input("Enter your name")

age = st.slider("How old are you?", 0, 130, 25)
st.write("I am ", age, "years old")

options = ["Phyton", "java", "C++", "Javascript"]
choice =st.selectbox("Select your language", options)
st.write("You selected:", choice)

if name:
  st.write(f"hello", {name})

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "San Francisco", "Los Angeles"]
}

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)
st.write(df)

uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df)

import streamlit as st
import pandas as pd
import sklearn.datasets import load_iris
from sklearn esmemble import RandomForestClassifier

@st.cache
def load_data():
  iris=load_iris()
  df.pd.DataFrame(iris.data, columns=iris.feature_names)
  df['species']=iris.target_names

df, target_name=load_data()

model=RandomForestClassifier()
model.fit(df.iloc[:,:-1], df['species'])

st.slider.title("input Feature")
sepal_length=st.sidebar.slider("Sepal length", float(df['sepal length (cm)'].min(), float(df['sepal length (cm)'].max())
sepal_width=st.sidebar.slider("Sepal width", float(df['sepal width (cm)'].min(), float(df['sepal width (cm)'].max())
petal_length=st.sidebar.slider("Petal length", float(df['petal length (cm)'].min(), float(df['petal length (cm)'].max())
petal_width=st.sidebar.slider(("Petal width", float(df['petal width (cm)'].min(), float(df['petal width (cm)'].max())

input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction =model.predict(input_data)
prediction_species = target_names[predictio[0]]

st.write("Predictions")
st.write(f"The predicted species is: {predicted_species}")                  
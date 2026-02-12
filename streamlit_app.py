import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

file = st.file_uploader("Upload a file")

df = pd.read_csv(file)
st.dataframe(df)

product_name = df.groupby('Product Name')['Quantity'].agg(['count', 'sum', 'mean', 'min', 'max']).reset_index()
print(product_name)

top_10 = product_name.nlargest(10, 'sum')
print(top_10)

st.bar_chart(top_10, x='Product Name', y='sum')
st.line_chart(top_10, x='Product Name', y='sum')
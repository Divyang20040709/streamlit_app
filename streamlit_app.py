import streamlit as st
import pandas as pd 

file = st.file_uploader("Upload a file")

if file is not None:
    df = pd.read_csv(file)
    st.write(df)

    product_name = df.groupby('Product Name')['Quantity'].agg(['count', 'sum', 'mean', 'min', 'max']).reset_index()
    st.write(product_name)

    top_10 = product_name.nlargest(10, 'sum')
    st.write(top_10)

else:
    st.write("Please upload a CSV file.")



st.bar_chart(top_10, x='Product Name', y='sum')
st.line_chart(top_10, x='Product Name', y='sum')

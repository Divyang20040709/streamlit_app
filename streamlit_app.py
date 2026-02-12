import streamlit as st
import pandas as pd

file = st.file_uploader("Upload CSV", type=["csv"])

if file is not None:
    df = pd.read_csv(file)
    st.DataFrame(df)
    
    product_name = df.groupby('Product Name')['Quantity'] \
                     .agg(['count', 'sum', 'mean', 'min', 'max']) \
                     .reset_index()

    top_10 = product_name.sort_values('sum', ascending=False).head(10)

    st.subheader("Top 10 Products by Quantity Sold")
    st.bar_chart(top_10, x='Product Name', y='sum')
    st.line_chart(top_10, x='Product Name', y='sum')

else:
    st.write("Please upload a CSV file.")


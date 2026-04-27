import pandas as pd
import streamlit as st

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRrghz-wZKTsB_EuLUhGGZxXN57bZMyC-0_hOULrMAHi50q9qpESkv1FkWBOhHKg2w-cfCO6X7TI731/pub?output=csv"

df = pd.read_csv(url)

st.title("Monitoramento IoT")

st.line_chart(df[['temperatura', 'umidade']])
st.dataframe(df)

import streamlit as st
import pandas as pd
import plotly_express as px 

df = pd.read_csv("vehicles_us.csv")

st.header("Analisis exploratorio")

if st.button("Construir Histograma"):
    st.write("Histograma de la columna 'odometer'")
    if 'odometer' in df.columns:
        fig = px.histogram(df, x='odometer', title='Histograma de odometro')
    else:
        fig = px.histogram(df, x=df.columns[0], title=f'Histograma de {df.columns[0]}')
    st.plotly_chart(fig, width='stretch')

#boton para grafico de dispersion

if st.button('scatter plot'):
    st.write("Scatter price vs odom")
    if 'odometer'in df.columns and 'price' in df.columns:
        fig2 = px.scatter(df, x='odometer', y='price', title='precio vs odo')
        st.plotly_chart(fig2, width='stretch')
    else:
        st.write("las columnas no estan disponibles")

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

car_data = pd.read_csv("vehicles_us.csv")

st.header("Análisis interactivo de anuncios de venta de coches")

if st.button("Construir histograma"):
    st.write("Creación de un histograma de la columna *odometer*")

    fig = go.Figure(data=[go.Histogram(x=car_data["odometer"])])
    fig.update_layout(title_text="Distribución del odómetro")
    st.plotly_chart(fig, use_container_width=True)

if st.button("Construir gráfico de dispersión"):
    st.write("Creación de un gráfico de dispersión entre *odometer* y *price*")

    fig2 = px.scatter(car_data, x="odometer", y="price", title="Precio vs Kilometraje")
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Opciones con casillas de verificación")

if st.checkbox("Mostrar histograma (price)"):
    fig3 = px.histogram(car_data, x="price", nbins=50, title="Distribución de precios")
    st.plotly_chart(fig3, use_container_width=True)

if st.checkbox("Mostrar dispersión (año vs precio)"):
    fig4 = px.scatter(car_data, x="model_year", y="price", title="Precio vs Año del modelo")
    st.plotly_chart(fig4, use_container_width=True)

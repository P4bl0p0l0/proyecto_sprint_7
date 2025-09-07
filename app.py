import pandas as pd
import plotly.express as px
import streamlit as st

# --- Load data ---
car_data = pd.read_csv("vehicles_us.csv")

# --- Page title ---
st.title("🚗 Dashboard interactivo de ventas de coches")

# --- Sidebar controls ---
st.sidebar.header("Controles de la app")

# Filtro de precio
price_max = st.sidebar.slider("Precio máximo", 
                              int(car_data["price"].min()), 
                              int(car_data["price"].max()), 
                              50000)

filtered_data = car_data[car_data["price"] <= price_max]

# Elección de variables para scatter
x_var = st.sidebar.selectbox("Variable X", filtered_data.columns)
y_var = st.sidebar.selectbox("Variable Y", filtered_data.columns)

# --- Main area ---
st.header("Visualizaciones")

if st.sidebar.button("Construir histograma de precios"):
    fig = px.histogram(filtered_data, x="price", nbins=50, title="Distribución de precios (filtrada)")
    st.plotly_chart(fig, use_container_width=True)

if st.sidebar.button("Construir gráfico de dispersión personalizado"):
    fig = px.scatter(filtered_data, x=x_var, y=y_var, title=f"{y_var} vs {x_var}")
    st.plotly_chart(fig, use_container_width=True)

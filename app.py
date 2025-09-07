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

# Selección múltiple de variables para gráficos
numeric_columns = filtered_data.select_dtypes(include=["int64", "float64"]).columns.tolist()

x_vars = st.sidebar.multiselect("Selecciona variable(s) X", numeric_columns, default=["odometer"])
y_vars = st.sidebar.multiselect("Selecciona variable(s) Y", numeric_columns, default=["price"])

# --- Main area ---
st.header("📊 Visualizaciones")

# --- Botón para histograma ---
if st.sidebar.button("Construir histograma de precios"):
    st.write("Histograma interactivo de precios filtrados")
    fig = px.histogram(filtered_data, x="price", nbins=50, title="Distribución de precios (filtrada)")
    st.plotly_chart(fig, use_container_width=True)

# --- Botón para scatter personalizado ---
if st.sidebar.button("Construir gráfico(s) de dispersión personalizado"):
    if x_vars and y_vars:
        for x in x_vars:
            for y in y_vars:
                if x != y:  # evita scatter de la misma variable
                    fig = px.scatter(filtered_data, x=x, y=y, title=f"{y} vs {x}")
                    st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Selecciona al menos una variable X y una Y")

# --- Checkboxes extras ---
st.subheader("Opciones adicionales")

if st.checkbox("Mostrar histograma de odómetro"):
    fig2 = px.histogram(filtered_data, x="odometer", nbins=50, title="Distribución del odómetro")
    st.plotly_chart(fig2, use_container_width=True)

if st.checkbox("Mostrar dispersión año vs precio"):
    fig3 = px.scatter(filtered_data, x="model_year", y="price", title="Precio vs Año del modelo")
    st.plotly_chart(fig3, use_container_width=True)


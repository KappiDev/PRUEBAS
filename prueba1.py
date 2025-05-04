import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts

data = [
    [1, "Pan blanco", "Alimentos", 1.50, 25],
    [2, "Jugo de naranja", "Bebidas", 2.20, 15],
    [3, "Papel higiénico", "Higiene", 3.80, 40],
    [4, "Galletas Oreo", "Snacks", 1.75, 30],
    [5, "Shampoo", "Higiene", 5.50, 20],
    [6, "Leche entera", "Lácteos", 1.90, 18],
    [7, "Arroz 1kg", "Alimentos", 2.50, 50],
    [8, "Agua embotellada", "Bebidas", 1.00, 60],
]

df = pd.DataFrame(data, columns=["Indice", "Producto", "Categoria", "Precio", "Stock"])
df.to_csv("Productos.csv", index=False)

st.title("Inventario de productos")

productos = pd.read_csv("Productos.csv")

nombres = productos["Producto"].tolist()
stocks = productos["Stock"].tolist()

color_opcion = st.selectbox("Selecciona el color de la gráfica:", {
    "Azul": "#3498db",
    "Rojo": "#e74c3c",
    "Verde": "#2ecc71",
    "Naranja": "#e67e22",
    "Púrpura": "#9b59b6"
})

opciones = {
    "title": {"text": "Stock de productos"},
    "tooltip": {},
    "xAxis": {"data": nombres},
    "yAxis": {},
    "series": [{
        "name": "Stock",
        "type": "bar",
        "data": stocks,
        "itemStyle": {"color": color_opcion}
    }],
}

st_echarts(options=opciones, height="400px", width="700px")

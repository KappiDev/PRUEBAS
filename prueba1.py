import streamlit as st
import pandas as pd

data = [
    [1, "Pan blanco", "Alimentos", 1.50, 25],
    [2, "Jugo de naranja", "Bebidas", 2.20, 15],
    [3, "Papel higiénico", "Higiene", 3.80, 40],
    [4, "Galletas Oreo", "Snacks", 1.75, 30],
    [5, "Shampoo", "Higiene", 5.50, 20],
    [6, "Leche entera", "Lácteos", 1.90, 18],
    [7, "Arroz 1kg", "Alimentos", 2.50, 50],
    [8, "Agua embotellada", "Bebidas", 1.00, 60],]

archivo = pd.DataFrame(data,columns=["Indice", "Producto","Categoria", "Precio", "Stock"])
archivo.to_csv("Productos.csv", index=False)

st_echarts(
    options="Productos.csv", height="400px",
)

st.title("Hola mundo")

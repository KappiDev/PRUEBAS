import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts

datos = [
    ["Usuario1","Contraseña1"],
    ["Usuario2","Contraseña2"],
    ["Usuario3","Contraseña3"],
]

df = pd.DataFrame(datos, columns=["Usuario","Contraseña"])
df.to_csv("datos.csv", index=False)
informacion = pd.read_csv("datos.csv")
st.title("Iniciar Sesion")

usuario = st.text_input("Usuario")
contraseña = st.text_input("Contraseña", type="password")

if st.button("Iniciar Sesion"):
    if any((informacion["Usuario"] == usuario) & (informacion["Contraseña"] == contraseña)):
        st.success("Inicio de sesion exitoso")
    else:
        st.error("Inicio de sesion fallido")

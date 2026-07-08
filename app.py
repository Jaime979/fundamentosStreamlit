import streamlit as st

st.title("Aplicación de Fundamento Streamlist")

st.sidebar.image("logo.png")

st.sidebar.title("parametros")


monto = st.number_input("ingrese el monto de su prestamo")

interes = st.number_input("ingrese el interes")

tiempo_meses st.number_input("ingrese el tiempo en meses")

resultado = monto*interes*(tiempo_meses/12)

st.write("El resultado es:",resultado)

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv") # Leitura do arquivo

model = LinearRegression() #create model with linear regression

x = df[["diameter"]] #define column diameter
y = df[["price"]] #define column price

model.fit(x,y) # training


st.title("Prevendo O Valor de uma pizza") #create one interface
st.divider()

diameter = st.number_input("Digite o tamanho do diametro da pizza: ")

if diameter:
    predict_price  = model.predict([[diameter]])[0][0] # predict value
    st.write(f"O valor da pizza com diamentro de {diameter:.2f} é R$: {predict_price:.2f}")
    st.balloons()
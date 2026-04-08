import streamlit as st
import plotly.express as px
import pandas as pd
st.title("In search for happiness")
x=st.selectbox("Select the data for X-axis",("GDP","Happiness","Generosity"))
y=st.selectbox("Select the data for Y-axis",("GDP","Happiness","Generosity"))
df=pd.read_csv("happy.csv")
match x:
    case "GDP":
        x_array=df["gdp"]
    case "Happiness":
        x_array=df["happiness"]
    case "Generosity":
        x_array=df["generosity"]
match y:
    case "GDP":
        y_array=df["gdp"]
    case "Happiness":
        y_array=df["happiness"]
    case "Generosity":
        y_array=df["generosity"]
figure=px.scatter(x=x_array,y=y_array,labels={"x":x,"y":y})
st.plotly_chart(figure)
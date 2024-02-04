import pandas as pd
import statsmodels.formula.api as smf
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

data = pd.read_csv('cleaned.csv', delimiter=',')

st.header('Ramka danych')

st.dataframe(data)

st.header('Rozkład zmiennych')

option = st.selectbox('Wybierz zmienną', ('price', 'carat', 'clarity', 'color', 'cut', 'depth', 'table'))

st.plotly_chart(px.histogram(data, x=option, histfunc='count').update_layout(bargap=0.2))

st.header('Zależność ceny od zmiennych')

option2 = st.selectbox('Wybierz zmienną zależną', ('carat', 'clarity', 'color', 'cut', 'x_dimension', 'y_dimension', 'z_dimension', 'depth', 'table'))

st.plotly_chart(px.scatter(data, x = option2, y = 'price'))

st.header('Regresja')

option3 = st.selectbox('Wybierz zmienną zależną do regresji', ('carat', 'x_dimension', 'y_dimension', 'z_dimension', 'clarity', 'color', 'cut', 'depth', 'table'))
#option3 = 'carat'

model = smf.ols(f'price ~ {option3}', data=data).fit()
data['fitted'] = model.fittedvalues

st.code(model.summary())

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=data[option3], y=data["price"], name=f"{option3} vs price", mode="markers"))
fig.add_trace(go.Scatter(
    x=data[option3], y=data["fitted"], name="regresja"))
fig.update_layout(title=f"{option3} vs price", xaxis_title=option3,
    yaxis_title="price")

st.plotly_chart(fig)



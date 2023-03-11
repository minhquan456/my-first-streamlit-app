import streamlit as st
import sklearn
import plotly

st.title('Giải phương trình bậc nhất')

number1 = st.number_input('Tham số a')
number2 = st.number_input('Tham số b')

if st.button('Giải'):
  st.write('phương trình có 1 nghiệm', -number2/number1)

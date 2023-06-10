import streamlit as st

num1 = st.number_input('Insert a number', key=1)
num2 = st.number_input('Insert a number', key =2)

def add_two(num_1,num_2):
    result = num_1+num_2
    return result

total = add_two(num1,num2)

if st.button('The current number is '):
    st.write(total)
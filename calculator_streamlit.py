import streamlit as st
st.title('Math calculator')

num1 = st.number_input('Insert a number', key=1)
num2 = st.number_input('Insert a number', key =2)

def add_two(num_1,num_2):
    result_add = num_1+num_2
    return result_add



if st.button('The sum is '):
    total_sum = add_two(num1,num2)
    st.write(total_sum)

def sub_two(num_1, num_2):
    result_sub = num1-num2
    return result_sub

if st.button('The substraction of numbers is '):
    total_sub = sub_two(num1,num2)
    st.write(total_sub)

def multiply_two(num_1, num_2):
    result_multiply = num1*num2
    return result_multiply

if st.button('The multiply is '):
    total_multiply = multiply_two(num1,num2)
    st.write(total_multiply)  

def div_two(num_1, num_2):
    result_div = num1/num2 if num2 else 0
    return result_div

if st.button('The division of numbers is '):
        total_div = div_two(num1,num2)
        st.write(total_div)
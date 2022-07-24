import streamlit as st

string = "Divider"
st.set_page_config(page_title=string)

st.write("""
# Two Numbler Divison App

This app divides two number
""")


st.header('User Input Parameters')

def user_input_features():
    n1 = st.number_input("Enter Number-1")
    n2 = st.number_input("Enter Number-2")

    return n1, n2

n1, n2 = user_input_features()

if st.button('Calculate'):
    st.write(n1/n2)

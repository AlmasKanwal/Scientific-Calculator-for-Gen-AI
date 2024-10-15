import streamlit as st
import math

# Set page configuration
st.set_page_config(page_title="Scientific Calculator", layout="centered")

# Style for the calculator
st.markdown("""
    <style>
    .calculator {
        width: 350px;
        padding: 20px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        margin: auto;
    }
    .calculator input {
        width: 100%;
        height: 60px;
        background-color: #e0f7fa;
        border: none;
        text-align: right;
        font-size: 24px;
        color: #00796b;
        border-radius: 5px;
        padding: 10px;
        margin-bottom: 20px;
        box-sizing: border-box;
    }
    .calculator button {
        width: 22%;
        height: 50px;
        font-size: 18px;
        margin: 5px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
        color: white;
        background-color: #00796b;
        transition: background-color 0.3s ease;
    }
    .calculator button:hover {
        background-color: #004d40;
    }
    .special {
        background-color: #ff4081 !important; /* Hot Pink */
    }
    .special:hover {
        background-color: #f50057 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Variables to hold calculator state
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Display input field
st.markdown(f"""
    <div class="calculator">
        <input type="text" value="{st.session_state.expression}" disabled>
    </div>
""", unsafe_allow_html=True)

# Functions for calculator operations
def add_to_expression(value):
    st.session_state.expression += str(value)

def clear_expression():
    st.session_state.expression = ""

def backspace():
    st.session_state.expression = st.session_state.expression[:-1]

def calculate_expression():
    try:
        st.session_state.expression = str(eval(st.session_state.expression))
    except:
        st.session_state.expression = "Error"

# Calculator buttons
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("C", key="clear", on_click=clear_expression):
        pass
with col2:
    if st.button("←", key="backspace", on_click=backspace):
        pass
with col3:
    if st.button("%", key="percent", on_click=lambda: add_to_expression("%")):
        pass
with col4:
    if st.button("÷", key="divide", on_click=lambda: add_to_expression("/")):
        pass

col5, col6, col7, col8 = st.columns(4)
with col5:
    if st.button("7", key="seven", on_click=lambda: add_to_expression("7")):
        pass
with col6:
    if st.button("8", key="eight", on_click=lambda: add_to_expression("8")):
        pass
with col7:
    if st.button("9", key="nine", on_click=lambda: add_to_expression("9")):
        pass
with col8:
    if st.button("×", key="multiply", on_click=lambda: add_to_expression("*")):
        pass

col9, col10, col11, col12 = st.columns(4)
with col9:
    if st.button("4", key="four", on_click=lambda: add_to_expression("4")):
        pass
with col10:
    if st.button("5", key="five", on_click=lambda: add_to_expression("5")):
        pass
with col11:
    if st.button("6", key="six", on_click=lambda: add_to_expression("6")):
        pass
with col12:
    if st.button("-", key="minus", on_click=lambda: add_to_expression("-")):
        pass

col13, col14, col15, col16 = st.columns(4)
with col13:
    if st.button("1", key="one", on_click=lambda: add_to_expression("1")):
        pass
with col14:
    if st.button("2", key="two", on_click=lambda: add_to_expression("2")):
        pass
with col15:
    if st.button("3", key="three", on_click=lambda: add_to_expression("3")):
        pass
with col16:
    if st.button("+", key="plus", on_click=lambda: add_to_expression("+")):
        pass

col17, col18, col19 = st.columns([2, 1, 1])
with col17:
    if st.button("0", key="zero", on_click=lambda: add_to_expression("0")):
        pass
with col18:
    if st.button(".", key="dot", on_click=lambda: add_to_expression(".")):
        pass
with col19:
    if st.button("=", key="equals", on_click=calculate_expression):
        pass


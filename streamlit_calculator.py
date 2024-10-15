import streamlit as st
import math

# Title and heading
st.title("Pak Angel Cohort 2")
st.write("<h3 style='text-align: center; color: teal;'>Simple Calculator</h3>", unsafe_allow_html=True)

# Create a display for the calculator
calc_display = st.text_input("", value="", placeholder="0", key="calc_display")

# Functions for operations
def add_to_display(value):
    st.session_state.calc_display += str(value)

def clear_display():
    st.session_state.calc_display = ""

def backspace():
    st.session_state.calc_display = st.session_state.calc_display[:-1]

def calculate():
    try:
        st.session_state.calc_display = str(eval(st.session_state.calc_display))
    except:
        st.session_state.calc_display = "Error"

def sqrt():
    try:
        st.session_state.calc_display = str(math.sqrt(eval(st.session_state.calc_display)))
    except:
        st.session_state.calc_display = "Error"

def square():
    try:
        st.session_state.calc_display = str(eval(st.session_state.calc_display) ** 2)
    except:
        st.session_state.calc_display = "Error"

def percent():
    try:
        st.session_state.calc_display = str(eval(st.session_state.calc_display) / 100)
    except:
        st.session_state.calc_display = "Error"

# Create the calculator buttons layout
col1, col2, col3, col4, col5 = st.columns(5)

# First row (C, backspace, %, ÷, sqrt)
with col1: st.button("C", on_click=clear_display)
with col2: st.button("←", on_click=backspace)
with col3: st.button("%", on_click=percent)
with col4: st.button("÷", on_click=lambda: add_to_display("/"))
with col5: st.button("√", on_click=sqrt)

# Second row (7, 8, 9, ×, x²)
col1, col2, col3, col4, col5 = st.columns(5)
with col1: st.button("7", on_click=lambda: add_to_display("7"))
with col2: st.button("8", on_click=lambda: add_to_display("8"))
with col3: st.button("9", on_click=lambda: add_to_display("9"))
with col4: st.button("×", on_click=lambda: add_to_display("*"))
with col5: st.button("x²", on_click=square)

# Third row (4, 5, 6, −)
col1, col2, col3, col4, col5 = st.columns(5)
with col1: st.button("4", on_click=lambda: add_to_display("4"))
with col2: st.button("5", on_click=lambda: add_to_display("5"))
with col3: st.button("6", on_click=lambda: add_to_display("6"))
with col4: st.button("−", on_click=lambda: add_to_display("-"))

# Fourth row (1, 2, 3, +)
col1, col2, col3, col4, col5 = st.columns(5)
with col1: st.button("1", on_click=lambda: add_to_display("1"))
with col2: st.button("2", on_click=lambda: add_to_display("2"))
with col3: st.button("3", on_click=lambda: add_to_display("3"))
with col4: st.button("+", on_click=lambda: add_to_display("+"))

# Fifth row (0, ., =)
col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])
with col1: st.button("0", on_click=lambda: add_to_display("0"))
with col2: st.button(".", on_click=lambda: add_to_display("."))
with col3: st.button("=", on_click=calculate)

# Footer
st.write("<p style='text-align: center; color: hotpink;'>Made by Almas Kanwal</p>", unsafe_allow_html=True)

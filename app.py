import streamlit as st
import math

# Function to evaluate expressions
def evaluate_expression(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return 'Error'

# Streamlit app layout
def main():
    st.markdown("<h1 style='text-align: center; color: #0ABAB5;'>Scientific Calculator</h1>", unsafe_allow_html=True)

    # Expression input
    expression = st.text_input("Enter expression", "")
    
    if 'result' not in st.session_state:
        st.session_state.result = ""

    # Result display
    result_display = st.text_input("Result", st.session_state.result, disabled=True)

    # Buttons layout
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button('7', key='7', help="Add 7 to the expression"):
            expression += '7'
    with col2:
        if st.button('8', key='8', help="Add 8 to the expression"):
            expression += '8'
    with col3:
        if st.button('9', key='9', help="Add 9 to the expression"):
            expression += '9'
    with col4:
        if st.button('/', key='/', help="Divide the expression"):
            expression += '/'
    with col5:
        if st.button('sqrt', key='sqrt', help="Square root of the expression"):
            expression = 'math.sqrt(' + expression + ')'

    with col1:
        if st.button('4', key='4', help="Add 4 to the expression"):
            expression += '4'
    with col2:
        if st.button('5', key='5', help="Add 5 to the expression"):
            expression += '5'
    with col3:
        if st.button('6', key='6', help="Add 6 to the expression"):
            expression += '6'
    with col4:
        if st.button('*', key='*', help="Multiply the expression"):
            expression += '*'
    with col5:
        if st.button('pow', key='pow', help="Power of the expression"):
            expression = 'math.pow(' + expression + ')'

    with col1:
        if st.button('1', key='1', help="Add 1 to the expression"):
            expression += '1'
    with col2:
        if st.button('2', key='2', help="Add 2 to the expression"):
            expression += '2'
    with col3:
        if st.button('3', key='3', help="Add 3 to the expression"):
            expression += '3'
    with col4:
        if st.button('-', key='-', help="Subtract from the expression"):
            expression += '-'
    with col5:
        if st.button('log', key='log', help="Logarithm of the expression"):
            expression = 'math.log(' + expression + ')'

    with col1:
        if st.button('0', key='0', help="Add 0 to the expression"):
            expression += '0'
    with col2:
        if st.button('.', key='.', help="Add a decimal point to the expression"):
            expression += '.'
    with col3:
        if st.button('=', key='=', help="Evaluate the expression"):
            st.session_state.result = evaluate_expression(expression)
            expression = ""
    with col4:
        if st.button('+', key='+', help="Add to the expression"):
            expression += '+'
    with col5:
        if st.button('C', key='C', help="Clear the expression"):
            expression = ""
            st.session_state.result = ""

    # Display the current expression and result
    st.text_input("Current Expression", expression, disabled=True)
    
    # Footer with custom message
    st.markdown("<p style='text-align: center; color: #FF69B4;'>Made by Almas Kanwal</p>", unsafe_allow_html=True)

# Run the app
if __name__ == '__main__':
    main()

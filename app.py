import streamlit as st
import math

# Function to perform the calculation
def calculate(expression):
    try:
        # Evaluates the entered expression
        result = eval(expression)
        return str(result)
    except Exception as e:
        return 'Error'

# Streamlit app layout
def main():
    # Title and styling
    st.markdown("<h1 style='text-align: center; color: #0ABAB5;'>Scientific Calculator</h1>", unsafe_allow_html=True)

    # Input text box for expression
    input_text = st.text_input("Enter expression", '')

    # Buttons layout (styled)
    button_style = """
        <style>
        .stButton button {
            background-color: #FF69B4; /* Hot Pink */
            color: white;
            border-radius: 10px;
            border: none;
            padding: 10px 20px;
            margin: 5px;
        }
        .stButton button:hover {
            background-color: #0ABAB5; /* Tiffany Blue */
            color: white;
        }
        </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)

    # Create buttons
    button_labels = [
        '7', '8', '9', '/', 'sqrt',
        '4', '5', '6', '*', 'pow',
        '1', '2', '3', '-', 'log',
        '0', '.', '=', '+', 'C'
    ]

    cols = st.columns(5)
    for label in button_labels:
        with cols[button_labels.index(label) % 5]:
            if st.button(label):
                if label == '=':
                    output_text = calculate(input_text)
                    st.text_input("Result", output_text, disabled=True)
                elif label == 'C':
                    input_text = ''
                    st.text_input("Result", '', disabled=True)
                elif label == 'sqrt':
                    input_text = str(math.sqrt(float(input_text)))
                elif label == 'pow':
                    input_text = str(math.pow(float(input_text), 2))
                else:
                    input_text += label
                # Update the input field
                st.text_input("Enter expression", input_text, key='input')

    # Footer
    st.markdown("<p style='text-align: center; color: #FF69B4;'>Made by Almas Kanwal</p>", unsafe_allow_html=True)

# Run the app
if __name__ == '__main__':
    main()

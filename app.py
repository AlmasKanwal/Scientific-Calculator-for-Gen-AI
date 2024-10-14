import streamlit as st
import math

# Function to perform the calculation
def calculate(expression):
    try:
        # Evaluates the entered expression
        result = eval(expression)
        return str(result)
    except Exception:
        return 'Error'

# Streamlit app layout
def main():
    # Title and styling
    st.markdown("<h1 style='text-align: center; color: #0ABAB5;'>Scientific Calculator</h1>", unsafe_allow_html=True)

    # Initial session state for expression
    if 'expression' not in st.session_state:
        st.session_state.expression = ''

    # Input text box for expression
    expression = st.text_input("Expression", st.session_state.expression, placeholder="Enter your expression here")

    # Buttons layout (styled)
    button_style = """
        <style>
        .stButton button {
            background-color: #FF69B4; /* Hot Pink */
            color: white;
            border-radius: 10px;
            border: none;
            padding: 15px 20px;
            margin: 5px;
            font-size: 20px;  /* Increase font size */
            width: 60px; /* Set a fixed width for better alignment */
        }
        .stButton button:hover {
            background-color: #0ABAB5; /* Tiffany Blue */
            color: white;
        }
        </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)

    # Create buttons with visible mathematical operators
    button_labels = [
        '7', '8', '9', ' / ', ' sqrt ',
        '4', '5', '6', ' * ', ' pow ',
        '1', '2', '3', ' - ', ' log ',
        '0', '.', ' = ', ' + ', ' C '
    ]

    # Output text box for result
    output_text = st.empty()  # Placeholder for result display

    # Create buttons in a responsive layout
    cols = st.columns(5)

    for label in button_labels:
        with cols[button_labels.index(label) % 5]:
            if st.button(label):
                if label == ' = ':
                    st.session_state.expression = expression  # Update expression in session state
                    result = calculate(expression)
                    output_text.text(result)
                elif label == ' C ':
                    st.session_state.expression = ''
                    output_text.text('')
                elif label == ' sqrt ':
                    try:
                        result = math.sqrt(float(expression))
                        st.session_state.expression = str(result)
                    except ValueError:
                        st.session_state.expression = 'Error'
                    output_text.text(st.session_state.expression)
                elif label == ' pow ':
                    try:
                        result = math.pow(float(expression), 2)
                        st.session_state.expression = str(result)
                    except ValueError:
                        st.session_state.expression = 'Error'
                    output_text.text(st.session_state.expression)
                elif label == ' log ':
                    try:
                        result = math.log(float(expression))
                        st.session_state.expression = str(result)
                    except ValueError:
                        st.session_state.expression = 'Error'
                    output_text.text(st.session_state.expression)
                else:
                    st.session_state.expression += label.strip()  # Add operator to expression

    # Display the result in a separate line
    st.markdown("<h3 style='text-align: center; color: #0ABAB5;'>Result:</h3>", unsafe_allow_html=True)
    result_display = st.empty()  # To display the result below the expression

    # Update the result display based on the session state
    result_display.text(st.session_state.expression)

    # Footer
    st.markdown("<p style='text-align: center; color: #FF69B4;'>Made by Almas Kanwal</p>", unsafe_allow_html=True)

# Run the app
if __name__ == '__main__':
    main()

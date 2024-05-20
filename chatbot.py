import streamlit as st
import pandas as pd

# Function to read and display CSV file
def read_csv_file(file):
    df = pd.read_csv(file)
    return df

# Streamlit app
def main():
    st.title("Anti Green Wash Chatbot 🤖🌱")

    # test input for interaction
    user_input = st.text_input("Ask me something:")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        st.write("### Analyzing uploaded file...")
        df = read_csv_file(uploaded_file)
        st.write("### Preview of the DataFrame:")
        st.write(df)

        # Additional analysis or operations can be added here
        # For example:
        # st.write("### Summary Statistics:")
        # st.write(df.describe())

    # Respond to user input
    if user_input:
        st.write(f"You asked: '{user_input}'")
        # Additional logic based on user input can be added here

if __name__ == "__main__":
    main()

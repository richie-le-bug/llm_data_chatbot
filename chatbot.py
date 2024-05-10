import pandas as pd
import streamlit as st
import plotly.graph_objs as go

# run this command on terminal -> streamlit run chatbot.py   

# Sample data for visualization
data = pd.read_csv("weatherHistory.csv")

def help_():
    st.write("Type one of the following commands: 'quit', 'info', 'temperature'")

def info_data(data):
    st.info(data.info())
    st.write(data)

def visualize_temp(data):
    # Create a line chart
    fig = go.Figure(data=go.Scatter(x=data.index, y=data['Temperature'], mode='lines'))
    fig.update_layout(title='Temperature Data Visualization', xaxis_title='Index', yaxis_title='Temperature')

    # Display the plot
    st.plotly_chart(fig)

def main():
    st.title("Crappy Data Visualization Chatbot🤓")

    # Get user input
    user_input = st.text_input("Type 'help' for assistance:")

    if 'help' in user_input:
        # print the keywords
        help_()
    elif 'quit' in user_input:
        st.write("Goodbye!")
        st.stop()
    elif 'temperature' in user_input:
        visualize_temp(data)
    elif 'info' in user_input:
        info_data(data)

if __name__ == '__main__':
    main()


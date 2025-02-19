import streamlit as st
import pandas as pd
import os

# Set the directory for data files
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

# Function to load data
def load_data(file_name):
    file_path = os.path.join(DATA_DIR, file_name)
    return pd.read_csv(file_path)

# Main function to run the Streamlit app
def main():
    st.title("Dashboard App")

    # File selection
    files = os.listdir(DATA_DIR)
    selected_file = st.selectbox("Select a file:", files)

    if selected_file:
        data = load_data(selected_file)
        st.write(data)

        # Plot selection
        plot_options = data.columns.tolist()
        selected_plot = st.selectbox("Select a plot:", plot_options)

        if selected_plot:
            st.line_chart(data[selected_plot])

if __name__ == "__main__":
    main()
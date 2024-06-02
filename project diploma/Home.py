import streamlit as st
import pandas as pd
import os

# Function to load and save dataset
def load_and_save_dataset(file_path, file_uploader_key):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    uploaded_file = st.file_uploader("Upload Video Game Sales Dataset", type="csv", key=file_uploader_key)
    if uploaded_file:
        dataset = pd.read_csv(uploaded_file)
        dataset.to_csv(file_path, index=False)
        return dataset
    return None

# Function to preprocess the dataset
def preprocess_dataset(data):
    if data is not None:
        # Drop any unnamed columns
        data = data.loc[:, ~data.columns.str.contains('Unnamed')]

        # Convert data types
        data['Year'] = pd.to_numeric(data['Year'], errors='coerce')  # Handle non-numeric years
        data.dropna(subset=['Year'], inplace=True)  # Drop rows where year is NaN

        # Sales data conversion (ensure they are floats)
        cols = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
        data[cols] = data[cols].apply(pd.to_numeric, errors='coerce')
        data.dropna(subset=cols, inplace=True)  # Drop rows with NaN in these columns
        
        return data
    return pd.DataFrame()

# Set page title and icon
st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)

# Main content
st.title("Welcome to the Video Game Sales Dashboard! 🎮")
st.markdown("""
    This dashboard allows you to upload and analyze historical sales data of video games.
    ### Instructions
    1. Upload the video game sales dataset below.
        - Ensure the file is in CSV format with the following column headers: Rank, Name, Platform, Year, Genre, Publisher, 
        NA_Sales, EU_Sales, JP_Sales, Other_Sales, and Global_Sales.
    2. After uploading, you can view the processed data and some basic analytics on sales by region and platform.
""")

# Load or upload dataset
dataset_path = "video_game_sales_dataset.csv"
dataset = load_and_save_dataset(dataset_path, "upload_video_game_sales")

if dataset is not None:
    st.success("Dataset uploaded successfully!")
    st.write("**Dataset Preview:**")
    st.dataframe(dataset.head(), width=700)

    # Preprocess the dataset
    preprocessed_data = preprocess_dataset(dataset)

    # Show preprocessed data
    st.subheader("Preprocessed Data")
    st.write("**Overview of Preprocessed Dataset:**")
    st.dataframe(preprocessed_data.head(), width=700)

    # Optionally, display more detailed analytics or visualizations here
else:
    st.warning("Please upload a dataset to proceed.")


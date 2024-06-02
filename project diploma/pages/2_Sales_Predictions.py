import streamlit as st
import numpy as np
import pickle
import matplotlib.pyplot as plt
import pandas as pd
import consts.consts as cs

# Set page title and icon
st.set_page_config(
    page_title="Sales Predictions",
    page_icon="📊",
)
st.sidebar.header("Sales Prediction Analytics")

st.title("Video Game Sales Prediction")

st.write(
    """
         This tool predicts the global sales of video games based on various inputs including platform, genre, and publisher,
         along with regional sales data. Input the details of the game to estimate its global market performance.
         """
)

# Load the model and historical data
def load_model():
    with open("Sales_Prediction_LinearRegresssion.pkl", "rb") as f:
        model = pickle.load(f)
    return model


def load_games_data():
    return pd.read_csv("video_game_sales_dataset.csv")


model = load_model()
sales_games_data = load_games_data()

sales_games_data["Platform"] = (
    sales_games_data["Platform"].astype(str).str.strip().str.upper()
)
sales_games_data["Genre"] = (
    sales_games_data["Genre"].astype(str).str.strip().str.upper()
)
sales_games_data["Publisher"] = (
    sales_games_data["Publisher"].astype(str).str.strip().str.upper()
)

with st.form("prediction_form"):
    st.write("Please enter the following inputs to predict sales:")

    selected_platform = st.selectbox(
        "Select Platform", options=list(cs.platformMapped_reversed.keys())
    )
    selected_genre = st.selectbox(
        "Select Genre", options=list(cs.genreMapped_reversed.keys())
    )
    selected_publisher = st.selectbox(
        "Select Publisher", options=list(cs.publisherMapped_reversed.keys())
    )

    rank = st.number_input("Rank", min_value=1, max_value=10000, step=1, value=1)
    year = st.number_input("Year", min_value=1980, max_value=2025, step=1, value=2021)
    na_sales = st.number_input("NA Sales", min_value=0.0, max_value=50.0, value=11.35)
    eu_sales = st.number_input("EU Sales", min_value=0.0, max_value=50.0, value=11.98)
    jp_sales = st.number_input("JP Sales", min_value=0.0, max_value=50.0, value=11.19)
    other_sales = st.number_input(
        "Other Sales", min_value=0.0, max_value=50.0, value=11.98
    )

    submitted = st.form_submit_button("Predict Sales")
    if submitted:
        platform = cs.platformMapped_reversed[selected_platform]
        genre = cs.genreMapped_reversed[selected_genre]
        publisher = cs.publisherMapped_reversed[selected_publisher]
        features = np.array(
            [
                [
                    rank,
                    platform,
                    year,
                    genre,
                    publisher,
                    na_sales,
                    eu_sales,
                    jp_sales,
                    other_sales,
                ]
            ]
        )
        prediction = model.predict(features)

        st.write(
            f"The predicted global sales are: {prediction[0][0]:.2f} million units"
        )

        filtered_data = sales_games_data[
            (sales_games_data["Platform"] == selected_platform.upper())
            & (sales_games_data["Genre"] == selected_genre.upper())
            & (sales_games_data["Publisher"] == selected_publisher.upper())
        ]

        if filtered_data.empty:
            st.write("No historical data available for the selected combination.")
        else:
            # Group by year and calculate total sales for each year
            sales_by_year = filtered_data.groupby("Year")["Global_Sales"].sum()

            # Prepare features for prediction
            features = np.array(
                [
                    [
                        rank,
                        platform,
                        year,
                        genre,
                        publisher,
                        na_sales,
                        eu_sales,
                        jp_sales,
                        other_sales,
                    ]
                ]
            )
            predicted_sales = model.predict(features)[0]

            # Plotting historical and predicted sales
            plt.figure(figsize=(10, 5))
            plt.plot(
                sales_by_year.index,
                sales_by_year,
                marker="o",
                linestyle="-",
                label="Historical Sales",
            )
            plt.scatter([year], [predicted_sales], color="red", label="Predicted Sales")
            plt.title(
                f"Sales Trends for {selected_platform}, {selected_genre}, {selected_publisher}"
            )
            plt.xlabel("Year")
            plt.ylabel("Global Sales (Millions)")
            plt.grid(True)
            plt.legend()
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(plt)


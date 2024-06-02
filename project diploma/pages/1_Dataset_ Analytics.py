import streamlit as st
import pandas as pd
import altair as alt
import os

# Set page title and icon
st.set_page_config(
    page_title="Dataset Analytics",
    page_icon="📈",
)

st.sidebar.header("Dataset Analytics")

# Main content
st.title("Dataset Analytics 📈")

# Load the preprocessed dataset and stop if it doesn't exist
dataset_path = "video_game_sales_dataset.csv"
if not os.path.exists(dataset_path):
    st.error("Dataset not uploaded. Please make sure the dataset file is in the correct location.")
    st.stop()

data = pd.read_csv(dataset_path)

# Create containers for different types of analytics
sales_trend_con = st.container()
total_sales_con = st.container()
total_rev_con = st.container()
top_sales_con = st.container()
top_rev_con = st.container()
top_cat_con = st.container()
cat_rank_con = st.container()

with sales_trend_con:
    st.subheader("Sales Trends Over Time")
    st.markdown("""
    This line chart displays the annual global sales from the dataset, showcasing trends over the years. 
                It helps identify peak sales periods and can be used to forecast future market behavior based on past performance.
    """)
    data['Year'] = pd.to_numeric(data['Year'], errors='coerce')
    yearly_sales = data.groupby('Year')['Global_Sales'].sum().reset_index()
    line_chart = alt.Chart(yearly_sales).mark_line().encode(
        x='Year:O',
        y='Global_Sales:Q',
        tooltip=['Year', 'Global_Sales']
    ).properties(title="Yearly Global Sales Trends")
    st.altair_chart(line_chart, use_container_width=True)

with total_sales_con:
    st.subheader("Total Global Sales by Game")
    st.markdown("""
    This bar chart ranks the top 10 games by their total global sales. It highlights which titles have achieved the greatest commercial success, 
                offering insights into consumer preferences and successful game franchises.
    """)
    total_sales = data.groupby('Name')['Global_Sales'].sum().reset_index().sort_values(by='Global_Sales', ascending=False).head(10)
    bar_chart = alt.Chart(total_sales).mark_bar().encode(
        x=alt.X('Name:N', sort='-y'),
        y='Global_Sales:Q',
        tooltip=['Name', 'Global_Sales']
    ).properties(title="Top 10 Games by Global Sales")
    st.altair_chart(bar_chart, use_container_width=True)

with total_rev_con:
    st.subheader("Total Revenue by Publisher")
    st.markdown("""
    TThis visualization presents the top 10 publishers by total revenue generated from global sales. 
                It indicates which publishers dominate the market and how their strategies might be impacting overall revenue.
    """)
    revenue_by_publisher = data.groupby('Publisher')['Global_Sales'].sum().reset_index().sort_values(by='Global_Sales', ascending=False).head(10)
    bar_chart = alt.Chart(revenue_by_publisher).mark_bar().encode(
        x='Publisher:N',
        y='Global_Sales:Q',
        tooltip=['Publisher', 'Global_Sales']
    ).properties(title="Top 10 Publishers by Global Sales")
    st.altair_chart(bar_chart, use_container_width=True)

with top_sales_con:
    st.subheader("Top Selling Platforms")
    st.markdown("""
    This chart shows the total sales for the top 10 gaming platforms, illustrating which platforms have the highest market penetration and consumer adoption. 
                It helps stakeholders understand platform performance in a competitive context.
    """)
    sales_by_platform = data.groupby('Platform')['Global_Sales'].sum().reset_index().sort_values(by='Global_Sales', ascending=False).head(10)
    platform_chart = alt.Chart(sales_by_platform).mark_bar().encode(
        x='Platform:N',
        y='Global_Sales:Q',
        tooltip=['Platform', 'Global_Sales']
    ).properties(title="Top Selling Platforms")
    st.altair_chart(platform_chart, use_container_width=True)

with top_rev_con:
    st.subheader("Top Revenue Generating Games")
    st.markdown("""
    This bar chart displays the top 10 games generating the highest revenue worldwide. 
                It not only reflects the market acceptance but also the economic impact of these titles on the gaming industry.
    """)
    top_revenue_games = data.groupby('Name')['Global_Sales'].sum().reset_index().sort_values(by='Global_Sales', ascending=False).head(10)
    game_chart = alt.Chart(top_revenue_games).mark_bar().encode(
        x='Name:N',
        y='Global_Sales:Q',
        tooltip=['Name', 'Global_Sales']
    ).properties(title="Top Revenue Generating Games")
    st.altair_chart(game_chart, use_container_width=True)

with top_cat_con:
    st.subheader("Sales by Genre")
    st.markdown("""
    Explore the popularity and financial success of different game genres with this bar chart. 
                It categorizes global sales by genre, providing a clear view of which types of games are currently leading the market and which are niche.
    """)
    sales_by_genre = data.groupby('Genre')['Global_Sales'].sum().reset_index().sort_values(by='Global_Sales', ascending=False)
    genre_chart = alt.Chart(sales_by_genre).mark_bar().encode(
        x='Genre:N',
        y='Global_Sales:Q',
        tooltip=['Genre', 'Global_Sales']
    ).properties(title="Sales by Genre")
    st.altair_chart(genre_chart, use_container_width=True)

with cat_rank_con:
    st.subheader("Ranking by Genre")
    st.markdown("""
    This ranking chart sorts game genres by total sales, revealing which genres are most lucrative and popular. 
                This analysis can guide publishers and developers in targeting their efforts and investments towards the most profitable genres.
    """)
    genre_chart = alt.Chart(sales_by_genre).mark_bar().encode(
        x=alt.X('Genre:N', sort='-y'),
        y='Global_Sales:Q',
        tooltip=['Genre', 'Global_Sales']
    ).properties(title="Ranking Genres by Sales")
    st.altair_chart(genre_chart, use_container_width=True)
import streamlit as st

# Set page title and icon
st.set_page_config(
    page_title="Features",
    page_icon="⚙️",
)
st.sidebar.header("Features")

st.title("The Features ⚙️")

st.markdown("""
    ### Features
    1. Sales Trends Over Time: Visualizes annual global sales to highlight trends, peaks, and declines, helping users understand market dynamics over the years. This is accomplished through a line chart that aggregates sales by year.
    2. Total Global Sales by Game: Displays a bar chart ranking the top 10 games by their total global sales, offering insights into the most commercially successful titles.
    3. Total Revenue by Publisher: Showcases the top publishers by revenue through a bar chart, highlighting which publishers dominate the market.
    4. Top Selling Platforms: Illustrates which gaming platforms have sold the most through a bar chart, useful for gauging platform market penetration.
    5. Top Revenue Generating Games: Focuses on individual games that have generated significant revenue, useful for understanding which titles have had substantial economic impacts.
    6. Sales by Genre: Analyzes the financial success of different game genres, providing a clear view of market preferences.
    7. Ranking by Genre: Sorts game genres by total sales to identify the most lucrative and popular categories.
            
    8. Input Form: Users can input game details such as platform, genre, publisher, and regional sales. These inputs are used to predict global sales based on a machine learning model.
    9. Sales Prediction Output: After entering the details, the predicted sales figures are displayed, providing users with an estimate of potential global sales.
    10. Historical Comparison: The application compares the predicted sales with historical data to give context to the predictions.
            
    11. Dynamic Filters: Users can filter the data by platform, year, genre, and publisher using sidebar widgets.
    12. Filtered Data Display: Displays the data filtered according to the selected criteria.
    13. ANOVA Test: Conducts an ANOVA test to determine if differences in global sales across selected platforms are statistically significant, which helps in understanding the impact of platform choice on sales.
    14. Sales Distribution Visualization: If multiple platforms are selected, a boxplot shows the distribution of sales across these platforms to visually compare performance.
    15. Correlation Heatmap: Shows a heatmap of the correlation between different regional sales figures and global sales, aiding in identifying how different markets relate to each other.       
""")
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from statsmodels.formula.api import ols
import statsmodels.api as sm


# Set page configuration
st.set_page_config(page_title="Video Game Sales Filtering", page_icon="📕")
st.title("Video Game Sales Filtering 📕")

# Load the preprocessed dataset and stop if it doesn't exist
dataset_path = "video_game_sales_dataset.csv"
if not os.path.exists(dataset_path):
    st.error("Dataset not uploaded. Please make sure the dataset file is in the correct location.")
    st.stop()

data = pd.read_csv(dataset_path)

# Filters Sidebar
st.sidebar.header("Filters")
selected_platform = st.sidebar.multiselect('Select Platform', options=data['Platform'].unique())
selected_year = st.sidebar.multiselect('Select Year', options=sorted(data['Year'].dropna().unique()))
selected_genre = st.sidebar.multiselect('Select Genre', options=data['Genre'].unique())
selected_publisher = st.sidebar.multiselect('Select Publisher', options=data['Publisher'].unique())

# Apply filters
filtered_data = data.copy()
if selected_platform:
    filtered_data = filtered_data[filtered_data['Platform'].isin(selected_platform)]
if selected_year:
    filtered_data = filtered_data[filtered_data['Year'].isin(selected_year)]
if selected_genre:
    filtered_data = filtered_data[filtered_data['Genre'].isin(selected_genre)]
if selected_publisher:
    filtered_data = filtered_data[filtered_data['Publisher'].isin(selected_publisher)]

# Display filtered data
st.header("Filtered Data")
st.write(filtered_data)

# Perform ANOVA if there are at least two platforms selected
if len(selected_platform) > 1:
    st.header("ANOVA Test on Global Sales Across Platforms")
    model = ols('Global_Sales ~ C(Platform)', data=filtered_data).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    st.write("ANOVA table", anova_table)
    p_value = anova_table['PR(>F)'][0]
    if p_value < 0.05:
        st.write(f"The p-value is {p_value}, which is less than 0.05, suggesting that the differences in sales across platforms are statistically significant. This implies that platform choice does have a significant impact on sales figures.")
    else:
        st.write(f"The p-value is {p_value}, which is greater than 0.05, suggesting that any differences in sales across platforms are not statistically significant and may be due to random variation.")
    # Optionally, show a boxplot for visual comparison
    st.header("Sales Distribution by Platform")
    fig, ax = plt.subplots()
    sns.boxplot(x='Platform', y='Global_Sales', data=filtered_data, ax=ax)
    st.pyplot(fig)
else:
    st.warning("Please select at least two platforms to perform ANOVA.")

# Correlation Heatmap
st.header("Correlation Heatmap")
st.markdown("The section below displays the dataset filtered according to your selections in the sidebar. This allows you to examine the data more closely and make specific observations about trends, sales, and market performance based on your chosen filters.")
if not filtered_data.empty:
    corr_data = filtered_data[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']]
    corr_matrix = corr_data.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm')
    st.pyplot(plt)


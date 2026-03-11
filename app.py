import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Netflix Analytics Dashboard", layout="wide")

# Load dataset
df = pd.read_csv("../data/silver/netflix_cleaned.csv")

# Title
st.title(" Netflix Data Analytics Dashboard")

# ===============================
# KPI METRICS
# ===============================

total_titles = len(df)
movies = len(df[df["type"] == "Movie"])
tv_shows = len(df[df["type"] == "TV Show"])
countries = df["country"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Titles", total_titles)
col2.metric("Movies", movies)
col3.metric("TV Shows", tv_shows)
col4.metric("Countries", countries)

st.divider()

# ===============================
# SIDEBAR FILTERS
# ===============================

st.sidebar.header("Filters")

selected_type = st.sidebar.selectbox(
    "Select Content Type",
    ["All"] + list(df["type"].unique())
)

selected_country = st.sidebar.selectbox(
    "Select Country",
    ["All"] + sorted(df["country"].dropna().unique())
)

# Apply filters
filtered_df = df.copy()

if selected_type != "All":
    filtered_df = filtered_df[filtered_df["type"] == selected_type]

if selected_country != "All":
    filtered_df = filtered_df[filtered_df["country"] == selected_country]

# ===============================
# CHARTS
# ===============================

col1, col2 = st.columns(2)

# Movies vs TV Shows
type_counts = filtered_df["type"].value_counts().reset_index()
type_counts.columns = ["Type", "Count"]

fig1 = px.pie(type_counts, names="Type", values="Count", title="Movies vs TV Shows")
col1.plotly_chart(fig1, use_container_width=True)

# Release year trend
year_data = filtered_df["release_year"].value_counts().sort_index().reset_index()
year_data.columns = ["Year", "Count"]

fig2 = px.line(year_data, x="Year", y="Count", title="Content Release Trend")
col2.plotly_chart(fig2, use_container_width=True)

# ===============================
# TOP COUNTRIES
# ===============================

country_data = filtered_df["country"].value_counts().head(10).reset_index()
country_data.columns = ["Country", "Count"]

fig3 = px.bar(
    country_data,
    x="Country",
    y="Count",
    title="Top 10 Countries Producing Netflix Content"
)

st.plotly_chart(fig3, use_container_width=True)

# ===============================
# DATA EXPLORER
# ===============================

st.subheader(" Dataset Explorer")

search = st.text_input("Search by Title")

if search:
    filtered_df = filtered_df[
        filtered_df["title"].str.contains(search, case=False, na=False)
    ]

st.dataframe(filtered_df)
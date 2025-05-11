import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from cleaning import *
from llama_chat import ask_llama

st.set_page_config(page_title="Data Cleaning Assistant", layout="wide")

st.sidebar.title("Navigation")
if st.sidebar.button("🏠 Home"):
    st.switch_page("Home.py")
if st.sidebar.button("💬 Chat Assistant"):
    st.switch_page("pages/ChatWithLlama.py")

theme = st.session_state.get("theme", "Light")

uploaded_file = st.session_state.get("uploaded_file", None)
if not uploaded_file:
    st.warning("Please upload a CSV file on the Home page.")
    st.stop()

if "raw_data" not in st.session_state:
    try:
        st.session_state.raw_data = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()

if "cleaned_data" not in st.session_state:
    st.session_state.cleaned_data = st.session_state.raw_data.copy()

df = st.session_state.cleaned_data

st.title("Data Cleaning and Analysis")
st.subheader("Raw Data Preview")
st.dataframe(df.head())

st.subheader("Initial Data Analysis")
col_types = detect_column_types(df)
missing = detect_missing_values(df)
outliers = detect_outliers(df)
duplicates = detect_duplicates(df)

st.markdown("### Column Types")
st.json(col_types)

st.markdown("### Missing Values")
st.json(missing)

st.markdown("### Outliers (Z-score > 3)")
st.json(outliers)

st.markdown(f"### Duplicate Rows: {duplicates}")

st.divider()
st.header("📊 Data Visualization")

numeric_cols = df.select_dtypes(include='number').columns.tolist()
selected_col = st.selectbox("Select a column to visualize", numeric_cols)

chart_type = st.radio("Select Chart Type", ["Histogram", "Boxplot"], horizontal=True)

fig, ax = plt.subplots()
if chart_type == "Histogram":
    sns.histplot(df[selected_col].dropna(), kde=True, ax=ax)
else:
    sns.boxplot(x=df[selected_col], ax=ax)
st.pyplot(fig)

st.divider()
st.header("Data Cleaning Options")

with st.form("cleaning_form"):
    if missing:
        col_to_clean = st.selectbox("Select column with missing values", list(missing.keys()))
        strategy = st.radio("Handle missing values using:",
                            ("mean", "median", "mode", "drop"), horizontal=True)
    else:
        col_to_clean = None
        strategy = None
        st.info("No missing values detected.")

    remove_dup = st.checkbox("Remove duplicate rows")
    submitted = st.form_submit_button("Clean the Data")

if submitted:
    if col_to_clean:
        df = fill_missing_values(df, strategy, col_to_clean)
    if remove_dup:
        df = remove_duplicates(df)

    if df.empty:
        st.error("Resulting DataFrame is empty!")
    else:
        st.session_state.cleaned_data = df
        st.success("Data cleaned successfully.")
        st.subheader("Cleaned Data Preview")
        st.dataframe(df.head())

st.divider()
st.download_button("⬇ Download Cleaned CSV",
                   data=st.session_state.cleaned_data.to_csv(index=False),
                   file_name="cleaned_data.csv",
                   mime="text/csv")
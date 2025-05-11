import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Cleaning Assistant", layout="wide")

st.title("Welcome to the Data Cleaning Assistant using NLP")

st.markdown("""
Make your data analysis smoother with this powerful yet easy-to-use tool.

Key features include:
- Automatic column type detection  
- Identification and treatment of missing values  
- Detection of outliers and duplicate records  
- AI powered chat for data-related queries  
- Quick visual summaries and charts
""")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    st.session_state["uploaded_file"] = uploaded_file
    try:
        df = pd.read_csv(uploaded_file)
        st.session_state["raw_data"] = df
        st.session_state["cleaned_data"] = df.copy()
        st.success("File uploaded successfully!")
    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()

    st.markdown("### Next Steps:")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Proceed to Data Cleaning"):
            st.switch_page("pages/DataCleanerApp.py")
    with col2:
        if st.button("Chat with AI Assistant"):
            st.switch_page("pages/ChatWithAI.py")

import streamlit as st
import pandas as pd
from llama_chat import ask_llama

st.set_page_config(page_title="Chat with AI Assistant", layout="wide")

st.sidebar.title("Navigation")
if st.sidebar.button("🏠 Home"):
    st.switch_page("Home.py")
if st.sidebar.button("🧹 Data Cleaner"):
    st.switch_page("pages/DataCleanerApp.py")

st.title("🤖 Chat with AI Assistant" )

if "raw_data" not in st.session_state:
    uploaded_file = st.session_state.get("uploaded_file", None)
    if uploaded_file:
        try:
            st.session_state.raw_data = pd.read_csv(uploaded_file)
        except Exception as e:
            st.error(f"Error reading file: {e}")
            st.stop()
    else:
        st.warning("Please upload a CSV file on the Home page.")
        st.stop()

df = st.session_state.raw_data.copy()

st.markdown("Ask any questions about your data. The assistant will help you analyze and clean it.")

user_prompt = st.text_area("📝 Your question:")

if st.button("Ask"):
    csv_preview = df.head(10).to_string()
    context = f"This is a preview of the dataset:\n{csv_preview}"
    response = ask_llama(user_prompt, context=context)
    st.markdown("### LLaMA Response")
    st.info(response)
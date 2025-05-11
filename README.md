# Data-Cleaning-Assistant-Using-NLP

A privacy-first, intelligent data cleaning platform designed to simplify and accelerate the preprocessing workflow for data analysts, engineers, and scientists. Built with **Streamlit**, this offline-capable application integrates both rule-based techniques and locally hosted natural language interaction to identify and resolve common data quality issues with minimal user intervention.

## Overview

The Intelligent Data Cleaning Assistant provides an intuitive interface for analyzing, cleaning, and visualizing datasets. By combining automated detection methods with a local natural language interface, it enables users to interact with their data securely—without requiring any internet connectivity or cloud services.

---

## Core Features

### 🔍 Automated Data Profiling
- Automatic detection of column data types (numerical, categorical, datetime)
- Identification of missing values, duplicate rows, and statistical outliers

### 🧹 Interactive Cleaning Tools
- Handle missing data using imputation (mean, median, mode) or row removal
- Remove duplicate entries effortlessly
- Immediate visual confirmation after every operation

### 🧠 Local Natural Language Querying
- Query your dataset using plain English
- Receive context-aware responses via a local language model
- Example queries:  
  *“Which columns have null values?”*  
  *“What is the median of the salary column?”*

### 📊 Visual Analytics
- Generate histograms and box plots for numerical features
- Visually explore data distributions and anomalies

### 📁 Export Options
- Download the cleaned dataset as a CSV file for further analysis or storage

---

## Application Architecture

├── Home.py # Main entry point: file upload & navigation
├── DataCleanerApp.py # Primary interface for cleaning and visualization
├── ChatWithLlama.py # NLP-based chat module for dataset queries
├── cleaning.py # Data profiling, cleaning, and utility logic
├── llama_chat.py # Local NLP engine interface (runs offline)


---

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

## Setup Instructions

### 1. Install Required Libraries

Ensure you have Python 3.7 or higher installed, then run:


pip install streamlit pandas numpy scipy matplotlib seaborn requests


### 2. Launch the Application

Start the web app using:


streamlit run Home.py


## Usage Guidelines

* Upload your dataset in CSV format via the Home page.
* Navigate between the Data Cleaner and Chat Assistant modules using the sidebar.
* Interactively clean the data and view visualizations in real-time.
* Download the cleaned CSV file once you're finished.

## Technologies Used

| Component       | Technology Used          |
| --------------- | ------------------------ |
| Frontend & UI   | Streamlit                |
| Data Processing | Pandas, NumPy, SciPy     |
| Visualization   | Matplotlib, Seaborn      |
| NLP Interaction | Local Language Model API |

## Contributors

This project was developed as part of an academic exercise to demonstrate the integration of data preprocessing techniques with intelligent, privacy-first NLP interactions.
Developed by
- Samruddhi Shinde
- Anushka Patil

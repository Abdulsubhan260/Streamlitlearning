# pages/1_Data_Analysis.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Data Analysis", page_icon="📈")

st.title("Data Analysis Tool ")


if "page" not in st.session_state:
    st.session_state.page = "Summary" 


st.sidebar.write("# Features")
st.sidebar.info("Please upload dataset to continue")

file = st.file_uploader("Upload your CSV file here:", type=["csv"])


if file:
    
    df = pd.read_csv(file)
    
    st.write("### Data Preview:")
    st.dataframe(df.head())

    
    st.sidebar.write("## Methods to analyze data")

    if st.sidebar.button("Summary"):
        st.session_state.page = "Summary"

    if st.sidebar.button("Name of columns"):
        st.session_state.page = "name of columns"

    if st.sidebar.button("Find null/NaN values"):
        st.session_state.page = "find null/NaN values"

    if st.sidebar.button("Columns to display"):
        st.session_state.page = "columns to display"

    if st.sidebar.button("Drop duplicate rows"):
        st.session_state.page = "drop duplicate rows"

    if st.sidebar.button("Rename the column"):
        st.session_state.page = "Rename the column"

    st.sidebar.write("## Methods to visualize the data")

    if st.sidebar.button("Bar Graph"):
        st.session_state.page = "bar"

    if st.sidebar.button("Scatter plot"):
        st.session_state.page = "scatter"

    if st.sidebar.button("Line Chart"):
        st.session_state.page = "line"

    if st.sidebar.button("Histogram"):
        st.session_state.page = "histogram"

    
    # st.markdown(f"--- \n### Current Mode: **{st.session_state.page}**")

    if st.session_state.page == "Summary":
        st.subheader("Summary of CSV file:")
        st.write(df.describe())

    elif st.session_state.page == "name of columns":
        st.write(df.columns.tolist())

    elif st.session_state.page == "find null/NaN values":
        st.subheader("Missing Values:")
        st.write(df.isnull().sum())

    elif st.session_state.page == "columns to display":
        st.subheader("Select Columns to Display:")
        selected_cols = st.multiselect("Choose columns", df.columns)
        if selected_cols:
            st.dataframe(df[selected_cols])

    elif st.session_state.page == "drop duplicate rows":
        st.subheader("Drop Duplicate Rows")
        
        if st.button("Remove Duplicates"):
            df_dropped = df.drop_duplicates()
            st.success("Duplicates Removed!")
            st.dataframe(df_dropped)

    elif st.session_state.page == "Rename the column":
        st.subheader("Rename Columns")
        col_to_rename = st.selectbox("Select column to rename", df.columns)
        new_name = st.text_input("New column name")

        if st.button("Rename Column"):
            
            df_renamed = df.rename(columns={col_to_rename: new_name})
            st.success(f"Column '{col_to_rename}' renamed to '{new_name}'!")
            st.dataframe(df_renamed)

    
    
    elif st.session_state.page == "bar":
        col1, col2 = st.columns(2)
        with col1:
            x_col = st.selectbox("Select X-axis column", df.columns)
        with col2:
            y_col = st.selectbox("Select Y-axis column", df.columns)

        if x_col and y_col:
            fig, ax = plt.subplots()
            
            num_bars = len(df[x_col].unique())
            bar_width = 0.8 if num_bars < 20 else max(0.1, 20/num_bars)
            
            ax.bar(df[x_col], df[y_col], color='red', width=bar_width)
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            ax.set_title(f"{y_col} vs {x_col}")
            st.pyplot(fig)

    elif st.session_state.page == "scatter":
        col1, col2 = st.columns(2)
        with col1:
            x_col = st.selectbox("Select X-axis col", df.columns)
        with col2:
            y_col = st.selectbox("Select Y-axis col", df.columns)

        if x_col and y_col:
            fig, ax = plt.subplots()
            ax.scatter(df[x_col], df[y_col], marker="*")
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            ax.set_title(f"{x_col} VS {y_col}")
            st.pyplot(fig)

    elif st.session_state.page == "line":
        col1, col2 = st.columns(2)
        with col1:
            x_col = st.selectbox("Select X-axis col", df.columns)
        with col2:
            y_col = st.selectbox("Select Y-axis col", df.columns)

        if x_col and y_col:
            fig, ax = plt.subplots()
            ax.plot(df[x_col], df[y_col])
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            ax.set_title(f"{x_col} VS {y_col}")
            st.pyplot(fig)

    elif st.session_state.page == "histogram":
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

        if len(numeric_cols) == 0:
            st.warning("No numeric columns available for histogram")
        else:
            col1, col2 = st.columns(2)
            with col1:
                x_col = st.selectbox("Select 1st column", numeric_cols, key="hist1")
            with col2:
                y_col = st.selectbox("Select 2nd column", numeric_cols, key="hist2")

            fig, ax = plt.subplots()
            ax.hist(df[x_col], bins=20, alpha=0.5, label=x_col)
            ax.hist(df[y_col], bins=10, alpha=0.5, label=y_col)
            ax.set_xlabel("Value")
            ax.set_ylabel("Frequency")
            ax.set_title(f"Histogram of {x_col} and {y_col}")
            ax.legend()
            st.pyplot(fig)

else:
    
    st.warning(" Please upload a CSV file in the sidebar to start!")
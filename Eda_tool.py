import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



st.sidebar.write("# Features")

st.sidebar.text("Please upload datset to continue")

if "page" not in st.session_state:
        st.session_state.page = None


st.sidebar.write("## Methods to analyze data")


if st.sidebar.button("Summary"):
       st.session_state.page = "Summary"


if st.sidebar.button("Name of columns"):
      st.session_state.page="name of columns"


if st.sidebar.button("find null/NaN values"):
      st.session_state.page="find null/NaN values"

if st.sidebar.button("columns to display"):
      st.session_state.page="columns to display"


if st.sidebar.button("drop duplicate rows"):
      st.session_state.page="drop duplicate rows"

if st.sidebar.button("Rename the column"):
      st.session_state.page="Rename the column"



st.sidebar.write("## Methods to visualize the data")

if st.sidebar.button("Bar Graph"):
      st.session_state.page="bar"


if st.sidebar.button("Scatter plot"):
      st.session_state.page="scatter"



if st.sidebar.button("Line Chart"):
      st.session_state.page="line"



if st.sidebar.button("Histogram"):
      st.session_state.page="histogram"




file=st.file_uploader("upload your csv file here:",type=["csv"])
if file :
    df = pd.read_csv(file)
    st.write("###  Data Preview:")
    st.dataframe(df)

if st.session_state.page=="Summary":
      st.subheader("summary of CSV file:")
      st.write(df.describe())


if st.session_state.page=="name of columns":
      st.write(df.columns.tolist())

if st.session_state.page=="find null/NaN values":
      st.subheader("Missing Values:")
      st.write(df.isnull().sum())


if st.session_state.page=="columns to display":
      st.subheader("Select Columns to Display:")
      selected_cols = st.multiselect("Choose columns", df.columns)
      if selected_cols:
        st.dataframe(df[selected_cols])


if st.session_state.page=="drop duplicate rows":
      st.subheader("Drop Duplicate Rows")
      if st.button("Remove Duplicates"):
        df = df.drop_duplicates()
        st.write("Duplicates Removed!")
        st.dataframe(df)

if st.session_state.page=="Rename the column":
      st.subheader("Rename Columns")
      col_to_rename = st.selectbox("Select column to rename", df.columns)
      new_name = st.text_input("New column name")

      if st.button("Rename Column"):
        df = df.rename(columns={col_to_rename: new_name})
        st.write("Column renamed!")
        st.dataframe(df)





if st.session_state.page=="bar":
      x_col = st.selectbox("Select X-axis column ", df.columns)
      y_col = st.selectbox("Select Y-axis column ", df.columns)



    
      fig, ax = plt.subplots()

      num_bars = len(df[x_col].unique())
      bar_width = 0.8 if num_bars < 20 else max(0.1, 20/num_bars)

    
      ax.bar(df[x_col], df[y_col], color='red', width=bar_width)
    
      
      ax.set_xlabel(x_col)
      ax.set_ylabel(y_col)
      ax.set_title(f"{y_col} vs {x_col}")

      st.pyplot(fig)


if st.session_state.page=="scatter":
      x_col=st.selectbox("Slelct x-axis col",df.columns)
      y_col=st.selectbox("select y-axis col",df.columns)


      fig,ax=plt.subplots()
      ax.scatter(df[x_col],df[y_col],marker="*")


      ax.set_xlabel(x_col)
      ax.set_ylabel(y_col)


      ax.set_title(f"{x_col} VS {y_col}")

      st.pyplot(fig)



if st.session_state.page=="line":
      x_col=st.selectbox("select x-axis col",df.columns)

      y_col=st.selectbox("select y-axis col",df.columns)

      fig,ax=plt.subplots()
      ax.plot(df[x_col],df[y_col])

      ax.set_xlabel(x_col)
      ax.set_ylabel(y_col)

      ax.set_title(f"{x_col} VS {y_col}")

      st.pyplot(fig)


if st.session_state.page == "histogram":

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    if len(numeric_cols) == 0:
        st.warning("No numeric columns available for histogram")
        st.stop()

    x_col = st.selectbox("Select first column for Histogram", numeric_cols)
    y_col = st.selectbox("Select second column for Histogram", numeric_cols)

    fig, ax = plt.subplots()
    ax.hist(df[x_col], bins=20, alpha=0.5, label=x_col)
    ax.hist(df[y_col], bins=10, alpha=0.5, label=y_col)
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title(f"Histogram of {x_col} and {y_col}")
    ax.legend()

    st.pyplot(fig)


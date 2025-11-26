import streamlit as st
import pandas as pd




# uploading file by using pandas and performing diffrent functions on it  by using pandas and streamlit

st.title("CSV File Uploader")
file= st.file_uploader("Upload your CSV file", type=["csv"])
# uplod file(csv)

if file :
    df = pd.read_csv(file)
    st.write("###  Data Preview:")
    st.dataframe(df)
    # preview data from uploaded file



if file:
    st.subheader("summary of CSV file:")
    st.write(df.describe())
    # show summary of data




if file:
    st.subheader("Column Names:")
    st.write(df.columns.tolist())
    # shows names of all columns




if file:
    st.subheader("Sort Data")
    sort_col = st.selectbox("Select column to sort", df.columns)
    st.dataframe(df.sort_values(sort_col))
# sort data in ascending order


if file:
    st.subheader("Missing Values:")
    st.write(df.isnull().sum())
# shows missing values if any





if file:
    st.subheader("Select Columns to Display:")
    selected_cols = st.multiselect("Choose columns", df.columns)
    if selected_cols:
        st.dataframe(df[selected_cols])
# user can select and inspect any individual col



if file:
    st.subheader("Head / Tail")
    rows = st.number_input("Number of rows", 1, 50, 5)

    if st.button("Show Top Rows"):
        st.dataframe(df.head(rows))

    if st.button("Show Bottom Rows"):
        st.dataframe(df.tail(rows))
# shows start/end rows default value is 5 but we can chnage





if file:
    st.subheader("Drop Duplicate Rows")
    if st.button("Remove Duplicates"):
        df = df.drop_duplicates()
        st.write("Duplicates Removed!")
        st.dataframe(df)

# remove duplicated rows if any




if file:
    st.subheader("Rename Columns")
    col_to_rename = st.selectbox("Select column to rename", df.columns)
    new_name = st.text_input("New column name")

    if st.button("Rename Column"):
        df = df.rename(columns={col_to_rename: new_name})
        st.write("Column renamed!")
        st.dataframe(df)
        # rename the col






# ****** SIMPLE TOOL FOR EDA********
# this tool load daata set in csv form and preview it,give summary of it,shows any missing value if exist
#  and  we cam also previwe any individual column,also shows which student got highest marks in which subject




st.title("### TOOL FOR EDA")


file= st.file_uploader("Upload your CSV file", type=["csv"])
if file :
    df = pd.read_csv(file)
    st.write("###  Data Preview:")
    st.dataframe(df)
    
    st.subheader("summary of CSV file:")
    st.write(df.describe())


    st.subheader("Missing Values:")
    st.write(df.isnull().sum())


    st.subheader("Select Columns to Display:")
    selected_cols = st.multiselect("Choose columns", df.columns)
    if selected_cols:
        st.dataframe(df[selected_cols])

    numeric_cols = ["math score", "reading score", "writing score"]

    subject = st.selectbox("Select subject", numeric_cols)

    if st.button("Show Highest Marks"):
        highest_value = df[subject].max()              
        highest_row = df[df[subject] == highest_value]  

        st.subheader("Highest Marks in Selected Column:")
        st.write(f"Highest Marks: {highest_value}")

        st.write("Student with Highest Marks:")
        st.dataframe(highest_row)









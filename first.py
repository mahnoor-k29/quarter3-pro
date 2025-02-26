import streamlit as st
import pandas as pd
import os 
from io import BytesIO

st.set_page_config  ( page_title == "Data Sweeper" ,layout='wide')

# custom css
st.markdown(
    """
<style>
    .stApp{
    background-color:black;
    color: white ;
    }
</style>
""",
unsafe_allow_html=True
)

# tittle and discription
st.title("Datasweeper Sterling Integrator by Mahnoor Kibrea")
st.write("Transform your files between CSV and excel formats with built in data cleaning and visualization Creating the project for quarter 3 !")

# file uploder 
uploaded_files = st.file_uploader("Upload your files(accepts CSV or Excel):",type=["cvs", "xlsx"],accept_multiple_files=(Trues))
if uploaded_files:
    for file in uploaded_files :
        file_ext =os.path.splitext(file.name)[-1].lower()
        if file_ext== ".csv":
         df = pd.read_csv(file)
        elif file_ext== "xlsx":
         df = pd.read_excel(file)
else :
            st.error(f"unsupported file type :{file_ext}")
            continue


            # file details
            st.write("Preview the head of the Dataframe ")
            st.dataframe(df.head())

            # data cleaning option 
            st.subheader("Data Cleaning Options")
            if st.checkbox(f"clean data for {file.name}"):
                col1 ,col2 = st.columns(2)


            with col1:
               if st.button(f"remove duplicates from the files : {file.name}"):
                 df.drop_duplicates(inplace=True)
                 st.write("Duplicates remove!")
            with col2:
                if st.button(f"fill missing value{file.name } "):
                    nimeric_cols=df.select_dtypes(includes=['number']) ,columns
                    df[numeric_cols] = df [numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing value have been filled!")

                    st.subheader("Select column to keep ")
                    columns= st.multiselect(f"choose column for {file.name } ", df.columns , default=df.columns)
                    df=df[columns]


                    # data visualization

                    st.subheader("Data Visaulization ")
                    if st.checkbox(f"show visualization for{file.name}"):
                     st.bar_chart(df.select_dtypes(include='number').iloc[:,:2])


                    #  conversion option
                    st.subheader("conversion options ")
                    conversion_type = st.radio(f"Convert{file.name}to :" ,["CVS","Excel"], key=file.name)
                    if st.button(f"convert{file.name}"):
                        buffer =BytesIO()                                                                                                                                                                                                                                                                                                                                                                                                 
                        if conversion_type== "CSV" :
                            df.to.csv(buffer,index=False)
                            file_name = file.name.replace(file_ext , ".csv")
                            mime_type = "text/csv"



                        elif conversion_type == "Excel":
                         df.to.to_excel(buffer, index=False )
                         file_name = file.name.replace(file_ext , ".xlsx")
                         mime_type ="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                         buffer.seek(0)
                          
                        st.download_button (
                            label=f"Download{file.name} as {conversion_type}"
                            data =buffer,
                            file_name=file_name,
                            mime=mime_type,
                        )

st.success("All file processed successfully")
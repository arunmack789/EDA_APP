import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

#web app title
st.markdown(
    """
    # ** The EDA app **
    This is the **EDA App** created in streamlit Using the **pandas-profiling** library.
    **Credit:** App Built in `Python` + `Streamlit`  by  [Arunkumar](https://www.linkedin.com/in/arun-kumar-85b159171/)
    
    ---
    """
)

#Upload csv data
with st.sidebar.header('1. Upload your Csv data'):
    uploaded_file = st.sidebar.file_uploader("Upload Your input Csv File",type=["csv"])
    st.sidebar.markdown("""
    [Example Csv Input File]((https://raw.githubusercontent.com/arunmack789/Data_repo/main/Trainy.csv)
    """)

if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)

import sys
import pandas as pd
import streamlit as st
import time
from datetime import datetime
from supporting_info import supporting_info
today_date_str = datetime.now().strftime("%Y-%m-%d")
try:
    st.set_page_config(layout='wide')
except:
    pass
st.markdown("""<style>
        .block-container {
        padding-top: 5rem;
        padding-bottom: 0rem;
        padding-left: 5rem;
        padding-right; 5rem;
        }
        </style>""", unsafe_allow_html=True)
st.title('Automate Loan Application Form')
@st.cache_data
def get_data():
    with open("Loan_Application_GreenLeaf_Organics_ASCII.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    return PDFbyte

if 'lending' not in st.session_state:
    st.session_state.lending = False
    st.session_state.submitted_button=False
import os
import json
@st.cache_data
def cache_df(path):
    df = pd.read_csv(path)
    return df
def form_button_click():
    st.session_state.submitted_button=True
def sidebar(submitted= False):

    st.sidebar.markdown("""
        <style>
        [data-testid=stSidebar] {
        background-color: #1A2142;
        color: #FFFFFF;
        }
        </style>
        """, unsafe_allow_html=True)
    st.sidebar.markdown("""
        <style>
        [data-testid=stPageLink-NavLink] {
        color: #FFFFFF;
        text-color: #FFFFFF;
        }
        </style>
        """, unsafe_allow_html=True)
    # st.sidebar.image("logo_base.jpeg",use_container_width=True)
    st.sidebar.markdown('''<h1 style="color:white;text-align: center"> [LOGO] </h3>''',
                        unsafe_allow_html=True)
    st.sidebar.markdown('''<h3 style="color:white;text-align: center"> User: John Smith </h3>''',unsafe_allow_html=True)
    st.sidebar.markdown('''<h3 style="color:white;text-align: center"> Role: RD </h3>''',unsafe_allow_html=True)



def main():
    form = pd.read_csv(r'lending_application.csv')
    # form =form.reset_index()
    form = form.fillna('')
    with st.expander(label = "Supporting Evidence",expanded=False):
        st.markdown("test")
    st.data_editor(form,hide_index=True)
    PDFbyte = get_data()
    col1,col2,col3 = st.columns(3)
    with col1:
        st.page_link('demo_app.py', label="Go Back", icon='🔙')

    with col2:
        st.download_button("Download Application Form",file_name="loan_application.pdf",
                           data=PDFbyte,
        mime="text/pdf",
        icon=":material/download:",)
    with col3:
        st.page_link('pages/demo_form.py', label="Email Loans Team", icon='✉️')

if __name__ == '__main__':
    sidebar()
    main()

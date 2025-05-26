
import sys
import pandas as pd
import streamlit as st
import time
from datetime import datetime


from supporting_info import supporting_info,sf_meeting_notes,news_articles_markdown
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

def color_coding(row):
    return ['background-color:red'] * len(
        row) if row.Value == "Attention Required" else ['background-color:white'] * len(row)

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


st.markdown(
    """
    <style>
        button[title^=Exit]+div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)
def main():
    form = pd.read_csv(r'lending_application.csv')
    # form =form.reset_index()
    form = form.fillna('')
    with st.expander(label = "Supporting Evidence",expanded=True):
        col1,col2, col3 = st.columns(3,vertical_alignment='center')
        with col1:
            st.markdown("**GreenLeaf Organics Ltd. 2023 Annual Report:**")
            colx1,colx2,colx3 = st.columns(3)

            with colx2:
                st.image("PDF_file_icon.svg.png",width=50)
        col1,col2, col3 = st.columns(3,vertical_alignment='center')
        with col1:
            st.markdown("**Transaction Data (Last 12 Months)**:")
            colx1,colx2,colx3 = st.columns(3)
            with colx2:
                st.image("Microsoft_Excel_2013-2019_logo.svg.png",width=50)
        col1,col2, col3 = st.columns(3,vertical_alignment='center')
        with col1:
            st.markdown("**DG Rating (Zeus)**:")
            # colx1,colx2,colx3 = st.columns(3)
            # with colx2:
            dg_Rating = cache_df(r'dg_rating.csv')
            st.dataframe(dg_Rating,hide_index=True)
        with st.popover("**Salesforce Meeting Notes**"):
            st.markdown("**Salesforce Meeting Notes:**")
            st.markdown(sf_meeting_notes,unsafe_allow_html=True)
        with st.popover("**External News & Market Intelligence**"):
            st.markdown("**External News & Market Intelligence (Retrieved by Agent):**")
            st.markdown(news_articles_markdown,unsafe_allow_html=True)
        # st.markdown("**Salesforce Meeting Notes:**")
        # st.markdown(sf_meeting_notes,unsafe_allow_html=True)


    form2 = form.style.map(lambda x: f"background-color: {'red' if x=='Attention Required' else 'white'}", subset='Value')

    # st.data_editor(form.style.apply(color_coding, axis=1),hide_index=True)
    st.data_editor(form2, hide_index=True)
    # st.dataframe(form2, hide_index=True)
    PDFbyte = get_data()
    col1,col2,col3 = st.columns(3)
    with col1:
        st.page_link('main_page.py', label="Go Back", icon='🔙')

    with col2:
        st.download_button("Download Application Form",file_name="loan_application.pdf",
                           data=PDFbyte,
        mime="text/pdf",
        icon=":material/download:",)
    with col3:
        # st.page_link('main_page.py', label="Email Loans Team", icon='✉️')
        st.page_link('main_page.py', label="Setup Client Meeting", icon='📅️')
if __name__ == '__main__':
    sidebar()
    main()

import pandas as pd
import streamlit as st
import time
import random
from raw_text import *
from crew import esg_crew
if 'submitted_button' not in st.session_state:
    st.session_state.submitted_button=False
    st.session_state.company_select=''
st.set_page_config(layout='wide')
st.markdown("""<style> 
        .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 5rem;
        padding-right; 5rem;
        }
        </style>""",unsafe_allow_html=True)
st.sidebar.markdown("""
    <style>
    [data-testid=stSidebar] {
    background-color: #1A2142;
    color: #FFFFFF;
    }
    </style>
    """,unsafe_allow_html=True)
st.sidebar.markdown("""
    <style>
    [data-testid=stPageLink-NavLink] {
    color: #FFFFFF;
    text-color: #FFFFFF;
    }
    </style>
    """,unsafe_allow_html=True)
st.title('Client Pitchbook Request')
@st.cache_data
def cache_df(path):
    df = pd.read_csv(path)
    return df
def form_button_click():
    st.session_state.submitted_button=True
def sidebar(submitted= False):
    # st.sidebar.divider()
    # with st.sidebar:
    #     st.markdown('''<p style="color:#00AEEF;text-align: center;font-size:42px"> MuRA</p>
    #     <p style="color:#00AEEF;text-align: center;font-size:20px"> Multi-Use Research Assistant</p>''',unsafe_allow_html=True)
    st.sidebar.image("logo.png",use_column_width=True)
    st.sidebar.markdown('''<h3 style="color:white;text-align: center"> User: John Smith </h3>''',unsafe_allow_html=True)
    st.sidebar.markdown('''<h3 style="color:white;text-align: center"> Role: RD </h3>''',unsafe_allow_html=True)
    st.sidebar.markdown('''<h3 style="color:#0068c9"> Tools </h3>''',unsafe_allow_html=True)
    st.sidebar.page_link('main_page.py',label=':blue[Pitchbook Request]',icon='📃')
    # st.sidebar.divider()
    st.sidebar.markdown('''<h2 style="color:white"> Verified Pitchbooks: </h2>''',unsafe_allow_html=True)
    st.sidebar.markdown("""- Company 123 
    \n- Company ABC""")
    if submitted:
        st.sidebar.markdown('''<h2 style="color:white"> In-progress Pitchbooks: </h2>''',unsafe_allow_html=True)
        st.sidebar.markdown("""- Company XYZ 
        \n- P-(ai)-oneers PLC""")
    else:
        st.sidebar.markdown('''<h2 style="color:white"> In-progress Pitchbooks: </h2>''',unsafe_allow_html=True)
        st.sidebar.markdown("""- Company XYZ""")
def main():
    st.markdown("##### Hello John Smith, please complete the below to request a Client Pitchbook:")




    with st.form('form1'):
        st.session_state.company_select = st.selectbox('Please Select Client',options=['P-(ai)-oneers PLC','Company XYZ','Company ABC', 'Company 123'])
        submitted_button = st.form_submit_button("Submit", on_click=form_button_click)
    if submitted_button:
        st.write_stream(esg_crew.kickoff(inputs = {'company_name':'Barclays Bank', 'number_of_articles':10}))

if __name__ == '__main__':
    main()


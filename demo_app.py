
import sys
import pandas as pd
import streamlit as st
import time
from datetime import datetime
from supporting_info import supporting_info
today_date_str = datetime.now().strftime("%Y-%m-%d")
st.set_page_config(layout='wide')
st.markdown("""<style>
        .block-container {
        padding-top: 5rem;
        padding-bottom: 0rem;
        padding-left: 5rem;
        padding-right; 5rem;
        }
        </style>""", unsafe_allow_html=True)
st.title('Sales Automation Tool')

if 'lending' not in st.session_state:
    st.session_state.lending = False
    st.session_state.submitted_button=False
    st.session_state.autofill = False
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
    # st.sidebar.page_link('pages/demo_form.py', label=':blue[Live App]', icon='📃')

def main():
    st.markdown("##### Hello John Smith, please select your client to view opportunities available")




    with st.form('form1'):
        st.session_state.company_select = st.selectbox('Please Select Client',options=['Select Client','GreenLeaf Organics Ltd','Company XYZ','Company ABC', 'Company 123'])
        # st.session_state.company_select = st.text_input('Please enter in Company name',value = 'Barclays Bank')
        submitted_button = st.form_submit_button("Submit", on_click=form_button_click)
        # prompts = pd.read_csv(r'prompts.csv')
        # st.dataframe(prompts,hide_index=True)

    if st.session_state.submitted_button or st.session_state.lending:
        #load in the prompts dataframe
        st.markdown(f"## Opportunities for {st.session_state.company_select}")
        prompts = pd.read_csv(r'prompts.csv')
        st.dataframe(prompts,hide_index=True)
        # with col1:
        #     with st.expander('Recent News Articles',expanded=True):
        st.markdown('#### Select below for more details')
        col1,col2,col3 = st.columns(3)
        with col1:
            st.session_state.lending = st.button("Lending (prompt_abc123)")
        with col2:
            fx = st.button("FX (prompt_abc124)")
        with col3:
            deposit = st.button("Deposit (prompt_abc125)")
        #st.write_stream(esg_crew.kickoff(inputs = {'company_name':'Barclays Bank', 'number_of_articles':10}))

    if st.session_state.lending:
        st.markdown(supporting_info)

        st.markdown("### Next Steps:")
        col1,col2,col3 = st.columns(3)
        with col1:
            # st.button("Setup Client Meeting")
            st.page_link('pages/demo_form.py', label="Setup Client Meeting", icon='📅️')
        with col2:
            # if st.button("Autofill Lending Application"):
            st.page_link('pages/demo_form.py',label="Autofill Lending Application",icon='📄️')
        with col3:
            # st.button("Email Loans Team")#
            st.page_link('pages/demo_form.py', label="Email Loans Team", icon='✉️')


if __name__ == '__main__':
    sidebar()
    main()


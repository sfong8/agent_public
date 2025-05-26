
import sys
import pandas as pd
import streamlit as st
import time
from datetime import datetime


from supporting_info import supporting_info, fake_email
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

if 'submitted_button' not in st.session_state:
    st.session_state.submitted_button=False

if 'email_button' not in st.session_state:
    st.session_state.email_button=False

if 'autofill' not in st.session_state:
    st.session_state.autofill = False
if 'send_email_button' not in st.session_state:
    st.session_state.send_email_button = False
import os
import json
@st.cache_data
def cache_df(path):
    df = pd.read_csv(path)
    return df
def form_button_click():
    st.session_state.submitted_button=True

def lending_button_click():
    st.session_state.lending = True

def email_button_click():
    st.session_state.email_button = True
def send_email_button():
    st.session_state.send_email_button = True
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
        submitted_button = st.form_submit_button("Submit",on_click=form_button_click)


    if st.session_state.submitted_button or st.session_state.lending:
        if (st.session_state.lending==False) and (st.session_state.email_button==False):
            with st.spinner("Loading Salesforce Prompts..."):
                time.sleep(3)
        #load in the prompts dataframe
        st.markdown(f"## Opportunities for {st.session_state.company_select}")
        prompts = pd.read_csv(r'prompts.csv')
        st.dataframe(prompts,hide_index=True)
        # with col1:
        #     with st.expander('Recent News Articles',expanded=True):
        st.markdown('#### Select below for more details')
        col1,col2,col3 = st.columns(3)
        with col1:
            lending = st.button("Lending (prompt_abc123)",on_click=lending_button_click)
        with col2:
            fx = st.button("FX (prompt_abc124)")
        with col3:
            deposit = st.button("Deposit (prompt_abc125)")

    if st.session_state.lending:
        if (st.session_state.email_button == False):
            with st.spinner(fr"Fetching Supporting Information for Lending Opportunity for GreenLeaf Organics Ltd..."):
                time.sleep(5)
        st.markdown(supporting_info)

        st.markdown("### Next Steps:")
        col1,col2,col3 = st.columns(3)
        with col1:
            email_button = st.button("Email Loans Team", icon='✉️',type='tertiary',on_click=email_button_click)#
            # st.page_link('pages/demo_form.py', label="Email Loans Team", icon='✉️')
        with col3:
            # st.button("Setup Client Meeting")
            st.page_link('pages/demo_form.py', label="Setup Client Meeting", icon='📅️')
        with col2:
            # if st.button("Autofill Lending Application"):
            st.page_link('pages/demo_form.py',label="Autofill Lending Application",icon='📄️')

        if st.session_state.email_button:
            if st.session_state.send_email_button==False:
                with st.spinner("Logging Salesforce Opportunity and Generating Email to Loans Team..."):
                    time.sleep(2)
            st.success("Salesforce Opportunity Logged and Email generated successfully!")
            with st.expander("Generated Email", expanded=False):
                st.markdown(fake_email)
            if st.button("Send Email",on_click=send_email_button):
                st.success("Email sent successfully!")
        st.markdown("")

if __name__ == '__main__':
    sidebar()
    main()


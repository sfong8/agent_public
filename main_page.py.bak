__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import pandas as pd
import streamlit as st
import time
import random
from crew import esg_crew,crew
from datetime import datetime
today_date_str = datetime.now().strftime("%Y-%m-%d")
st.set_page_config(layout='wide')
st.markdown("""<style>
        .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 5rem;
        padding-right; 5rem;
        }
        </style>""", unsafe_allow_html=True)
st.title('Client Research Assistant')
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
    st.sidebar.image("logo_base.jpeg",use_column_width=True)
    st.sidebar.markdown('''<h3 style="color:white;text-align: center"> User: John Smith </h3>''',unsafe_allow_html=True)
    st.sidebar.markdown('''<h3 style="color:white;text-align: center"> Role: RD </h3>''',unsafe_allow_html=True)
    # st.sidebar.markdown('''<h3 style="color:#0068c9"> Tools </h3>''',unsafe_allow_html=True)
    st.sidebar.page_link('pages/demo.py',label=':blue[Demo]',icon='📃')
    st.sidebar.page_link('main_page.py', label=':blue[Live App]', icon='📃')
    # st.sidebar.divider()

def main():
    st.markdown("##### Hello John Smith, please enter in Company name below to get started")




    with st.form('form1'):
        # st.session_state.company_select = st.selectbox('Please Select Client',options=['P-(ai)-oneers PLC','Company XYZ','Company ABC', 'Company 123'])
        st.session_state.company_select = st.text_input('Please enter in Company name',value = 'Barclays Bank')
        submitted_button = st.form_submit_button("Submit", on_click=form_button_click)
    if submitted_button:
        # col1,col2 = st.columns(2)
        try:
            os.remove('crew_log.json')
            os.remove('esg_crew_log.json')
        except:
            pass
        # with col1:
        #     with st.expander('Recent News Articles',expanded=True):
            st.markdown(f"## Recent News Articles on {st.session_state.company_select}")
            with st.spinner('Fetching news articles and Generating Report...'):
                news_results = crew.kickoff(inputs = {'company_name':st.session_state.company_select, 'number_of_articles':10,'today_date':today_date_str})
                time.sleep(2)
                with st.expander("News Agent Logs", expanded=False):
                    with open('crew_log.json', 'r') as f:
                        d = json.load(f)
                    st.json(d, expanded=False)
                st.markdown(news_results.raw)
            time.sleep(60)
            st.markdown(f"## ESG Insights on {st.session_state.company_select}")
            with st.spinner('Fetching ESG articles and Generating ESG Report...'):
                esg_results = esg_crew.kickoff(inputs = {'company_name':st.session_state.company_select, 'number_of_articles':10,'today_date':today_date_str})
                time.sleep(2)
                with st.expander("ESG Agent Logs", expanded=False):
                    with open('esg_crew_log.json', 'r') as f:
                        d = json.load(f)
                    st.json(d, expanded=False)
                st.markdown(esg_results.raw)
        #st.write_stream(esg_crew.kickoff(inputs = {'company_name':'Barclays Bank', 'number_of_articles':10}))

if __name__ == '__main__':
    sidebar()
    main()


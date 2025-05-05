import pandas as pd
import streamlit as st
import time
import json
import random
from datetime import datetime
from main_page import sidebar
from demo_text import *
today_date_str = datetime.now().strftime("%Y-%m-%d")
try:
    st.set_page_config(layout='wide')
except:
    pass
if 'submitted_button' not in st.session_state:
    st.session_state.submitted_button=False
    st.session_state.company_select=''

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
st.title('Client Research Assistant')
@st.cache_data
def cache_df(path):
    df = pd.read_csv(path)
    return df
def form_button_click():
    st.session_state.submitted_button=True

def main():
    st.markdown("##### Hello John Smith, please enter in Company name below to get started")




    with st.form('form1'):
        # st.session_state.company_select = st.selectbox('Please Select Client',options=['P-(ai)-oneers PLC','Company XYZ','Company ABC', 'Company 123'])
        st.session_state.company_select = st.text_input('Please enter in Company name',value = 'Barclays Bank')
        submitted_button_live = st.form_submit_button("Submit", on_click=form_button_click)
    if submitted_button_live:
        col1, col2 = st.columns(2)
        with col1:
            with st.container(border = True):
                st.markdown(f"## Recent News Articles on {st.session_state.company_select}")
                with st.spinner('Fetching news articles and Generating Report...'):
                    time.sleep(random.randint(5,10))
                    with st.expander("News Agent Logs", expanded=False):
                        with open('crew_log_demo.json','r') as f:
                            d=json.load(f)
                        st.json(d,expanded=False)

                    st.markdown(latest_news_barclays)
        with col2:
            with st.container(border=True):
                st.markdown(f"## Recent ESG Articles on {st.session_state.company_select}")
                with st.spinner('Fetching news articles and Generating Report...'):
                    time.sleep(random.randint(5,10))
                    with st.expander("ESG Agent Logs", expanded=False):
                        with open('crew_log_demo.json','r') as f:
                            d=json.load(f)
                        st.json(d,expanded=False)

                    st.markdown(esg_report)
        # st.markdown(f"## ESG Insights on {st.session_state.company_select}")
        # with st.spinner('Fetching ESG articles and Generating ESG Report...'):
        #     # time.sleep(10)
        #     with st.expander("ESG Agent Logs", expanded=False):
        #         with open('esg_crew_log_demo.json','r') as f:
        #             d=json.load(f)
        #         st.json(d,expanded=False)
        #
        #     st.markdown(esg_report)

        #st.write_stream(esg_crew.kickoff(inputs = {'company_name':'Barclays Bank', 'number_of_articles':10}))

if __name__ == '__main__':
    sidebar()
    main()


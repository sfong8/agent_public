import pandas as pd
import streamlit as st
import time
import random
import sys
sys.path.append(r'C:\Users\JFong\IdeaProjects\hackathon\streamlit')
from raw_text import *

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
    color: #FFF;
    }
    </style>
    """,unsafe_allow_html=True)
# st.markdown("""
#     <style>
#     [data-testid=stSidebar] {
#     background-color: #1A2142;
#     color: #00AEEF;
#     text-size: 16px;
#     }
#     </style>
#     """,unsafe_allow_html=True)
st.title('Client Pitchbook Review (DST)')
@st.cache_data
def cache_df(path):
    df = pd.read_csv(path)
    return df
def form_button_click():
    st.session_state.submitted_button=True
def sidebar(submitted= False):
    st.sidebar.image("Picture2.png",use_column_width=True)
    st.sidebar.markdown('''<h3 style="color:white;text-align: center"> User: Jane Smith </h3>''',unsafe_allow_html=True)
    st.sidebar.markdown('''<h3 style="color:white;text-align: center"> Role: DST </h3>''',unsafe_allow_html=True)

    st.sidebar.markdown('''<h2 style="color:white"> Pending Review: </h2>''',unsafe_allow_html=True)
    st.sidebar.markdown("""- Company XYZ 
    \n- P-(ai)-oneers PLC
    \n - Company 123""")

def main():
    st.markdown("##### Hello Jane Smith, Please review the below report for P-(ai)-oneers PLC requested by RD John Smith")

    fin_statement = cache_df(r'financial_statements.csv')
    client_income = cache_df(r'client_income.csv')
    client_transaction = cache_df(r'client_payments.csv')
    # st.markdown("<h6 style='text-align: center'>**Disclaimer**: Pitchbook **:red[NOT]** verified by Deal Support Team (DST) yet.</h6>",unsafe_allow_html=True)
    st.markdown(f'''<h2 style="text-align: center"> {st.session_state.company_select} Pitchbook </h2>''',unsafe_allow_html=True)
    # st.markdown("<h6 style='text-align: center'>**Disclaimer**: Pitchbook **:red[NOT]** verified by Deal Support Team (DST) yet.</h6>",unsafe_allow_html=True)
    # st.markdown("**Disclaimer**: Pitchbook **:red[NOT]** verified by Deal Support Team (DST) yet.",unsafe_allow_html=True)
    with st.expander("Client Internal Insights",expanded=False):
        st.markdown(f'''<h2 style="color:#1A2142;text-align: center"> Client Internal Summary</h2>''',unsafe_allow_html=True)
        st.write("""#### Client Details:
                                \n- Customer Name: P-(ai)-oneers PLC
                                \n- Number of Subsidaries: 5
                                \n- Industry Sector: Manufacturing """)

        st.markdown(f'''<h3 style="color:#1A2142;text-align: center"> Client Income Performance</h3>''',unsafe_allow_html=True)

        # col1,col2,col3= st.columns(3)
        # with col2:
        st.markdown('''<h5 style="text-align: center"> Total Monthly Income (12 months) </h5>''',unsafe_allow_html=True)
        st.bar_chart(data=client_income.groupby(['Summary date']).sum().reset_index(),x='Summary date',y='Income',use_container_width=False,width=800)
        st.markdown(income_insights)

        st.markdown(f'''<h3 style="color:#1A2142;text-align: center"> Client Complaints Summary</h3>''',unsafe_allow_html=True)
        st.markdown(complaints_text)
        st.markdown(f'''<h3 style="color:#1A2142;text-align: center"> Client Transactions Insights</h3>''',unsafe_allow_html=True)
        col1,col2= st.columns(2)
        with col1:
            st.markdown('''<h5 style="text-align: center"> Total Outbound Payments (£) (12 months) </h5>''',unsafe_allow_html=True)
            st.bar_chart(data=client_transaction,x='Month',y='Total Outbound Payments',use_container_width=True)
        with col2:
            st.markdown('''<h5 style="text-align: center"> Total Inbound Payments (£) (12 months) </h5>''',unsafe_allow_html=True)
            st.bar_chart(data=client_transaction,x='Month',y='Total Inbound Payments',use_container_width=True)
        st.markdown(client_payments_text)
    with st.expander("Client External Insights",expanded=False):
        st.markdown(f'''<h2 style="color:#1A2142;text-align: center"> Client External Insights</h2>''',unsafe_allow_html=True)
        st.markdown(f'''<h3 style="color:#1A2142;text-align: center"> Financial Statement</h3>''',unsafe_allow_html=True)
        st.dataframe(fin_statement)
        st.markdown(fin_statement_text)

        st.markdown(f'''<h3 style="color:#1A2142;text-align: center"> ESG Industry Insights</h3>''',unsafe_allow_html=True)
        st.markdown(esg_text)
        st.markdown('#### Industry Trends')
        st.markdown(industry_trends_manufacturing)

    col0,col1,col2,col00 = st.columns(4)
    with col1:
        st.button('Accept and Verify Accuracy of Report')
    with col2:
            st.button('Reject and Override')
    sidebar()

if __name__ == '__main__':
    main()


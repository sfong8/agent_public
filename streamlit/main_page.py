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
    st.sidebar.page_link('pages/chat_assistant.py',label=':blue[Assistant]',icon='🤖')
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

    colx,col1,col2,coly = st.columns(4)


    with col2:
        clientbutton1 = st.button('Prospect Client')

    with col1:
        clientbutton_existing = st.button('Existing Internal Client')


    if clientbutton1:
        st.text_input('Please Enter in the name of the company')

    if clientbutton_existing:
        with st.form('form1'):
            st.session_state.company_select = st.selectbox('Please Select Client',options=['P-(ai)-oneers PLC','Company XYZ','Company ABC', 'Company 123'])
            st.multiselect('Select Internal Data Source',['Client Income Data','Client Transaction Data','Client Complaints'],['Client Income Data','Client Transaction Data','Client Complaints'])
            st.multiselect('Select External Data Source',['Company Financial Statement','Client Annual Report','ESG','Industry Trends'],['Company Financial Statement','Client Annual Report','ESG','Industry Trends'])
            submitted_button = st.form_submit_button("Submit",on_click=form_button_click)
    sidebar(submitted=st.session_state.submitted_button)
    if st.session_state.submitted_button:
        with st.spinner(f"Generating Client Pitchbook for {st.session_state.company_select}"):
            time.sleep(random.randint(3,5))
            client_income = cache_df(r'client_income.csv')
            fin_statement = cache_df(r'financial_statements.csv')
            client_transaction = cache_df(r'client_payments.csv')
            # st.markdown("<h6 style='text-align: center'>**Disclaimer**: Pitchbook **:red[NOT]** verified by Deal Support Team (DST) yet.</h6>",unsafe_allow_html=True)
            st.markdown(f'''<h2 style="text-align: center"> {st.session_state.company_select} Pitchbook </h2>''',unsafe_allow_html=True)
            st.markdown("**Disclaimer**: Pitchbook **:red[NOT]** verified by Deal Support Team (DST) yet",unsafe_allow_html=True)
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
                st.markdown(f'''<h3 style="color:#1A2142;text-align: center"> Client Transactions Insights</h3>''',unsafe_allow_html=True)
                col1,col2= st.columns(2)
                with col1:
                    st.markdown('''<h5 style="text-align: center"> Total Outbound Payments (£) (12 months) </h5>''',unsafe_allow_html=True)
                    st.bar_chart(data=client_transaction,x='Month',y='Total Outbound Payments',use_container_width=True)
                with col2:
                    st.markdown('''<h5 style="text-align: center"> Total Inbound Payments (£) (12 months) </h5>''',unsafe_allow_html=True)
                    st.bar_chart(data=client_transaction,x='Month',y='Total Inbound Payments',use_container_width=True)
                st.markdown(client_payments_text)
                st.markdown(f'''<h3 style="color:#1A2142;text-align: center"> Client Complaints Summary</h3>''',unsafe_allow_html=True)
                st.markdown(complaints_text)

            with st.expander("Client External Insights",expanded=False):
                st.markdown(f'''<h2 style="color:#1A2142;text-align: center"> Client External Insights</h2>''',unsafe_allow_html=True)
                st.markdown(f'''<h3 style="color:#1A2142;text-align: center"> Financial Statement</h3>''',unsafe_allow_html=True)
                st.dataframe(fin_statement)
                st.markdown(fin_statement_text)

                st.markdown(f'''<h3 style="color:#1A2142;text-align: center"> ESG Industry Insights</h3>''',unsafe_allow_html=True)
                st.markdown(esg_text)
                st.markdown('#### Industry Trends')
                st.markdown(industry_trends_manufacturing)
        col1,col2,col3 = st.columns(3)
        with col1:
            st.button('Download Report (PDF)')
        with col2:
            st.button('Download Report (PPT)')
        with col3:
            st.button('Submit Feedback')

if __name__ == '__main__':
    main()


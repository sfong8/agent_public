import streamlit as st
import time
if 'messages' not in st.session_state:
    st.session_state['messages']=[]
    st.session_state.messages.append({'role':'assistant',"content":"""Hello John Smith! I am your AI assistant who can help you research your client, please ask a question below"""})
st.set_page_config(layout='wide')
st.title('Client Research Assistant')
st.markdown("""<style> 
        .block-container {
        padding-top: 2rem;
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
def sidebar(submitted= False):
    # st.sidebar.divider()
    # with st.sidebar:
    #     st.markdown('''<p style="color:#00AEEF;text-align: center;font-size:42px"> MuRA</p>
    #     <p style="color:#00AEEF;text-align: center;font-size:20px"> Multi-Use Research Assistant</p>''',unsafe_allow_html=True)
    st.sidebar.image("Picture2.png",use_column_width=True)
    st.sidebar.markdown('''<h3 style="color:white;text-align: center"> User: John Smith </h3>''',unsafe_allow_html=True)
    st.sidebar.markdown('''<h3 style="color:white;text-align: center"> Role: RD </h3>''',unsafe_allow_html=True)
    st.sidebar.markdown('''<h3 style="color:#0068c9"> Tools </h3>''',unsafe_allow_html=True)
    st.sidebar.page_link('main_page.py',label=':blue[Pitchbook Request]',icon='📃')
    st.sidebar.page_link('pages/chat_assistant.py',label=':blue[Assistant]',icon='🤖')
    # st.sidebar.divider()
    st.sidebar.markdown('''<h2 style="color:white"> Verified Pitchbooks: </h2>''',unsafe_allow_html=True)
    st.sidebar.markdown("""- Company123 
    \n- Company ABC""")
    if submitted:
        st.sidebar.markdown('''<h2 style="color:white"> In-progress Pitchbooks: </h2>''',unsafe_allow_html=True)
        st.sidebar.markdown("""- Company XYZ 
        \n- P-(ai)-oneers PLC""")
    else:
        st.sidebar.markdown('''<h2 style="color:white"> In-progress Pitchbooks: </h2>''',unsafe_allow_html=True)
        st.sidebar.markdown("""- Company XYZ""")



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
sidebar()
# Accept user input
if prompt := st.chat_input("Ask a Question"):

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    if prompt.lower()=='what can you do?':
        with st.spinner("Generating Response"):
            time.sleep(5)
        response = """I can perform a variety of tasks to support and enhance the banking experience for our clients. Here’s a breakdown of some of the key activities I can undertake:  
   
1. **Client Research and Analysis:**  
   - Conduct thorough research on clients to understand their business models, financial health, industry trends, and competitive landscape.  
   - Analyze financial statements, market conditions, and other relevant data to gain insights into client needs and opportunities.  
   
2. **Identifying Banking Needs:**  
   - Identify potential banking products and services that align with the client's business goals and financial needs, such as loans, treasury services, cash management, trade finance, and investment products.  
   - Understand and anticipate the evolving needs of clients based on changes in their business or industry.  

   
3. **Cross-Selling and Up-Selling:**  
   - Identify opportunities to cross-sell and up-sell additional banking products and services that can benefit the client.  
   - Collaborate with other departments within the bank to deliver comprehensive solutions.  

4. **Market and Industry Insights:**  
   - Stay updated on market trends, economic conditions, and regulatory changes that may impact clients.  
   - Share relevant insights and information with clients to help them make informed decisions.  
   
By leveraging these activities, I can help clients achieve their financial goals, enhance their banking experience, and contribute to the overall success and growth of the bank."""
    else:
        # prompt.lower()=='Give me a summary of last 12months of complaints my client "P-(ai)-oneers PLC"'
        with st.spinner("Generating Response"):
            time.sleep(5)
        response = """Based on the provided information, here is a summary of customer complaints for the past 12months:  
1. **Bank account or service**:   
   - **Account opening, closing, or management**:  
     - Complaints included charges for insufficient funds although funds were sufficient.  
     - Issues with being charged for account types customers claim they did not request or were eligible for.  
2. **Debt or credit management**:  
   - **Credit repair services**:  
     - Complaints about unauthorized charges for memberships and the struggle to get refunds for those charges  
3. **Money transfer, virtual currency, or money service**:  
   - **Foreign currency exchange**:  
     - Complaints regarding incorrect exchange rates that resulted in financial loss despite assurances of receiving the federal exchange rate.  """
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})



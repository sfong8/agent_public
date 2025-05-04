from crewai import Crew, Process
# from tasks import new_research_task,webcrawl_task,webscrape_task
# from agents import researcher,webcrawl_agent,webscraping_agent
from agents import *
from tasks import *
from crewai import LLM
import os
os.environ['GEMINI_API_KEY'] = "AIzaSyCUL6FMSbkJhzu1Xh0f4xrYj5Q_LGFFfzE"
# call gemini model
from datetime import datetime
# Define your custom crew here
# crew = Crew(
#     agents=[Webcrawler, Webscraper,ReportAnalyst],
#     tasks=[google_news_search, webpage_extraction,createReport],
#     planning=True,
#     planning_llm=llm,
#             verbose=True,
#             process=Process.sequential
#         )
crew = Crew(
    agents=[esg_Webcrawler, ESG_Webscraper,ESG_ReportAnalyst],
    tasks=[ESG_search, esg_webpage_extraction,createESGReport],
    planning=True,
    planning_llm=llm,
            verbose=True,
            process=Process.sequential
        )
today_date_str = datetime.now().strftime("%Y-%m-%d")
result = crew.kickoff(inputs = {'company_name':'Barclays Bank', 'number_of_articles':10,'today_date':today_date_str})

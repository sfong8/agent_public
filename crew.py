from crewai import Crew, Process
# from tasks import new_research_task,webcrawl_task,webscrape_task
# from agents import researcher,webcrawl_agent,webscraping_agent
from agents import *
from tasks import *
from crewai import LLM
import os
os.environ['GEMINI_API_KEY'] = "AIzaSyCUL6FMSbkJhzu1Xh0f4xrYj5Q_LGFFfzE"
# call gemini model
llm = LLM(model='gemini/gemini-1.5-flash',
                            verbose=True,
                            temperature=0.1,
                            )


# Define your custom crew here
crew = Crew(
    agents=[Webcrawler, Webscraper,ReportAnalyst],
    tasks=[google_news_search, webpage_extraction,createReport],
    # manager_agent=manager,
    # manager_task=custom_task_3,
    # manager_llm=llm,
            verbose=True,
            process=Process.sequential
        )

result = crew.kickoff(inputs = {'company_name':'Barclays Bank', 'number_of_articles':5})

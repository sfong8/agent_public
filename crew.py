from crewai import Crew, Process
# from tasks import new_research_task,webcrawl_task,webscrape_task
# from agents import researcher,webcrawl_agent,webscraping_agent
from agents import *
from tasks import *
from crewai import LLM
from crewai.agents.parser import AgentAction, AgentFinish
from crewai.agents.crew_agent_executor import ToolResult
# import logging
# import sys
# logger = logging.getLogger(__name__)
# logger.addHandler(logging.FileHandler(f"{__name__}.log"))
# logger.addHandler(logging.StreamHandler(sys.stdout))
# def step_callback(step):
#     if isinstance(step, AgentAction):
#         logger.info(f"Action: {step.text}")
#     elif isinstance(step, AgentFinish):
#         logger.info(f"Finish: {step.text}")
#     elif isinstance(step, ToolResult):
#         logger.info(f"Tool Result: {step.result}")

import os
os.environ['GEMINI_API_KEY'] = "AIzaSyCUL6FMSbkJhzu1Xh0f4xrYj5Q_LGFFfzE"
# call gemini model
from datetime import datetime
# Define your custom crew here
crew = Crew(
    agents=[Webcrawler, Webscraper,ReportAnalyst],
    tasks=[google_news_search, webpage_extraction,createReport],
    planning=True,
    planning_llm=llm,
max_rpm=12,
            verbose=True,
            process=Process.sequential,
output_log_file='crew_log.json'
         )
esg_crew = Crew(
    agents=[esg_Webcrawler, ESG_Webscraper,ESG_ReportAnalyst],
    tasks=[ESG_search, esg_webpage_extraction,createESGReport],
    planning=True,
    planning_llm=llm,
max_rpm=12,
output_log_file='esg_crew_log.json',
            verbose=True,
            process=Process.sequential
        )


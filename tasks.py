# To know more about the Task class, visit: https://docs.crewai.com/concepts/tasks
from crewai import Task
from textwrap import dedent
from tools import google_news_tool,scrape_tool
from agents import *

google_news_search=Task(
            description=dedent(
                """
            Google news search for the latest news articles related to {company_name} and return a list URLS of the {number_of_articles} articles. - use google news as the search engine
        """
            ),
            expected_output="Return only the URLs (link from the tool output) containing the most relevant information about company {company_name}",
            tools=[google_news_tool],
            agent=Webcrawler,
        )

webpage_extraction   = Task(
            description=dedent(
                """
            Scrape the websites for the Latest news and articles related to {company_name}. Note, it is ok if you cannot extract the text from the URL, just move onto the next one.
        """
            ),
            expected_output="Return extracted content about company {company_name}",
            agent=Webscraper,
            tools=[scrape_tool],
            context=[google_news_search]
        )

createReport= Task(
            description=dedent("""Review the context you got about {company_name} and expand it into a full section for a report.
Make sure the report is detailed and contains any and all relevant information. It is fine the Webscraper cannot extract all the information from the URLs, as long as you have atleast one source, you can create the report.
Remember to cite your sources.
"""
            ),
            expected_output="A fully fledge reports with the latest news about {company_name}",
            agent=ReportAnalyst,
            context=[webpage_extraction]
        )
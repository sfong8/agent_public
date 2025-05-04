from crewai import Agent
from textwrap import dedent
import os
from crewai import Agent
from tools import google_news_tool,scrape_tool
from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import LLM
load_dotenv()
os.environ['GEMINI_API_KEY'] = "AIzaSyCUL6FMSbkJhzu1Xh0f4xrYj5Q_LGFFfzE"

# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
llm = LLM(model='gemini/gemini-1.5-flash',
                            verbose=True,
                            temperature=0.2,
          max_tokens=100_000)

Webcrawler   = Agent(
            role="Google News Searcher",
            backstory=dedent("""You’re a news article agent renowned for uncovering the latest news and articles for the following company {company_name}.
Your expertise lies in identifying the most relevant source URLs containing information about {company_name}., you find the latest news """),
            goal=dedent("Find the latest and most relevant latest news articles for company {company_name} - use google news as the search engine. Avoid using urls that are the company own website"""),
             tools=[google_news_tool],
            allow_delegation=False,
            verbose=True,
            llm=llm,
        )

Webscraper= Agent(
            role="Specialist in Scraping the important information from different websites about the company {company_name}.",
            backstory=dedent("""You are a Webpage Extractor agent, you extract the text from the following urls."""),
            goal=dedent("""Find the latest news about company {company_name} from different URLs you get from Web_crawler and extracting the important information about the company {company_name}"""),
            tools=[scrape_tool],
            allow_delegation=False,
            verbose=True,
            llm=llm,
        )
ReportAnalyst= Agent(
        role="""Specialist in creating a Report from the provided context related to the company {company_name} for a relationship manager preparing for a client meeting. """,

        goal="Create detailed reports based on {company_name} with the help of data from Webscraper.",
        backstory="You’re a meticulous analyst with a keen eye for detail. You’re known for your ability to turn complex data into clear and concise reports, making it easy for others to understand and act on the information you provide.",
        allow_delegation=False,
        llm=llm,
                )
manager = Agent(
        role="Manager",
        memory=True,
        goal="Efficiently manage the crew and ensure high-quality task completion, your role is to oversee the entire process - from getting the top {number_of_articles} news article urls and using the webpage_extractor for each of the urls to extract the text from the url, then pass to the news_article_aggregator to combine the text along with the source url and return back the final output to the user.",
        backstory="You're an experienced manager, skilled in overseeing complex projects and guiding teams to success. Your role is to coordinate the efforts of the crew members, ensuring that each task is completed on time and to the highest standard.",
        allow_delegation=True,
            llm=llm,
    )

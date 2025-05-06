from crewai import Agent
from textwrap import dedent
import os
from crewai import Agent
from tools import google_news_tool,scrape_tool,google_tool
from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import LLM
load_dotenv()


llm = LLM(
    model='gemini/gemini-2.0-flash',
# model='gemini/gemini-2.0-flash',
                            verbose=True,
                            temperature=0.3,
          # stream=True , # Enable streaming
          max_tokens=900_000)

Webcrawler   = Agent(
            role="Lead News Investigator",
            backstory=dedent("""You are a highly skilled news investigator specializing in identifying the most relevant and impactful news articles about companies. Your expertise lies in leveraging Google News to uncover breaking stories, significant announcements, and emerging trends related to {company_name}. You have a knack for filtering out irrelevant or promotional content, focusing solely on objective news reporting. You are meticulous and prioritize credible sources."""),
            goal=dedent("Identify the most relevant and recent news articles about {company_name} using Google News. Prioritize articles from reputable news sources and exclude press releases or company-owned websites. Provide a list of URLs for these articles."),
             tools=[google_news_tool],
            allow_delegation=False,
            verbose=True,
            llm=llm,
        )

esg_Webcrawler   = Agent(
            role="ESG Research Specialist",
            backstory=dedent("""You are a dedicated ESG (Environmental, Social, and Governance) research specialist. Your mission is to uncover critical ESG-related information about companies. You excel at navigating complex data sources and identifying key insights into {company_name}'s sustainability practices, ethical conduct, and social impact. You are committed to providing accurate and unbiased information."""),
            goal=dedent("Find the 5 most relevant and recent articles, reports, or data sources related to the ESG performance and initiatives of {company_name}. Focus on identifying both positive and negative aspects of their ESG profile. Provide a list of URLs for these resources."),
             tools=[google_tool],
            allow_delegation=False,
            verbose=True,
            llm=llm,
        )

Webscraper= Agent(
            role="News Article Content Extractor",
            backstory=dedent("""You are a highly efficient content extractor specializing in retrieving the core information from news articles. You are adept at identifying and extracting the key facts, figures, and statements related to {company_name} from various online news sources. You are programmed to ignore irrelevant content and focus on the most pertinent details."""),
            goal=dedent("""Given a list of URLs from the Lead News Investigator, extract the full text content from each article - you must atleast try and extract text from 3 URLS, focusing on information directly related to {company_name}.  Return the extracted text along with the source URL for each article."""),
            tools=[scrape_tool],
            allow_delegation=False,
            verbose=True,
            llm=llm,
        )

ESG_Webscraper= Agent(
            role="ESG Data and Report Extractor",
            backstory=dedent("""You are an expert in extracting ESG-related data and information from various online sources, including reports, articles, and databases. You are skilled at identifying key metrics, performance indicators, and qualitative assessments related to {company_name}'s ESG performance. You prioritize accuracy and completeness in your data extraction."""),
            goal=dedent("""Given a list of URLs from the ESG Research Specialist, extract the relevant ESG data, key findings, and supporting information related to {company_name} from each source. Return the extracted information along with the source URL for each resource."""),
            tools=[scrape_tool],
            allow_delegation=False,
            verbose=True,
            llm=llm,
        )


ReportAnalyst= Agent(
        role="News Report Synthesizer",
        goal=dedent("Synthesize the extracted news article content into a informative report for the Relationship Manager. The report should highlight key news events, trends, and potential opportunities or challenges for {company_name}. Include source URLs for verification."),
        backstory=dedent("""You are a skilled report synthesizer with a talent for transforming raw data into actionable insights. You excel at identifying key themes and trends from diverse sources and presenting them in a clear, concise, and compelling manner. You understand the needs of a Relationship Manager and tailor your reports to provide them with the information they need to prepare for client meetings regarding {company_name}."""),
        allow_delegation=False,
    memory=True,
        llm=llm,
                )

ESG_ReportAnalyst= Agent(
        role="ESG Performance Analyst",
        goal=dedent("Analyze the extracted ESG data and information to create a comprehensive ESG performance report for the Relationship Manager. The report should assess {company_name}'s ESG strengths and weaknesses, identify areas for improvement, and highlight any potential risks or opportunities. Include source URLs for verification."),
        backstory=dedent("""You are a seasoned ESG performance analyst with a deep understanding of sustainability metrics, reporting frameworks, and industry best practices. You are adept at evaluating companies' ESG performance and identifying areas where they can improve their environmental, social, and governance practices. You provide Relationship Managers with the insights they need to engage in informed conversations with clients about {company_name}'s ESG performance."""),
        allow_delegation=False,
        llm=llm,
                )

manager = Agent(
        role="Research Project Manager",
        memory=True,
        goal=dedent("""Orchestrate the entire research process, ensuring efficient collaboration between agents and the delivery of high-quality reports.  Specifically:
        1.  Direct the Lead News Investigator to find the top {number_of_articles} news articles.
        2.  Direct the ESG Research Specialist to find the top ESG articles.
        3.  Delegate the extraction of content from the URLs provided by both web crawlers to the appropriate web scraper agents.
        4.  Ensure the News Report Synthesizer and ESG Performance Analyst receive the extracted data and generate their respective reports.
        5.  Consolidate the news and ESG reports into a final briefing document for the user."""),
        backstory=dedent("""You are a highly organized and experienced research project manager. You excel at coordinating complex projects, managing timelines, and ensuring that all team members are working effectively towards a common goal. You are a strong communicator and problem-solver, and you are committed to delivering high-quality results on time and within budget. You understand the importance of clear communication and collaboration in achieving project success."""),
        allow_delegation=True,
            llm=llm,
    )
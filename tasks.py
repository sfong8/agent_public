# To know more about the Task class, visit: https://docs.crewai.com/concepts/tasks
from crewai import Task
from textwrap import dedent
from tools import google_news_tool,scrape_tool
from agents import *

google_news_search=Task(
            description=dedent(
                """
            Google news search for the latest news articles related to {company_name} and return a list URLS of the {number_of_articles} articles. - use google news as the search engine and search query should include 'recent news' 
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
This report should include some of the following if possible:
Latest Performance: A brief overview of the company's recent financial performance, including key metrics (e.g., revenue, profit, stock price if publicly traded) and any significant trends.
Good News : Highlight any positive news stories, achievements, successful product launches, strategic partnerships, or favorable industry trends that could be relevant to the client's business.
Bad News/Potential Challenges (: Identify any negative news, challenges, controversies, regulatory issues, or unfavorable market conditions that could impact the client's business or reputation.
Overall Sentiment: Provide a brief assessment of the overall sentiment surrounding the company based on the news you've gathered (e.g., "Generally positive," "Mixed," "Concerning").
potential Banking Product Opportunities: Identify any potential banking products or services that could be relevant to the client based on the news and developments you've summarized.
Future Outlook: If available, summarize any forward-looking statements or guidance provided by the company or analysts regarding its future prospects.
Key Risks: Highlight any key risks or uncertainties mentioned in the news that could impact the company's performance or reputation.
industry trends: Identify any relevant industry trends or developments that could impact the client's business or the banking relationship.
Source Citation: Always cite your sources so the relationship manager can easily verify the information.
Focus: Focus on news that would be relevant to a corporate banking relationship, such as financial performance, strategic initiatives, and potential risks.
"""
            ),
            expected_output="A fully fledge reports with the latest news about {company_name}",
            agent=ReportAnalyst,
            context=[webpage_extraction]
        )
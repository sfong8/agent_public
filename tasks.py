# To know more about the Task class, visit: https://docs.crewai.com/concepts/tasks
from crewai import Task
from textwrap import dedent
from tools import google_news_tool,scrape_tool,google_tool
from agents import *

google_news_search=Task(
            description=dedent(
                """
            Conduct a Google News search for the latest news articles related to {company_name}.  Focus on identifying articles from reputable news sources that provide objective reporting on the company's activities, performance, and industry context.  Return a list of URLs for the {number_of_articles} most relevant articles.  Important Note: Use google news as the search engine and The search query should include 'recent news' and exclude results from the company's own website or press release services.
        """
            ),
            expected_output="A list of {number_of_articles} URLs, each pointing to a recent news article from a reputable source about {company_name}.  Exclude URLs from the company's website or press release services.",
            tools=[google_news_tool],
            agent=Webcrawler,
        )

ESG_search=Task(
            description=dedent(
                """
            Use Google to find the most relevant webpages containing information about the ESG (Environmental, Social, and Governance) performance, policies, and initiatives of {company_name}. Return a list of URLs for the {number_of_articles} most relevant resources. The search query should include 'ESG policies and news' and should prioritize reports, articles, and data sources from reputable organizations and research institutions.
        """
            ),
            expected_output="A list of {number_of_articles} URLs, each pointing to a relevant resource (report, article, data source) providing information about the ESG performance, policies, and initiatives of {company_name}. Prioritize reputable sources.",
            tools=[google_tool],
            agent=esg_Webcrawler,
        )

webpage_extraction   = Task(
            description=dedent(
                """
            For each URL provided in the context, extract the full text content of the webpage, focusing on information directly related to {company_name}.  Identify and extract key facts, figures, statements, and events that are relevant to understanding the company's activities, performance, and industry context.  If extraction fails for a particular URL, log the failure and proceed to the next URL.
            Note: if the extracted text is too long (over 100k tokens) then summarize it to a maximum of 1000 words.
        """
            ),
            expected_output="A dictionary where each key is a URL from the context and the corresponding value is the extracted text content from that URL.  If extraction failed for a URL, the value should be an error message indicating the failure.",
            agent=Webscraper,
            tools=[scrape_tool],
            context=[google_news_search]
        )

esg_webpage_extraction   = Task(
            description=dedent(
                """
            For each URL provided in the context, extract the relevant ESG data, key findings, and supporting information related to {company_name}. Focus on extracting information about the company's environmental impact, social responsibility, and governance practices. If extraction fails for a particular URL, log the failure and proceed to the next URL.
        Note: if the extracted text (from url) is too long (over 100k tokens) then summarize it to a maximum of 1000 words.
        """
            ),
            expected_output="A dictionary where each key is a URL from the context and the corresponding value is the extracted ESG data and information from that URL. If extraction failed for a URL, the value should be an error message indicating the failure.",
            agent=ESG_Webscraper,
            tools=[scrape_tool],
            context=[ESG_search]
        )

createReport= Task(
            description=dedent("""
            Synthesize the extracted news article content into an informative report for the Relationship Manager. The report should include the following sections, if possible, based on the available information:

            *   **Latest Performance:** A brief overview of the company's recent financial performance, including key metrics (e.g., revenue, profit, stock price if publicly traded) and any significant trends.
            *   **Good News:** Highlight any positive news stories, achievements, successful product launches, strategic partnerships, or favorable industry trends.
            *   **Bad News/Potential Challenges:** Identify any negative news, challenges, controversies, regulatory issues, or unfavorable market conditions.
            *   **Overall Sentiment:** Provide a brief assessment of the overall sentiment surrounding the company (e.g., "Generally positive," "Mixed," "Concerning").
            *   **Potential Banking Product Opportunities:** Identify any potential banking products or services that could be relevant.
            *   **Future Outlook:** Summarize any forward-looking statements or guidance provided by the company or analysts.
            *   **Key Risks:** Highlight any key risks or uncertainties.
            *   **Industry Trends:** Identify any relevant industry trends or developments.

            Cite all sources using the URLs provided in the context.  Focus on news that would be relevant to a corporate banking relationship, such as financial performance, strategic initiatives, and potential risks.  Do not include dates in the report.  If no information is available for a particular section, omit that section.
            """
            ),
            expected_output="An informative report (use markdown bold for the headings, dont use ```) summarizing the latest news about {company_name}, with sections covering the topics listed in the description.  The report should be well-organized, clearly written, and cite all sources.",
            agent=ReportAnalyst,
            context=[webpage_extraction]
        )


createESGReport= Task(
            description=dedent("""
            Synthesize the extracted ESG data and information into a comprehensive ESG performance report for the Relationship Manager. The report should include the following sections, if possible, based on the available information:

            *   **Company Overview and Context:** Briefly describe the company's mission, vision, and values.
            *   **ESG Overview:** Summarize the company's ESG strategy, goals, and commitments.
            *   **ESG Performance Metrics:** Present the company's key ESG performance metrics and targets.
            *   **Environmental Factors (E):** Describe the company's environmental impact and initiatives.
            *   **Social Factors (S):** Describe the company's social responsibility efforts and performance.
            *   **Governance Factors (G):** Describe the company's governance practices and policies.
            *   **Areas of Concern:** Highlight any areas of concern or controversy related to the company's ESG practices.

            Cite all sources using the URLs provided in the context.  Do not include dates in the report.  If no information is available for a particular section, omit that section.
            """
            ),
            expected_output="A comprehensive ESG performance report for {company_name} (in markdown format using bold for headings,, dont use ```), with sections covering the topics listed in the description. The report should be well-organized, clearly written, and cite all sources.",
            agent=ESG_ReportAnalyst,
            context=[esg_webpage_extraction]
        )
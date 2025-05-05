## https://serper.dev/
import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool,ScrapeWebsiteTool
from sqlalchemy.testing.plugin.plugin_base import engines

# os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

# inititlaize the tool for internet searching capabilities
google_news_tool = SerperDevTool(engine="google news",n_results=20,search_type='news',country='gb',language='en')
google_tool = SerperDevTool(engine="google",n_results=20)

scrape_tool = ScrapeWebsiteTool()

# crawler = FirecrawlScrapeWebsiteTool(de)
from crew import crew,esg_crew
from datetime import datetime

today_date_str = datetime.now().strftime("%Y-%m-%d")
result = esg_crew.kickoff(inputs = {'company_name':'Barclays Bank', 'number_of_articles':10,'today_date':today_date_str})
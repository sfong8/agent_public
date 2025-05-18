from fpdf import FPDF
from datetime import datetime

# --- Configuration ---
COMPANY_NAME = "GreenLeaf Organics Ltd."
REPORT_YEAR = "2023"
CEO_NAME = "Jane Doe" # From previous context
OUTPUT_FILENAME = f"GreenLeaf_Organics_Annual_Report_{REPORT_YEAR}.pdf"

# --- Financial Figures (Fake but consistent with previous data) ---
TURNOVER = 3500000
NET_PROFIT = 450000
COST_OF_GOODS_SOLD = 1900000 # Invented
OPERATING_EXPENSES = 1000000 # Invented (Salaries, Rent, Marketing etc.)

# Derived Financials
GROSS_PROFIT = TURNOVER - COST_OF_GOODS_SOLD
OPERATING_PROFIT = GROSS_PROFIT - OPERATING_EXPENSES
# Assume some interest and tax for PBT and Net Profit to align
PROFIT_BEFORE_TAX = 550000 # Invented to lead to Net Profit
TAX_EXPENSE = PROFIT_BEFORE_TAX - NET_PROFIT

# Balance Sheet Figures (Invented, ensure Assets = Liabilities + Equity)
CASH = 300000
ACCOUNTS_RECEIVABLE = 450000
INVENTORY = 250000
TOTAL_CURRENT_ASSETS = CASH + ACCOUNTS_RECEIVABLE + INVENTORY

PROPERTY_PLANT_EQUIPMENT = 1500000 # Net
TOTAL_NON_CURRENT_ASSETS = PROPERTY_PLANT_EQUIPMENT
TOTAL_ASSETS = TOTAL_CURRENT_ASSETS + TOTAL_NON_CURRENT_ASSETS

ACCOUNTS_PAYABLE = 300000
SHORT_TERM_DEBT = 100000 # Could be part of the existing bank loan
TOTAL_CURRENT_LIABILITIES = ACCOUNTS_PAYABLE + SHORT_TERM_DEBT

LONG_TERM_DEBT = 700000 # Could include the FinSecure Lenders PLC loan
TOTAL_NON_CURRENT_LIABILITIES = LONG_TERM_DEBT
TOTAL_LIABILITIES = TOTAL_CURRENT_LIABILITIES + TOTAL_NON_CURRENT_LIABILITIES

SHARE_CAPITAL = 500000
RETAINED_EARNINGS = TOTAL_ASSETS - TOTAL_LIABILITIES - SHARE_CAPITAL # Calculated to balance
TOTAL_EQUITY = SHARE_CAPITAL + RETAINED_EARNINGS


class PDFReport(FPDF):
    def header(self):
        self.set_font("Times", "B", 16)
        self.cell(0, 10, COMPANY_NAME, 0, 1, "C")
        self.set_font("Times", "B", 14)
        self.cell(0, 10, f"Annual Report for the Year Ended December 31, {str(REPORT_YEAR)}", 0, 1, "C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Times", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}} - {COMPANY_NAME} Annual Report {REPORT_YEAR}", 0, 0, "C")

    def chapter_title(self, title):
        self.set_font("Times", "B", 14)
        self.set_fill_color(230, 230, 230) # Light grey
        self.cell(0, 10, title, 0, 1, "L", fill=True)
        self.ln(5)

    def chapter_body(self, text_content):
        self.set_font("Times", "", 12)
        self.multi_cell(0, 7, text_content)
        self.ln()

    def add_financial_table(self, title, data, headers, col_widths, currency_symbol="GBP"):
        self.set_font("Times", "B", 12)
        self.cell(0, 10, title, 0, 1, "L")
        self.set_font("Times", "B", 10)
        self.set_fill_color(240, 240, 240)
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 7, header, 1, 0, "C", fill=True)
        self.ln()

        self.set_font("Times", "", 10)
        for row in data:
            for i, item in enumerate(row):
                if isinstance(item, (int, float)) and i > 0: # Format numbers, skip first column if it's a label
                    text = f"{currency_symbol} {item:,.0f}"
                else:
                    text = str(item)
                self.cell(col_widths[i], 7, text, 1, 0, "L" if i == 0 else "R")
            self.ln()
        self.ln(5)

# --- Create PDF Document ---
pdf = PDFReport()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=20) # Increased margin for report feel
pdf.set_left_margin(20)
pdf.set_right_margin(20)

# --- Title Page (Simplified) ---
pdf.set_font("Times", "B", 24)
pdf.cell(0, 50, "", 0, 1) # Spacer
pdf.cell(0, 20, COMPANY_NAME, 0, 1, "C")
pdf.set_font("Times", "B", 18)
pdf.cell(0, 15, "Annual Report", 0, 1, "C")
pdf.set_font("Times", "", 16)
pdf.cell(0, 10, f"Year Ended December 31, {REPORT_YEAR}", 0, 1, "C")
pdf.cell(0, 60, "", 0, 1) # Spacer
pdf.set_font("Times", "", 10)
pdf.cell(0, 10, "Registered Office: Unit 5, Willowbrook Industrial Estate, Reading, RG2 0TD", 0, 1, "C")
pdf.cell(0, 10, "Company Registration No: 09876543", 0, 1, "C")
pdf.add_page()

# --- Table of Contents (Simplified) ---
pdf.chapter_title("Table of Contents")
pdf.set_font("Times", "", 12)
toc_items = [
    ("Letter from the CEO", 3), # Assuming page numbers, adjust if content changes
    ("Our Company & Mission", 4),
    (f"Operational Highlights {REPORT_YEAR}", 5),
    (f"Financial Highlights {REPORT_YEAR}", 6),
    ("Simplified Financial Statements", 7),
    ("  - Statement of Profit & Loss", 7),
    ("  - Statement of Financial Position (Balance Sheet)", 8),
    ("Future Outlook & Strategy", 9),
    ("Contact Information", 10),
]
for item, page_num in toc_items:
    pdf.cell(0, 7, f"{item} .................................................................... Page {page_num}", 0, 1, "L") # Basic dotted line
pdf.ln(10)
pdf.add_page() # Start CEO letter on a new page

# --- Letter from the CEO ---
pdf.chapter_title(f"Letter from the CEO - {CEO_NAME}")
ceo_letter = f"""
Dear Stakeholders,

It is with great pleasure that I present the Annual Report for GreenLeaf Organics Ltd. for the year ended December 31, {REPORT_YEAR}. This past year has been one of significant growth and achievement for our company, driven by our unwavering commitment to providing high-quality, sustainable organic products to our valued customers.

We saw a remarkable 40% increase in turnover, reaching GBP {TURNOVER:,.0f}, and a net profit of GBP {NET_PROFIT:,.0f}. These results reflect the hard work of our dedicated team, the loyalty of our customers, and the growing consumer demand for healthy, ethically sourced food.

During {REPORT_YEAR}, we successfully launched two new organic juice lines, expanded our distribution network to include 'HealthyHarvest' retail chains, and continued to invest in sustainable farming practices. Our focus remains on innovation, quality, and environmental responsibility.

Looking ahead, we are excited about the opportunities for further expansion. We are actively planning significant investments to enhance our production capabilities, including a new state-of-the-art bottling and packaging line, to meet the escalating demand for our products and to further broaden our market reach. This strategic investment, estimated at around GBP 750,000, is central to our growth plans for the coming years.

Thank you for your continued support of GreenLeaf Organics Ltd.

Sincerely,

{CEO_NAME}
CEO, GreenLeaf Organics Ltd.
"""
pdf.chapter_body(ceo_letter)
pdf.add_page()

# --- Our Company & Mission ---
pdf.chapter_title("Our Company & Mission")
company_mission = f"""
{COMPANY_NAME} is a leading producer of certified organic food and beverages in the UK. Founded with the vision of making healthy, delicious, and sustainably produced food accessible to everyone, we have grown from a small local enterprise into a recognized brand synonymous with quality and integrity.

Our Mission:
To nourish our customers and the planet by cultivating and crafting the finest organic products, adhering to the highest standards of quality, sustainability, and ethical practices.

Our Values:
- Quality: Uncompromising standards from farm to table.
- Sustainability: Protecting the environment for future generations.
- Integrity: Transparency and honesty in all our dealings.
- Community: Supporting local farmers and fostering healthy lifestyles.
"""
pdf.chapter_body(company_mission)
pdf.add_page()

# --- Operational Highlights ---
pdf.chapter_title(f"Operational Highlights {REPORT_YEAR}")
op_highlights = f"""
The year {REPORT_YEAR} was marked by several key operational achievements:

- Production Increase: Scaled up production capacity by 25% across our core product ranges to meet growing demand.
- New Product Launches: Successfully introduced two new lines of organic cold-pressed juices and a range of gluten-free organic snacks.
- Expanded Distribution: Secured new partnerships with national retail chain 'HealthyHarvest' and several independent health food stores, increasing our product availability by 30%.
- Sustainability Initiatives: Implemented a new water recycling program at our primary processing facility, reducing water consumption by 15%. Transitioned to 100% recyclable packaging for 70% of our product lines.
- Quality Assurance: Maintained our Grade AA BRCGS Food Safety Certification and received the "Organic Excellence Award {REPORT_YEAR}" from the National Organic Producers Association (fictional).
- Team Growth: Expanded our dedicated team by 15%, particularly in production and quality control, to support our growth trajectory.
"""
pdf.chapter_body(op_highlights)
pdf.add_page()

# --- Financial Highlights ---
pdf.chapter_title(f"Financial Highlights {REPORT_YEAR}")
fin_highlights_text = f"""
{COMPANY_NAME} delivered a strong financial performance in {REPORT_YEAR}, demonstrating robust growth and profitability.

Key Financial Metrics:
- Turnover: GBP {TURNOVER:,.0f} (a 40% increase from 2022)
- Gross Profit: GBP {GROSS_PROFIT:,.0f} (Gross Profit Margin: {GROSS_PROFIT/TURNOVER*100:.1f}%)
- Operating Profit: GBP {OPERATING_PROFIT:,.0f}
- Net Profit: GBP {NET_PROFIT:,.0f} (a 25% increase from 2022)
- Net Asset Position: Healthy and strengthening, supporting future investments.

This performance underscores the company's strong market position and effective operational management.
"""
pdf.chapter_body(fin_highlights_text)
pdf.add_page()

# --- Simplified Financial Statements ---
pdf.chapter_title("Simplified Financial Statements")

# Statement of Profit & Loss
pnl_headers = ["Description", f"Year Ended Dec 31, {REPORT_YEAR}"]
pnl_col_widths = [100, 70]
pnl_data = [
    ["Revenue (Turnover)", TURNOVER],
    ["Cost of Goods Sold", -COST_OF_GOODS_SOLD],
    ["Gross Profit", GROSS_PROFIT],
    ["Operating Expenses", -OPERATING_EXPENSES],
    ["Operating Profit", OPERATING_PROFIT],
    ["Interest Expense (Net)", -(PROFIT_BEFORE_TAX - OPERATING_PROFIT) if OPERATING_PROFIT > PROFIT_BEFORE_TAX else 0], # Simplified
    ["Profit Before Tax", PROFIT_BEFORE_TAX],
    ["Tax Expense", -TAX_EXPENSE],
    ["Net Profit for the Year", NET_PROFIT],
]
pdf.add_financial_table(f"Statement of Profit & Loss", pnl_data, pnl_headers, pnl_col_widths)

pdf.add_page() # Ensure Balance Sheet starts on a new page if P&L is long
pdf.chapter_title("Simplified Financial Statements (Continued)") # Title for BS page

# Statement of Financial Position (Balance Sheet)
bs_headers = ["Description", f"As at Dec 31, {REPORT_YEAR}"]
bs_col_widths = [100, 70]
bs_data_assets = [
    ["ASSETS", ""],
    ["Current Assets", ""],
    ["  Cash & Cash Equivalents", CASH],
    ["  Accounts Receivable", ACCOUNTS_RECEIVABLE],
    ["  Inventory", INVENTORY],
    ["Total Current Assets", TOTAL_CURRENT_ASSETS],
    ["Non-Current Assets", ""],
    ["  Property, Plant & Equipment (Net)", PROPERTY_PLANT_EQUIPMENT],
    ["Total Non-Current Assets", TOTAL_NON_CURRENT_ASSETS],
    ["TOTAL ASSETS", TOTAL_ASSETS],
]
bs_data_liabilities_equity = [
    ["LIABILITIES & EQUITY", ""],
    ["Current Liabilities", ""],
    ["  Accounts Payable", ACCOUNTS_PAYABLE],
    ["  Short-Term Debt", SHORT_TERM_DEBT],
    ["Total Current Liabilities", TOTAL_CURRENT_LIABILITIES],
    ["Non-Current Liabilities", ""],
    ["  Long-Term Debt", LONG_TERM_DEBT],
    ["Total Non-Current Liabilities", TOTAL_NON_CURRENT_LIABILITIES],
    ["TOTAL LIABILITIES", TOTAL_LIABILITIES],
    ["Equity", ""],
    ["  Share Capital", SHARE_CAPITAL],
    ["  Retained Earnings", RETAINED_EARNINGS],
    ["TOTAL EQUITY", TOTAL_EQUITY],
    ["TOTAL LIABILITIES & EQUITY", TOTAL_LIABILITIES + TOTAL_EQUITY], # Should match TOTAL_ASSETS
]
pdf.add_financial_table(f"Statement of Financial Position (Balance Sheet) - Assets", bs_data_assets, bs_headers, bs_col_widths)
pdf.add_financial_table(f"Statement of Financial Position (Balance Sheet) - Liabilities & Equity", bs_data_liabilities_equity, bs_headers, bs_col_widths)
pdf.add_page()

# --- Future Outlook & Strategy ---
pdf.chapter_title("Future Outlook & Strategy")
future_outlook = f"""
{COMPANY_NAME} is poised for continued growth in the expanding organic food market. Our strategy for the coming years focuses on three key pillars:

1.  Capacity Expansion & Efficiency:
    As mentioned by our CEO, a primary focus is the investment of approximately GBP 750,000 in a new, automated bottling and packaging line. This will significantly increase our production capacity for high-demand products like organic juices and sauces, reduce per-unit costs, and improve overall operational efficiency. This project is expected to be commissioned by Q3 {REPORT_YEAR_PLUS_ONE if 'REPORT_YEAR_PLUS_ONE' in locals() else int(REPORT_YEAR) + 1}.

2.  Market Development & Product Innovation:
    We will continue to explore new product categories that align with our brand ethos and consumer trends. Further expansion into national retail channels and exploration of export markets are key objectives. We aim to increase our market share by 5% in the next two years.

3.  Strengthening Sustainability Practices:
    We are committed to becoming a leader in sustainable organic food production. Future initiatives include achieving carbon neutrality in our operations by {int(REPORT_YEAR) + 5} and expanding our support for local organic farming cooperatives.

We are confident that these strategic initiatives will deliver sustainable value for our stakeholders and further solidify {COMPANY_NAME}'s position as a trusted name in organic foods.
"""
pdf.chapter_body(future_outlook.replace("REPORT_YEAR_PLUS_ONE", str(int(REPORT_YEAR)+1))) # Ensure replacement
pdf.add_page()

# --- Contact Information ---
pdf.chapter_title("Contact Information")
contact_info = f"""
{COMPANY_NAME}

Registered Office:
Unit 5, Willowbrook Industrial Estate
Reading, Berkshire
RG2 0TD
United Kingdom

General Enquiries:
Email: info@greenleaforganics.co.uk
Phone: +44 (0)118 9XXXXXX

Website:
www.greenleaforganics.co.uk

Investor Relations:
For investor-related queries, please contact:
Email: investors@greenleaforganics.co.uk
"""
pdf.chapter_body(contact_info)

# --- Output the PDF ---
try:
    pdf.output(OUTPUT_FILENAME, "F")
    print(f"PDF '{OUTPUT_FILENAME}' generated successfully.")
except Exception as e:
    print(f"Error generating PDF: {e}")
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
import os
import shutil

pdf_path_downloads = r'C:\Users\Akhil\Downloads\CodSoft_LinkedIn_Video_Script.pdf'
pdf_path_repo = r'c:\Projects\Codesoft\CodSoft_LinkedIn_Video_Script.pdf'

doc = SimpleDocTemplate(
    pdf_path_downloads,
    pagesize=letter,
    rightMargin=40, leftMargin=40, topMargin=36, bottomMargin=36
)

styles = getSampleStyleSheet()

# Custom Palette
c_navy = colors.HexColor('#0f2942')
c_blue = colors.HexColor('#1d4ed8')
c_bg_card = colors.HexColor('#f8fafc')
c_border = colors.HexColor('#cbd5e1')
c_text_dark = colors.HexColor('#1e293b')

# Styles
title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=20,
    leading=24,
    textColor=c_navy,
    alignment=1,
    spaceAfter=4
)

subtitle_style = ParagraphStyle(
    'DocSubTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=10.5,
    leading=14,
    textColor=colors.HexColor('#475569'),
    alignment=1,
    spaceAfter=10
)

section_heading = ParagraphStyle(
    'SectionHeading',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=12,
    leading=15,
    textColor=c_blue,
    spaceBefore=8,
    spaceAfter=6
)

part_title = ParagraphStyle(
    'PartTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=13,
    textColor=c_navy,
    spaceBefore=2,
    spaceAfter=2
)

script_body = ParagraphStyle(
    'ScriptBody',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=9,
    leading=12.5,
    textColor=c_text_dark
)

screen_action = ParagraphStyle(
    'ScreenAction',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=11,
    textColor=colors.HexColor('#2563eb'),
    spaceAfter=2
)

tbl_header = ParagraphStyle('THeader', fontName='Helvetica-Bold', fontSize=8.5, leading=11, textColor=c_navy)
tbl_cell = ParagraphStyle('TCell', fontName='Helvetica', fontSize=8, leading=10.5, textColor=c_text_dark)

caption_text = ParagraphStyle(
    'CaptionText',
    fontName='Courier',
    fontSize=8.5,
    leading=12,
    textColor=colors.HexColor('#1e293b')
)

elements = []

# Title & Subtitle
elements.append(Paragraph('CodSoft Data Analytics Virtual Internship', title_style))
elements.append(Paragraph('LinkedIn Video Recording Script & Post Guide (90-Second Presentation)', subtitle_style))

# Blue Decorative Line
elements.append(HRFlowable(width='100%', thickness=2, color=c_blue, spaceBefore=0, spaceAfter=8))

# Section 1: Presentation Timeline & Visual Guide
elements.append(Paragraph('■■ Presentation Timeline & Visual Guide', section_heading))

table_data = [
    [Paragraph('Time', tbl_header), Paragraph('Topic / Section', tbl_header), Paragraph('On-Screen Visual Action', tbl_header)],
    [Paragraph('0:00 - 0:15', tbl_cell), Paragraph('Intro & Project Overview', tbl_cell), Paragraph('On Camera or VS Code project overview', tbl_cell)],
    [Paragraph('0:15 - 0:35', tbl_cell), Paragraph('Tasks 1 & 2 (Data Cleaning & EDA)', tbl_cell), Paragraph('Show cleaned_dataset.csv & eda_report.md', tbl_cell)],
    [Paragraph('0:35 - 1:00', tbl_cell), Paragraph('Task 3 (Live Web Dashboard)', tbl_cell), Paragraph('Show Live Web Dashboard in Browser', tbl_cell)],
    [Paragraph('1:00 - 1:25', tbl_cell), Paragraph('Tasks 4 & 5 (ML & Web Scraping)', tbl_cell), Paragraph('Show customer_rfm_scatter.png & scraped_products.csv', tbl_cell)],
    [Paragraph('1:25 - 1:45', tbl_cell), Paragraph('GitHub Link & Thank You', tbl_cell), Paragraph('Show GitHub Repo URL at github.com/workwithme2003-cmyk', tbl_cell)]
]

t = Table(table_data, colWidths=[70, 190, 272])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('LEFTPADDING', (0,0), (-1,-1), 6),
    ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ('GRID', (0,0), (-1,-1), 0.5, c_border),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_card]),
]))
elements.append(t)
elements.append(Spacer(1, 10))

# Section 2: Word-for-Word Speaking Script
elements.append(Paragraph('■■ Word-for-Word Speaking Script', section_heading))

# Part 1
p1_text = '"Hi everyone! I am excited to share that I have completed the Data Analytics Virtual Internship at CodSoft! Over the past month, I built five end-to-end data analytics pipelines using Python, Pandas, Machine Learning, and Interactive Dashboards to solve real-world business analytics challenges."'
p1_data = [[Paragraph('Part 1: Introduction & Overview (0:00 - 0:15)', part_title)], [Paragraph(p1_text, script_body)]]
t1 = Table(p1_data, colWidths=[532])
t1.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), c_bg_card),
    ('BOX', (0,0), (-1,-1), 0.5, c_border),
    ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8),
]))
elements.append(t1)
elements.append(Spacer(1, 6))

# Part 2
p2_text = '"In Task 1: Data Cleaning and Preprocessing, I imported raw transactional data, handled missing entries with median imputation, removed duplicate records, standardized text categories, and formatted ISO dates to create a clean, 100% complete dataset.<br/><br/>In Task 2: Exploratory Data Analysis, I analyzed feature distributions, evaluated skewness, and used Interquartile Range (IQR) outlier detection to discover key revenue drivers and discount impact on profit margins."'
p2_data = [[Paragraph('Part 2: Tasks 1 & 2 — Data Cleaning & EDA (0:15 - 0:35)', part_title)], [Paragraph(p2_text, script_body)]]
t2 = Table(p2_data, colWidths=[532])
t2.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), c_bg_card),
    ('BOX', (0,0), (-1,-1), 0.5, c_border),
    ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8),
]))
elements.append(t2)
elements.append(Spacer(1, 6))

# Part 3
p3_text = '"For Task 3: Data Visualization, I built an interactive executive sales dashboard featuring bordered card containers, KPI metrics with live trend sparklines, dynamic region and category filtering, and instant CSV exports. It is also deployed live on the web!"'
p3_data = [
    [Paragraph('Part 3: Task 3 — Interactive Web Dashboard (0:35 - 1:00)', part_title)],
    [Paragraph('[Screen Action: Click on sidebar filters in your live web dashboard app]', screen_action)],
    [Paragraph(p3_text, script_body)]
]
t3 = Table(p3_data, colWidths=[532])
t3.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), c_bg_card),
    ('BOX', (0,0), (-1,-1), 0.5, c_border),
    ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8),
]))
elements.append(t3)
elements.append(Spacer(1, 6))

# Part 4
p4_text = '"In Task 4: Customer Segmentation, I evaluated RFM — Recency, Frequency, and Monetary — metrics and trained a K-Means Machine Learning Clustering model to group customers into VIP Champions, Loyal High-Value, and At-Risk segments with targeted marketing strategies.<br/><br/>Finally, in Task 5: Web Data Extraction, I built an automated web scraper using BeautifulSoup and regex numerical parsing to extract product titles, prices, star ratings, and stock availability into structured CSV and Excel files."'
p4_data = [[Paragraph('Part 4: Tasks 4 & 5 — ML Customer Clustering & Web Scraping (1:00 - 1:25)', part_title)], [Paragraph(p4_text, script_body)]]
t4 = Table(p4_data, colWidths=[532])
t4.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), c_bg_card),
    ('BOX', (0,0), (-1,-1), 0.5, c_border),
    ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8),
]))
elements.append(t4)
elements.append(Spacer(1, 6))

# Part 5
p5_text = '"All five tasks, complete source code, visual charts, and comprehensive analytical reports are live on my public GitHub repository, and the interactive web dashboard is accessible online!<br/><br/>A sincere thank you to @CodSoft for this enriching learning experience. Please check out the GitHub link in my caption. Thank you!"'
p5_data = [[Paragraph('Part 5: Conclusion & GitHub Call-To-Action (1:25 - 1:45)', part_title)], [Paragraph(p5_text, script_body)]]
t5 = Table(p5_data, colWidths=[532])
t5.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), c_bg_card),
    ('BOX', (0,0), (-1,-1), 0.5, c_border),
    ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8),
]))
elements.append(t5)
elements.append(Spacer(1, 10))

# Section 3: Text Caption for LinkedIn Post
elements.append(Paragraph('■ Text Caption for LinkedIn Post', section_heading))

caption_body = '''Excited to share that I have completed my Data Analytics Virtual Internship at @CodSoft! 🚀<br/><br/>
During this program, I built 5 end-to-end Data Analytics projects:<br/>
1. ■ Data Cleaning & Preprocessing (Pandas, Deduplication, Imputation)<br/>
2. ■ Exploratory Data Analysis (Descriptive Stats, IQR Outliers, Correlation)<br/>
3. ■ Interactive Data Visualization Dashboard (Interactive Web App & Plotly)<br/>
4. ■ Customer Segmentation (RFM Analysis & K-Means Machine Learning)<br/>
5. ■ Web Data Extraction (BeautifulSoup Web Scraper & Trend Analysis)<br/><br/>
■ Live Web Dashboard: https://raw.githack.com/workwithme2003-cmyk/CODSOFT_DataAnalytics/main/index.html<br/>
■ GitHub Repository: https://github.com/workwithme2003-cmyk/CODSOFT_DataAnalytics<br/><br/>
Thank you @CodSoft for this valuable learning experience!<br/><br/>
#codsoft #cip #dataanalytics #python #machinelearning #internship #streamlit #datascience'''

t_cap = Table([[Paragraph(caption_body, caption_text)]], colWidths=[532])
t_cap.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f1f5f9')),
    ('BOX', (0,0), (-1,-1), 0.5, c_border),
    ('TOPPADDING', (0,0), (-1,-1), 8), ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('LEFTPADDING', (0,0), (-1,-1), 10), ('RIGHTPADDING', (0,0), (-1,-1), 10),
]))
elements.append(t_cap)

doc.build(elements)

shutil.copy(pdf_path_downloads, pdf_path_repo)
print('Successfully generated PDF at both locations!')

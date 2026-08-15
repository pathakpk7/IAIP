# Task 1 — Sales Data Analysis

## Intern Alpha Data Analytics Internship

A comprehensive exploratory data analysis project completed as part of my **Data Analytics Internship at Intern Alpha**.

The project analyzes the **Sample Superstore** dataset to understand sales performance, profitability, customer segments, product performance, regional trends, seasonal patterns, and the relationship between discounts and profitability.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [Dataset](#dataset)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Data Preparation](#data-preparation)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Key Performance Indicators](#key-performance-indicators)
- [Sales Trend Analysis](#sales-trend-analysis)
- [Seasonal Analysis](#seasonal-analysis)
- [Customer Segment Analysis](#customer-segment-analysis)
- [Category Analysis](#category-analysis)
- [Product and Sub-Category Analysis](#product-and-sub-category-analysis)
- [Regional Analysis](#regional-analysis)
- [Discount and Profitability Analysis](#discount-and-profitability-analysis)
- [Key Business Insights](#key-business-insights)
- [Business Recommendations](#business-recommendations)
- [Visualizations](#visualizations)
- [How to Run](#how-to-run)
- [Conclusion](#conclusion)

---

# Project Overview

The objective of this project is to analyze retail sales data and transform raw transactional information into meaningful business insights.

The analysis focuses on:

- Overall sales performance
- Profitability
- Sales growth over time
- Monthly and seasonal trends
- Customer segment performance
- Category and sub-category performance
- Product-level profitability
- Regional performance
- Discounting patterns
- Relationship between discounts and profit

The project follows a complete data-analysis workflow:

```text
Raw Dataset
     ↓
Data Quality Assessment
     ↓
Data Cleaning
     ↓
Feature Engineering
     ↓
Exploratory Data Analysis
     ↓
Trend Analysis
     ↓
Seasonal Analysis
     ↓
Product Analysis
     ↓
Regional Analysis
     ↓
Profitability Analysis
     ↓
Business Insights
     ↓
Recommendations


Objectives

The primary objectives of this analysis are:

Analyze overall sales and profitability.
Identify yearly and monthly sales trends.
Identify recurring seasonal patterns.
Determine the strongest customer segments.
Evaluate category and sub-category performance.
Identify high-performing and loss-making products.
Compare sales and profitability across regions.
Investigate the relationship between discount levels and profitability.
Identify potential business risks and opportunities.
Develop data-driven recommendations.
Dataset
Dataset Name

Sample Superstore

The dataset contains retail transaction records covering orders, customers, products, categories, regions, sales, discounts, quantities, and profits.

Dataset Size
Rows: 9,994
Original Columns: 21
Analysis Period: January 2014 – December 2017
Missing Values: 0
Duplicate Rows: 0
Original Columns
Row ID
Order ID
Order Date
Ship Date
Ship Mode
Customer ID
Customer Name
Segment
Country
City
State
Postal Code
Region
Product ID
Category
Sub-Category
Product Name
Sales
Quantity
Discount
Profit
Technologies Used
Technology	Purpose
Python	Data analysis and processing
Pandas	Data manipulation and aggregation
NumPy	Numerical operations
Matplotlib	Data visualization
Seaborn	Statistical visualization
Jupyter Notebook	Interactive analysis environment
Project Structure
Task-1-Sales-Data-Analysis/
│
├── data/
│   └── Sample - Superstore.csv
│
├── notebooks/
│   └── sales_data_analysis.ipynb
│
├── outputs/
│   ├── yearly_sales_trend.png
│   ├── monthly_sales_trend.png
│   ├── seasonal_sales_pattern.png
│   ├── sales_heatmap.png
│   ├── sales_vs_profit.png
│   ├── category_performance.png
│   ├── subcategory_profitability.png
│   └── discount_vs_profit.png
│
├── README.md
└── requirements.txt
Data Preparation

Before beginning the analysis, the dataset was inspected for data-quality issues.

Data Quality Checks

The following checks were performed:

Missing-value analysis
Duplicate-record analysis
Data-type inspection
Numerical-value validation
Date-format validation
Date-range verification
Results
Check	Result
Total Records	9,994
Original Columns	21
Missing Values	0
Duplicate Rows	0
Invalid Quantity Values	0
Invalid Sales Values	0
Discounts Above 100%	0

The Order Date and Ship Date columns were converted into Pandas datetime format.

Feature Engineering

Additional time-based features were created from the Order Date column.

New Features
Year
Month
Month Name
Quarter
Year-Month

These features were used for:

Yearly trend analysis
Monthly trend analysis
Seasonal analysis
Year-month comparisons
Sales heatmap generation
Exploratory Data Analysis

The exploratory analysis examined:

Sales distribution
Profit distribution
Sales vs Profit
Customer segments
Product categories
Product sub-categories
Regional performance
Discount levels

The analysis was designed to evaluate both revenue generation and profitability, rather than relying on sales alone.

Key Performance Indicators

The following KPIs were calculated from the dataset.

KPI	Result
Total Sales	$2,297,200.86
Total Profit	$286,397.02
Total Quantity Sold	37,873
Total Orders	5,009
Unique Customers	793
Unique Products	1,862
Overall Profit Margin	12.47%

The results provide a high-level overview of the business performance represented by the dataset.

Sales Trend Analysis
Yearly Performance
Year	Sales	Profit	Sales Growth
2014	$484,247	$49,544	—
2015	$470,533	$61,619	-2.83%
2016	$609,206	$81,795	+29.47%
2017	$733,215	$93,439	+20.36%
Observation

Sales increased from approximately $484K in 2014 to approximately $733K in 2017.

This represents approximately 51% growth over the analysis period.

Although sales declined slightly in 2015, the business experienced strong growth in:

2016: +29.47%
2017: +20.36%

Profit also increased each year across the four-year period.

Seasonal Analysis

Monthly sales were aggregated across years to identify recurring seasonal patterns.

The strongest average annual sales were observed during the later months of the year.

Average Annual Sales by Calendar Month
Month	Average Annual Sales
January	$23,731
February	$14,938
March	$51,251
April	$34,441
May	$38,757
June	$38,180
July	$36,810
August	$39,761
September	$76,912
October	$50,081
November	$88,115
December	$81,323
Observation

November recorded the highest average annual sales, while February recorded the lowest.

The stronger performance during November and December indicates a significant year-end sales pattern.

Customer Segment Analysis

The dataset contains three customer segments:

Consumer
Corporate
Home Office
Segment Performance
Segment	Sales	Profit	Orders	Customers
Consumer	$1,161,401	$134,119	2,586	409
Corporate	$706,146	$91,979	1,514	236
Home Office	$429,653	$60,299	909	148
Observation

The Consumer segment contributes the largest share of sales, profit, orders, and customers among the three segments.

Category Analysis

The dataset contains three major product categories:

Technology
Furniture
Office Supplies
Category Performance
Category	Sales	Profit
Technology	$836,154	$145,455
Furniture	$742,000	$18,451
Office Supplies	$719,047	$122,491
Observation

Technology is the strongest category in terms of both sales and profit.

Furniture generates substantial sales but comparatively lower profit, making its profitability worth further investigation.

Product and Sub-Category Analysis

The analysis was extended from major categories to individual sub-categories.

Highest Sales Sub-Categories
Sub-Category	Sales	Profit
Phones	$330,007	$44,516
Chairs	$328,449	$26,590
Storage	$223,844	$21,279
Tables	$206,966	-$17,725
Binders	$203,413	$30,222
Important Finding

The Tables sub-category generated approximately:

$206,966 in sales
-$17,725 in profit
-8.56% profit margin

This demonstrates that high sales volume does not necessarily indicate strong business performance.

Sub-Category Profitability

Several sub-categories showed significant differences between sales and profitability.

Sub-Category	Sales	Profit	Profit Margin
Tables	$206,966	-$17,725	-8.56%
Bookcases	$114,880	-$3,473	-3.02%
Supplies	$46,674	-$1,189	-2.55%
Machines	$189,239	$3,385	1.79%
Chairs	$328,449	$26,590	8.10%
Phones	$330,007	$44,516	13.49%
Accessories	$167,380	$41,937	25.05%
Copiers	$149,528	$55,618	37.20%
Observation

The Copiers sub-category generated significantly higher profitability relative to its sales volume.

In contrast, Tables, Bookcases, and Supplies generated negative aggregate profitability.

Regional Analysis

The dataset contains four regions:

West
East
Central
South
Regional Performance
Region	Sales	Profit	Profit Margin
West	$725,458	$108,418	14.94%
East	$678,781	$91,523	13.48%
Central	$501,240	$39,706	7.92%
South	$391,722	$46,749	11.93%
Observation

The West region achieved the strongest combination of sales, profit, and profit margin.

The Central region has a substantially lower profit margin compared with the West.

This difference may warrant further investigation into:

Product mix
Pricing
Discounting
Regional demand
Operating costs
Discount and Profitability Analysis

Discount levels were analyzed to investigate their relationship with profitability.

Discount-Level Performance
Discount	Sales	Profit	Profit Margin
0%	$1,087,908	$320,988	29.51%
10%	$54,369	$9,029	16.61%
15%	$27,559	$1,419	5.15%
20%	$764,594	$90,337	11.82%
30%	$103,227	-$10,369	-10.05%
40%	$116,418	-$23,057	-19.81%
50%	$58,919	-$20,506	-34.80%
60%	$6,645	-$5,945	-89.46%
70%	$40,620	-$40,075	-98.66%
80%	$16,964	-$30,539	-180.03%
Observation

Higher discount levels show a strong association with lower profitability.

Aggregate profitability becomes negative at discount levels of 30% and above.

At an 80% discount level, the aggregate profit margin falls to approximately -180%.

Note: This analysis identifies an association between discount levels and profitability. It does not by itself establish that discounts are the sole cause of losses.

Profitable vs Loss-Making Transactions

Transactions were divided into two groups based on whether their recorded profit was positive or negative.

Transaction Type	Transactions	Sales	Profit	Average Discount
Profitable	8,123	$1,828,494	$442,528	8.14%
Loss	1,871	$468,707	-$156,131	48.09%
Observation

Loss-making transactions received a substantially higher average discount than profitable transactions:

Profitable transactions → 8.14% average discount


Loss-making transactions → 48.09% average discount

This supports the need for further investigation of discounting strategies.

Key Business Insights

Based on the complete analysis, the following insights were identified.

1. Strong Long-Term Sales Growth

Sales increased by approximately 51% between 2014 and 2017.

The strongest growth occurred in 2016 and 2017.

2. Strong Year-End Seasonality

November and December showed the strongest average annual sales, while February was the weakest month.

3. Technology Is the Strongest Major Category

Technology generated approximately $836K in sales and $145K in profit, making it the strongest major category by profitability.

4. Revenue Does Not Always Equal Profitability

The Tables sub-category generated more than $206K in sales but lost approximately $17.7K.

5. High Discounts Are Associated With Lower Profitability

Aggregate profitability becomes negative at discount levels of 30% or higher.

6. Loss-Making Transactions Have Higher Average Discounts

Loss-making transactions had an average discount of approximately 48.1%, compared with 8.1% for profitable transactions.

7. Regional Profitability Varies

The West region achieved a 14.94% profit margin, while the Central region achieved only 7.92%.

Business Recommendations
1. Review High-Discount Pricing

Discount levels of 30% or higher should be carefully evaluated because these levels are associated with negative aggregate profitability.

2. Reassess the Tables Sub-Category

The Tables sub-category should be investigated at the product level.

Potential areas of investigation include:

Product pricing
Procurement costs
Discount levels
Product margins
Product demand
3. Prioritize Profitable Products

High-margin products and sub-categories should be considered alongside sales volume when planning inventory and promotions.

4. Improve Year-End Planning

The strong November and December sales pattern suggests that the business should prepare inventory, marketing, and operational resources ahead of the year-end period.

5. Investigate Regional Differences

The significant difference between West and Central profitability suggests that regional pricing, product mix, discounting, or operational factors should be investigated.

6. Evaluate Profit Alongside Sales

Business decisions should consider:

Sales
+
Profit
+
Profit Margin
+
Discount

rather than relying on revenue alone.

Visualizations
Yearly Sales Trend

Monthly Sales Trend

Seasonal Sales Pattern

Monthly Sales Heatmap

Sales vs Profit

Category Performance

Sub-Category Profitability

Discount vs Profit

How to Run
1. Clone the Repository
git clone <YOUR_GITHUB_REPOSITORY_URL>

Navigate to the project:

cd IAIP/Task-1-Sales-Data-Analysis
2. Create a Virtual Environment
python -m venv .venv
Windows
.\.venv\Scripts\Activate.ps1
3. Install Dependencies
pip install -r requirements.txt
4. Launch Jupyter Notebook
jupyter notebook

Open:

notebooks/sales_data_analysis.ipynb

Run the notebook cells sequentially.

Notebook

The complete analysis is available in:

notebooks/sales_data_analysis.ipynb

The notebook contains the complete workflow from:

Data Loading
     ↓
Data Cleaning
     ↓
Feature Engineering
     ↓
EDA
     ↓
Trend Analysis
     ↓
Seasonality
     ↓
Product Analysis
     ↓
Regional Analysis
     ↓
Discount Analysis
     ↓
Insights
     ↓
Recommendations
Conclusion

The Sales Data Analysis project demonstrates how Python-based exploratory data analysis can be used to convert transactional retail data into actionable business insights.

The analysis identified:

Strong long-term sales growth
Significant year-end seasonality
Technology as a strong-performing category
Loss-making product sub-categories
A strong association between higher discounts and lower profitability
Significant differences in regional profitability

The project highlights the importance of evaluating sales, profit, margins, discounts, products, and regions together when making data-driven business decisions.




Internship

Organization: InternAlpha
Internship Domain: Data Analytics
Project: Task 1 — Sales Data Analysis

Author

Prasoon Pathak

Data Analytics Intern | Computer Science Engineering Student
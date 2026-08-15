# Intern Alpha — Data Analytics Internship

## IAIP Internship Project Repository

This repository contains the projects completed as part of my **Data Analytics Internship at Intern Alpha**.

The purpose of this repository is to document the practical work completed during the internship, including data analysis, visualization, machine learning, customer analysis, and business-oriented insights.

---

## Internship Overview

| Detail                | Information    |
| --------------------- | -------------- |
| **Organization**      | Intern Alpha   |
| **Internship Domain** | Data Analytics |
| **Repository**        | `IAIP`         |
| **Primary Language**  | Python         |
| **Status**            | Ongoing        |

---

# Internship Tasks

## Task 1 — Sales Data Analysis

**Status: Completed**

A comprehensive exploratory analysis of the Sample Superstore dataset.

### Objectives

* Analyze overall sales performance
* Identify yearly and monthly sales trends
* Detect seasonal patterns
* Evaluate customer segments
* Analyze categories and sub-categories
* Identify high-performing and loss-making products
* Compare regional performance
* Investigate discount and profitability patterns
* Develop data-driven business recommendations

### Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

### Key Results

The analysis identified:

* Approximately **$2.30M in total sales**
* Approximately **$286K in total profit**
* **12.47% overall profit margin**
* Approximately **51% sales growth from 2014 to 2017**
* Strong year-end sales performance, particularly in **November and December**
* **Technology** as the strongest major category by profit
* **Tables** generating more than $206K in sales while producing a loss of approximately $17.7K
* A strong association between higher discount levels and lower profitability
* Significant differences in profitability across geographic regions

### Project Files

[View Task 1](./Task-1-Sales-Data-Analysis/)

### Main Outputs

* Sales trend analysis
* Seasonal analysis
* Sales heatmap
* Category performance
* Sub-category profitability
* Discount vs profit analysis
* Business recommendations

---

# Task 2 — Customer Segmentation

**Status: Planned / In Progress**

Customer segmentation using machine learning and clustering techniques.

### Planned Objectives

* Explore customer purchasing behavior
* Prepare customer-level analytical features
* Scale numerical features
* Determine an appropriate number of clusters
* Apply K-Means clustering
* Visualize customer segments
* Profile each customer group
* Develop business and marketing recommendations

### Planned Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* K-Means Clustering
* Jupyter Notebook

### Project Files

[View Task 2](./Task-2-Customer-Segmentation/)

---

# Repository Structure

```text
IAIP/
│
├── Task-1-Sales-Data-Analysis/
│   │
│   ├── data/
│   │   └── Sample - Superstore.csv
│   │
│   ├── notebooks/
│   │   └── sales_data_analysis.ipynb
│   │
│   ├── outputs/
│   │   ├── yearly_sales_trend.png
│   │   ├── monthly_sales_trend.png
│   │   ├── seasonal_sales_pattern.png
│   │   ├── sales_heatmap.png
│   │   ├── sales_vs_profit.png
│   │   ├── category_performance.png
│   │   ├── subcategory_profitability.png
│   │   └── discount_vs_profit.png
│   │
│   ├── README.md
│   └── requirements.txt
│
├── Task-2-Customer-Segmentation/
│   │
│   ├── data/
│   ├── notebooks/
│   ├── outputs/
│   ├── README.md
│   └── requirements.txt
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Technology Stack

| Technology           | Usage                             |
| -------------------- | --------------------------------- |
| **Python**           | Core programming and analysis     |
| **Pandas**           | Data manipulation and aggregation |
| **NumPy**            | Numerical computation             |
| **Matplotlib**       | Data visualization                |
| **Seaborn**          | Statistical visualization         |
| **Scikit-learn**     | Machine learning and clustering   |
| **Jupyter Notebook** | Interactive analysis              |

---

# Analytical Workflow

The internship projects follow a structured data-analysis workflow:

```text
Data Collection
      ↓
Data Understanding
      ↓
Data Quality Assessment
      ↓
Data Cleaning
      ↓
Feature Engineering
      ↓
Exploratory Data Analysis
      ↓
Statistical / Machine Learning Analysis
      ↓
Visualization
      ↓
Insight Extraction
      ↓
Business Recommendations
```

---

# Task 1 Highlights

### Sales Performance

The Superstore analysis covers **9,994 records** across the period from **2014 to 2017**.

The dataset contained no missing values or duplicate records after the initial quality assessment.

### Sales Growth

Sales increased from approximately:

```text
2014 → $484K
2017 → $733K
```

representing approximately **51% growth** over the analysis period.

### Seasonality

The analysis showed a stronger year-end sales pattern, with **November** recording the highest average annual monthly sales and **February** the lowest.

### Profitability

The project demonstrates why revenue alone is insufficient for evaluating performance.

For example:

```text
Tables
Sales  → ~$207K
Profit → ~-$17.7K
```

while other sub-categories generated significantly stronger profit margins.

### Discount Analysis

Higher discount levels were associated with increasingly negative profitability.

The analysis showed aggregate negative profitability beginning at discount levels of approximately **30% and above**.

---

# Project Documentation

Detailed documentation for each task is available inside its respective directory.

### Task 1

[Sales Data Analysis README](./Task-1-Sales-Data-Analysis/README.md)

### Task 2

[Customer Segmentation README](./Task-2-Customer-Segmentation/README.md)

---

# Running the Projects

## Clone the Repository

```bash
git clone https://github.com/pathakpk7/IAIP.git
```

Move into the repository:

```bash
cd IAIP
```

---

## Create a Virtual Environment

```bash
python -m venv .venv
```

### Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## Install Dependencies

For the overall repository:

```bash
pip install -r requirements.txt
```

Each task also contains its own `requirements.txt` for task-specific dependencies.

---

## Launch Jupyter Notebook

```bash
jupyter notebook
```

Then open the required notebook from the corresponding task directory.

---

# Internship Progress

| Task  | Project               | Status                    |
| ----- | --------------------- | ------------------------- |
| **1** | Sales Data Analysis   | **Completed**             |
| **2** | Customer Segmentation | **In Progress / Planned** |

This table will be updated as additional internship tasks are completed.

---

# Deliverables

The internship work is being documented through:

* GitHub source code and notebooks
* Generated analytical visualizations
* Project documentation
* Demo videos
* LinkedIn project posts

The repository serves as the central record of the completed technical work.

---

# Learning Outcomes

Through these projects, the internship work focuses on developing practical skills in:

* Data cleaning
* Exploratory data analysis
* Feature engineering
* Data visualization
* Business-oriented analytical thinking
* Statistical interpretation
* Machine learning fundamentals
* Customer behavior analysis
* Communicating technical results
* Git and GitHub project management

---

# Author

## Prasoon Pathak

Computer Science Engineering Student
Data Analytics Intern at **Intern Alpha**

GitHub: [@pathakpk7](https://github.com/pathakpk7)

---

# Acknowledgement

This repository contains work completed as part of my internship at **Intern Alpha**.

The projects are intended to demonstrate practical application of data analytics and machine learning techniques to real-world-style datasets.

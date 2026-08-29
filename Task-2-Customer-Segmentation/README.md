# Customer Segmentation Using K-Means Clustering

## InternAlpha Data Analytics Internship — Task 2

This project focuses on segmenting customers based on their demographic characteristics and purchasing behavior using the **K-Means clustering algorithm**.

Customer segmentation helps businesses identify groups of customers with similar characteristics and spending patterns. These segments can be used to develop targeted marketing strategies, improve customer engagement, and support data-driven business decisions.

---

## Project Objective

The objective of this project is to apply an unsupervised machine learning technique, **K-Means Clustering**, to identify meaningful customer segments from customer demographic and purchasing data.

The analysis focuses on:

- Understanding the customer dataset
- Performing data quality checks
- Exploring customer demographics and purchasing behavior
- Selecting relevant features for clustering
- Standardizing numerical features
- Determining an appropriate number of clusters
- Applying K-Means clustering
- Profiling the resulting customer segments
- Developing actionable business recommendations

---

## Dataset

The project uses the **Mall Customer Segmentation Dataset** obtained from Kaggle.

The dataset contains **200 customer records** and the following attributes:

| Column | Description |
|---|---|
| `CustomerID` | Unique identifier for each customer |
| `Genre` | Customer gender |
| `Age` | Customer age |
| `Annual Income (k$)` | Annual income in thousands of dollars |
| `Spending Score (1-100)` | Customer spending score |

`CustomerID` is used only as an identifier and is not included in the clustering model.

`Genre` is treated as a categorical demographic attribute and is not directly used by the standard K-Means distance calculation.

The clustering model uses:

- Age
- Annual Income
- Spending Score

---

## Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Scikit-learn**
- **Jupyter Notebook**

---

## Project Workflow

The project follows the workflow below:

```text
Dataset
   ↓
Data Loading
   ↓
Data Inspection
   ↓
Data Quality Check
   ↓
Exploratory Data Analysis
   ↓
Feature Selection
   ↓
Feature Scaling
   ↓
Elbow Method
   ↓
Silhouette Score
   ↓
K-Means Clustering
   ↓
Cluster Profiling
   ↓
Business Insights
   ↓
Recommendations
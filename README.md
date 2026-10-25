# Intern Alpha — Data Analytics Internship Portfolio (IAIP)

[![GitHub Pages Live Dashboard](https://img.shields.io/badge/Live%20Dashboard-GitHub%20Pages-0e8de9?style=for-the-badge&logo=github&logoColor=white)](https://pathakpk7.github.io/IAIP/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-K--Means-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)

> **Live Interactive Web Dashboard**: Access the complete interactive dashboard comparing both tasks with live interactive charts, an interactive customer cluster classifier, and data storytelling at:  
> 👉 **[https://pathakpk7.github.io/IAIP/](https://pathakpk7.github.io/IAIP/)**

---

## 📌 Executive Summary

This repository contains the end-to-end data analytics and unsupervised machine learning projects completed during my **Data Analytics Internship at Intern Alpha**. 

Rather than confining insights to raw Jupyter Notebooks, the entire project has been elevated into an **interactive executive dashboard (`index.html`)** hosted directly on **GitHub Pages**, featuring:
* **Dual Task Navigation in Navbar**: Easily toggle between **Task 1 (Sales Diagnostic)** and **Task 2 (Customer Clustering)** with single-click tabs.
* **Pure Inline SVGs**: Clean, high-performance vector icons throughout the interface.
* **Interactive Data Visualizations**: Dynamic Chart.js visualizations with custom tooltips, zoom modals, and trendlines.
* **What-If Customer Segment Classifier**: Real-time interactive tool where users can adjust Age, Income, and Spending Score sliders to predict the customer cluster and recommended marketing action.
* **Cross-Task Strategic Synergy**: Synthesis connecting high-margin product categories with high-value customer personas.

---

## 📊 Overview of Internship Tasks

### 📈 Task 1 — Retail Sales Performance & Profitability Analysis
* **Dataset**: *Sample Superstore* (9,994 transactional records, 21 attributes, 2014–2017)
* **Key Focus**: Diagnostic sales analytics, time-series growth, regional variance, seasonality cycles, and discount profit-erosion.
* **Major Findings**:
  * **$2,297,200.86 in Gross Revenue** and **$286,397.02 in Net Profit** (12.47% margin).
  * **+51.2% Sales Growth** over 4 years with peak demand concentrated in November & December.
  * **Technology** proved to be the most lucrative category ($836K sales, $145K profit, 17.4% margin).
  * **Tables Sub-Category Anomaly**: Generated $206.9K in sales but recorded a net aggregate loss of **-$17,725**.
  * **The 30% Discount Cliff**: Aggregate transactions receiving discounts $\ge 30\%$ generated steep net losses (loss-making transactions averaged 48.09% discount).
  * **Regional Disparities**: West region achieved a **14.94% margin** vs Central region at **7.92%**.

### 👥 Task 2 — Customer Segmentation Using K-Means Clustering
* **Dataset**: *Mall Customer Segmentation Dataset* (200 customer profiles, Kaggle)
* **Key Focus**: Unsupervised machine learning, feature standardization (`StandardScaler`), cluster evaluation via **Elbow Method (WCSS)** and **Silhouette Score Analysis**, and actionable persona profiling.
* **Major Findings**:
  * Successfully validated **$K = 6$ optimal clusters** across standardized 3D feature space (Age, Annual Income, Spending Score).
  * **Cluster 3 (Champions / High Income, High Spending)**: Average age 32.7, income $86.5K, spending score 82.1. Crown-jewel demographic for luxury tech and premium lines with zero discounting needed.
  * **Cluster 2 (Untapped Wealth / High Income, Low Spending)**: 33 affluent customers with conservative spending habits (17.3 score), prime for prestige re-engagement campaigns.
  * **Cluster 4 (Young Enthusiasts / Low Income, High Spending)**: Young trend-seekers (avg age 25.3) responsive to BNPL financing, capsule drops, and flash sales.
  * **Cluster 0 & 1 (Moderate Spenders)**: Mature (49 yrs) and Young (25 yrs) stable consumers seeking consistency and digital convenience.
  * **Cluster 5 (Frugal Essentials / Low Income, Low Spending)**: Value-driven shoppers responsive to bulk discounts and clearance promotions.

---

## 🛠️ Technology Stack

| Layer | Technologies |
|---|---|
| **Data Processing & ML** | Python 3.11, Pandas, NumPy, Scikit-learn (`StandardScaler`, `KMeans`, `silhouette_score`) |
| **Statistical Plotting** | Matplotlib, Seaborn |
| **Interactive Live Dashboard** | HTML5, Tailwind CSS, Chart.js 4.4, Pure Inline SVG Icons |
| **Deployment & Hosting** | GitHub Pages (Static HTTPS, zero backend dependencies) |
| **Presentation Assets** | Microsoft PowerPoint (`.pptx`), 3D Rendered Story Assets |

---

## 📁 Repository Structure

```text
IAIP/
├── index.html                               # Live Unified Interactive Dashboard (GitHub Pages root)
├── README.md                                # Comprehensive Repository Documentation
├── requirements.txt                         # Python dependencies
├── Mini_Project_Presentation.pptx           # Executive Slide Deck
├── Cinematic_Story_3D_Morph_Presentation.pptx # Cinematic 3D Morph Presentation
│
├── Task-1-Sales-Data-Analysis/
│   ├── data/
│   │   └── Sample - Superstore.csv          # 9,994 retail transaction records
│   ├── notebooks/
│   │   └── sales_data_analysis.ipynb        # Complete exploratory data analysis
│   ├── outputs/                             # High-resolution generated charts
│   │   ├── yearly_sales_trend.png
│   │   ├── monthly_sales_trend.png
│   │   ├── seasonal_sales_pattern.png
│   │   ├── sales_heatmap.png
│   │   ├── sales_vs_profit.png
│   │   ├── category_performance.png
│   │   ├── subcategory_profitability.png
│   │   └── discount_vs_profit.png
│   └── README.md
│
├── Task-2-Customer-Segmentation/
│   ├── data/
│   │   └── Mall_Customers.csv               # 200 customer demographic & spending records
│   ├── notebooks/
│   │   └── customer_segmentation.ipynb      # K-Means clustering & validation workflow
│   ├── outputs/                             # Cluster visual outputs
│   │   ├── age_distribution.png
│   │   ├── age_vs_income.png
│   │   ├── cluster_distribution.png
│   │   ├── cluster_profile.png
│   │   ├── correlation_matrix.png
│   │   ├── customer_clusters.png
│   │   ├── elbow_method.png
│   │   ├── gender_distribution.png
│   │   ├── income_distribution.png
│   │   ├── income_vs_spending.png
│   │   ├── silhouette_score.png
│   │   └── spending_distribution.png
│   └── README.md
│
├── outputs_flowcharts/
│   ├── flowchart_pipeline.png               # End-to-end data pipeline diagram
│   └── flowchart_kmeans.png                 # K-Means mathematical clustering architecture
└── presentation_assets_3d/                  # 3D visual assets
```

---

## 🚀 How to Run Locally

### 1. View the Dashboard
Simply open `index.html` in any web browser:
```bash
# On Windows
start index.html
```

### 2. Run the Jupyter Notebooks
```bash
# Clone the repository
git clone https://github.com/pathakpk7/IAIP.git
cd IAIP

# Create virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install requirements
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

---

## 🌐 Enabling GitHub Pages (1-Minute Setup)

To activate the live URL for your own fork or this repo:
1. Go to your repository on GitHub: `https://github.com/pathakpk7/IAIP`.
2. Click **Settings** (top tab) ➔ **Pages** (left navigation bar).
3. Under **Build and deployment**:
   * **Source**: `Deploy from a branch`
   * **Branch**: Select `main` and folder `/(root)`
   * Click **Save**.
4. Your live dashboard is immediately published at:  
   👉 **`https://pathakpk7.github.io/IAIP/`**

---

## 👤 Author

**Prasoon Pathak**  
*Data Analytics Intern | InternAlpha*  
*Computer Science & Engineering Student*  
GitHub: [@pathakpk7](https://github.com/pathakpk7)

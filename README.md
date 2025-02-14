# **Superstore Sales Analysis: Data-Driven Insights & Forecasting**

## Project Overview
This project analyzes **Superstore Sales Data** to gain business insights, improve decision-making, and forecast future sales. It involves **data cleaning, database integration, visualization (Power BI), and machine learning models**.

### Key Objectives
- **Data Cleaning & Preprocessing**: Handling missing values, duplicates, and structuring data.  
- **Exploratory Data Analysis (EDA)**: Identifying sales trends, profitability, and regional performance.  
- **Machine Learning Models**:
  - **Sales Forecasting (Linear Regression)**
  - **Customer Segmentation (K-Means Clustering)**
- **Database Integration**: Storing and querying data using **MySQL**.  
- **Interactive Dashboard**: Built with **Power BI** for visualizing key business insights.
---

## Features
### Power BI Dashboard Insights
The **Power BI** dashboard provides a **Sales Overview**, including:
- **Total Sales**: $2.30M  
- **Average Profit**: $28.66  
- **Total Quantity Sold**: 38K  
- **Top-Selling Products**: Canon imageCLASS, Fellowes PB500, etc.  
- **Sales by Region**: Highest in **West (32%)** and **East (30%)**  
- **Sales by Category**: Technology ($0.84M) leads, followed by Furniture and Office Supplies.  
- **Monthly Profit Trends**: Higher in Q4, showing seasonal spikes.  

### Data Pipeline
- **superstore.py** → Prepares and cleans data before storing it in MySQL.  
- **mysql.py** → Connects to MySQL, creates a database and tables, and loads the dataset.  

---
## Technologies Used
- **Programming Language**: Python  
- **Database**: MySQL  
- **Visualization**: Power BI, Matplotlib, Seaborn  
- **Machine Learning**: Scikit-Learn  
- **Database Connection**: SQLAlchemy  

---

## Setup Guide
1. Clone the Repository
```bash
git clone <https://github.com/AlbaAdili/superstore-sales-powebi.git>
cd superstore-sales-analysis
```
2. Install Dependencies
```bash
pip install -r requirements.txt
```
3. Set Up MySQL Database
```bash
sudo systemctl start mysql  # macOS/Linux
net start mysql             # Windows
```
4. Create Database & Load Data
```bash
CREATE DATABASE superstore;
```
5. Run Analysis & Generate Insights
```bash
python superstore.py
```
##  Conclusions
- **Sales Performance**: The company generated $2.30M in total sales, with Technology leading in revenue.
- **Profitability Insights**: The West and East regions had the highest sales, but discount strategies impacted profitability.
- **Customer Segmentation**: Corporate customers contributed significantly to revenue, but consumer segment purchases dominated.
- **Seasonality Trends**: Sales peaked in Q4, indicating a holiday season sales boost.
- **Product Performance**: The Canon imageCLASS was the top-selling product.


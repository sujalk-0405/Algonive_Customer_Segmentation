# 📊 Customer Segmentation Using Python

**Algonive Data Analytics Internship – Task 1**

---

## 📌 Project Overview

Customer segmentation is the process of dividing customers into meaningful groups based on their demographic and behavioral characteristics.
In this project, **K-Means Clustering** is used to segment customers based on their **age, annual income, and spending behavior**.

This analysis helps businesses:

* Understand customer behavior
* Target marketing strategies effectively
* Improve customer engagement and retention

---

## 🎯 Objectives

* Perform data cleaning and preprocessing
* Conduct exploratory data analysis (EDA)
* Apply clustering techniques for customer segmentation
* Visualize customer segments
* Generate meaningful business insights

---

## 📂 Dataset

* **Dataset Name:** Mall Customer Segmentation Dataset
* **Source:** Kaggle
* **Description:** Contains customer demographic details and spending behavior

### Features Used

* Gender
* Age
* Annual Income (k$)
* Spending Score (1–100)

---

## 🛠️ Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook
* Streamlit (for dashboard visualization)

---

## 🔍 Project Workflow

1. Data loading and inspection
2. Data cleaning and preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature scaling using StandardScaler
5. Optimal cluster selection using Elbow Method
6. Customer segmentation using K-Means clustering
7. Visualization of customer segments
8. Interactive dashboard using Streamlit

---

## 📈 Results & Insights

* Customers were successfully segmented into **five distinct clusters**
* Each cluster represents unique spending and income behavior
* The results can be used for:

  * Personalized marketing campaigns
  * Customer profiling
  * Business decision-making

---

## 🖥️ Streamlit Dashboard

An interactive Streamlit dashboard is included to:

* Visualize customer segments dynamically
* Adjust the number of clusters using a slider
* Display cluster-wise customer summaries

### Run the dashboard

```bash
streamlit run dashboard/dashboard.py
```

---

## ▶️ How to Run the Project

1. Clone the repository

```bash
git clone https://github.com/sujalk-0405/Algonive_Customer_Segmentation.git
```

2. Navigate to the project directory

```bash
cd Algonive_Customer_Segmentation
```

3. Install required dependencies

```bash
pip install -r requirements.txt
```

4. Open the Jupyter Notebook

```bash
jupyter notebook
```

---

## 📌 Folder Structure

```
Algonive_Customer_Segmentation/
│
├── data/
│   └── Mall_Customers.csv
├── dashboard/
│   └── dashboard.py
├── customer_segmentation.ipynb
├── README.md
├── requirements.txt
└── LICENSE
```

---

## 📌 Conclusion

This project demonstrates how clustering techniques can be effectively used to analyze customer behavior and generate actionable insights. The implementation follows industry-standard practices and provides a strong foundation for real-world business applications.

---

## 👤 Author

**Name:** Sujal Kalal
**Internship:** Data Analytics Intern
**Organization:** Algonive

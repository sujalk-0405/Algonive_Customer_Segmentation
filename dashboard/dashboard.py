import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans

st.set_page_config(page_title="Customer Segmentation Dashboard", layout="centered")

st.title("📊 Customer Segmentation Dashboard")
st.markdown("Segmenting customers using K-Means clustering")

@st.cache_data
def load_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, "..", "data", "Mall_Customers.csv")

    df = pd.read_csv(DATA_PATH)
    le = LabelEncoder()
    df['Gender'] = le.fit_transform(df['Gender'])
    return df

df = load_data()

st.subheader("Dataset Preview")
st.dataframe(df.head())

features = df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]
scaler = StandardScaler()
scaled_data = scaler.fit_transform(features)

st.sidebar.header("Settings")
k = st.sidebar.slider("Select number of clusters", 2, 10, 5)

kmeans = KMeans(n_clusters=k, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_data)

st.subheader("Customer Segments Visualization")

fig, ax = plt.subplots()
sns.scatterplot(
    x=df['Annual Income (k$)'],
    y=df['Spending Score (1-100)'],
    hue=df['Cluster'],
    palette='viridis',
    ax=ax
)

plt.title("Income vs Spending Score")
st.pyplot(fig)

st.subheader("Cluster Summary")
st.dataframe(df.groupby('Cluster').mean())

st.markdown("---")
st.markdown("**Developed as part of Algonive Data Analytics Internship**")

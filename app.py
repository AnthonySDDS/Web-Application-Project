# Import required libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")  # Update with the correct file path

vehicle_data = load_data()

# App Title
st.header("Vehicle Data Visualization")

# Scatter Plot: Model Year vs Frequency
st.subheader("Scatterplot of Model Years with Frequency")

# Calculate model year counts and jitter
model_year_counts = vehicle_data['model_year'].value_counts()
unique_years = model_year_counts.index
frequencies = model_year_counts.values

jitter = np.random.uniform(-0.3, 0.3, size=len(unique_years))
unique_years_with_jitter = unique_years + jitter

scatter_data = pd.DataFrame({
    'model_year': unique_years_with_jitter,
    'frequency': frequencies
})

# Create scatter plot
fig_scatter = px.scatter(
    scatter_data,
    x='model_year',
    y='frequency',
    title='Scatterplot of Model Years with Frequency',
    labels={'model_year': 'Model Year', 'frequency': 'Frequency'},
    template='plotly',
    opacity=0.7
)

fig_scatter.update_traces(marker=dict(size=8))
fig_scatter.update_xaxes(title_text="Model Year")
fig_scatter.update_yaxes(title_text="Frequency")

# Display scatter plot
st.plotly_chart(fig_scatter)

# Bar Chart: Count of Vehicles by Cylinder Type
st.subheader("Count of Vehicles by Cylinder Type")

cylinder_counts = vehicle_data['cylinders'].value_counts().reset_index()
cylinder_counts.columns = ['Cylinders', 'Count']

# Create bar chart
fig_bar = px.bar(
    cylinder_counts,
    x='Cylinders',
    y='Count',
    title='Count of Vehicles by Cylinder Type',
    labels={'Cylinders': 'Number of Cylinders', 'Count': 'Vehicle Count'},
    template='plotly',
    text='Count'
)

fig_bar.update_traces(marker_color='orange', textposition='outside')
fig_bar.update_layout(
    xaxis_tickangle=-45,
    uniformtext_minsize=8, 
    uniformtext_mode='hide'
)

# Display bar chart
st.plotly_chart(fig_bar)

# End Header
st.header("Thank you for exploring the vehicle dataset!")

import streamlit as sl
import plotly.express as px
import pandas as pd
import altair as alt
import os

os.chdir("C:/Users/alexi/Coding Stuff/Web-Application-Project")

vehicle_data = pd.read_csv(r"C:\Users\alexi\Coding Stuff\Web-Application-Project\vehicles_us.csv")



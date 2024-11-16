import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from pinotdb import connect
import plotly.express as px
from datetime import datetime

# Connect to the Pinot database
conn = connect(host='13.214.194.35', port=8099, path='/query/sql', schema='http')
curs = conn.cursor()

def query_total_revenue_by_genre():
    curs.execute(''' 
    SELECT 
        GENRE, 
        SUM(TOTAL_PRICE) AS total_revenue 
    FROM 
        book
    GROUP BY 
        GENRE
    ORDER BY 
        total_revenue DESC;
    ''')
    tables = [row for row in curs.fetchall()]
    tables = [(genre if genre is not None else "Others", revenue) for genre, revenue in tables]
    genres = [row[0] for row in tables]
    revenues = [row[1] for row in tables]

    # Find the max revenue
    max_revenue = max(revenues)

    # Create a color list where the max value gets 'orangered' and others get 'skyblue'
    colors = ['orangered' if revenue == max_revenue else 'skyblue' for revenue in revenues]

    fig = plt.figure(figsize=(10, 6))
    plt.bar(genres, revenues, color=colors)
    plt.title('Total Revenue by Genre', fontsize=14)
    plt.xlabel('Genre', fontsize=12)
    plt.ylabel('Total Revenue (USD)', fontsize=12)
    plt.xticks(rotation=45, ha="right")
    st.pyplot(fig)

query_total_revenue_by_genre()

def query_total_quantity_by_genre():
    curs.execute(''' 
    SELECT 
        GENRE, 
        SUM(QUANTITY) AS total_quantity
    FROM 
        book
    GROUP BY 
        GENRE
    ORDER BY 
        total_quantity DESC;
    ''')
    tables = [row for row in curs.fetchall()]
    tables = [(genre if genre is not None else "Others", quantity) for genre, quantity in tables]
    genres = [row[0] for row in tables]
    quantities = [row[1] for row in tables]

    # Find the max quantity
    max_quantity = max(quantities)

    # Create a color list where the max value gets 'orangered' and others get 'skyblue'
    colors = ['orangered' if quantity == max_quantity else 'skyblue' for quantity in quantities]

    fig = plt.figure(figsize=(10, 6))
    plt.bar(genres, quantities, color=colors)
    plt.title('Total Quantity by Genre', fontsize=14)
    plt.xlabel('Genre', fontsize=12)
    plt.ylabel('Total Quantity', fontsize=12)
    plt.xticks(rotation=45, ha="right")
    st.pyplot(fig)

query_total_quantity_by_genre()
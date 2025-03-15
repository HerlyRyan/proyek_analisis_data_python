import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import date
import function

# Load dataset
data = pd.read_csv('./dashboard/main_data.csv')

# Convert date columns to datetime
date_columns = ['date']
data.sort_values(by='date', inplace=True)
data.reset_index(drop=True, inplace=True)

for col in date_columns:
    data[col] = pd.to_datetime(data[col])

# Sidebar date filter
max_date = data['date'].max().date()
min_date = data['date'].min().date()

with st.sidebar:
    start_date, end_date = st.date_input(
        label='Select Date Range',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

    if st.checkbox("Show Dataset"):
        st.subheader("Dataset")
        st.write(data)
    
    st.title('Created by:')
    st.write(
        """ 
        **Herly Riyanto Hidayat**\n
        Dicoding ID: **herlyryanth**\n
        Email: **herlynjjd@gmail.com**
        """
    )

filtered_data = data[(data['date'] >= str(start_date)) & (data['date'] <= str(end_date))]

# Call functions to create summaries
monthly_summary = function.create_month_recap(filtered_data)
season_summary = function.create_season_recap(filtered_data)
weather_summary = function.create_weather_recap(filtered_data)
workingday_hour_summary = function.create_workingday_hour_recap(filtered_data)
holiday_hour_summary = function.create_holiday_hour_recap(filtered_data)
rfm_summary = function.create_rfm_recap(filtered_data)
daily_summary = function.create_daily_recap(filtered_data)
casual_summary = function.create_casual_recap(filtered_data)
registered_summary = function.create_registered_recap(filtered_data)
temperature_summary = function.create_temp_recap(filtered_data)
humidity_summary = function.create_hum_recap(filtered_data)

# Build UI
st.header('Bike Analytics Dashboard')

# Bike Rent Summary
st.subheader('Bike Rent Summary')
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    total_users = daily_summary['total'].sum()
    st.metric('Total Users', value=total_users)

with col2:
    registered_users = registered_summary['registered'].sum()
    st.metric('Registered Users', value=registered_users)

with col3:
    casual_users = casual_summary['casual'].sum()
    st.metric('Casual Users', value=casual_users)

with col4:
    avg_temp = temperature_summary['temp'].mean()
    st.metric('Average Temperature', value=avg_temp)

with col5:
    avg_humidity = humidity_summary['hum'].mean()
    st.metric('Average Humidity', value=avg_humidity)

# Monthly Rent Recap
st.subheader('Monthly Rent Recap')
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    monthly_summary['year_month'],
    monthly_summary['total_sum'],
    marker='o', 
    linewidth=5,
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15, rotation=45)

st.pyplot(fig)

# Season and Weather Recap
st.subheader('Season and Weather Recap')

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(
        y='registered', 
        x='season',
        data=season_summary.sort_values(by='registered', ascending=False),
        color='tab:blue',
        label='Registered Users',
        ax=ax
    )
    sns.barplot(
        y='casual', 
        x='season',
        data=season_summary.sort_values(by='casual', ascending=False),
        color='tab:orange',
        label='Casual Users',
        ax=ax
    )
    ax.set_title('Number of Rents by Season', loc='center', fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    ax.legend(fontsize=20)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(
        y='total', 
        x='weather',
        data=weather_summary.sort_values(by='total', ascending=False),
        ax=ax
    )
    
    ax.set_title('Mean Rents by Weather', loc='center', fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

# Workingday and Holiday Hour Recap
st.subheader('Workingday and Holiday Hour Recap')

col1, col2 = st.columns(2)

with col1:
    max_workingday_hour = workingday_hour_summary['total'].idxmax()
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(
        y='total', 
        x='hour',
        data=workingday_hour_summary,
        color='tab:blue',
        ax=ax
    )
    plt.bar(max_workingday_hour, workingday_hour_summary.loc[max_workingday_hour, 'total'], color='tab:red', label='Peak Hour')
    ax.set_title('Workingday Rent Hour Recap', loc='center', fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    ax.legend(fontsize=20)
    st.pyplot(fig)

with col2:
    max_holiday_hour = holiday_hour_summary['total'].idxmax()
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(
        y='total', 
        x='hour',
        data=holiday_hour_summary,
        color='tab:blue',
        ax=ax
    )
    plt.bar(max_holiday_hour, holiday_hour_summary.loc[max_holiday_hour, 'total'], color='tab:red', label='Peak Hour')
    ax.set_title('Holiday Rent Hour Recap', loc='center', fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    ax.legend(fontsize=20)
    st.pyplot(fig)

# RFM Recap
st.subheader('RFM Recap')

col1, col2, col3 = st.columns(3)

with col1:
    top_recency = rfm_summary.sort_values(by='recency', ascending=True).head(7)
    fig, ax = plt.subplots(figsize=(10, 6))

    sns.barplot(
        data=top_recency, 
        x='hour', 
        y='recency',
        color='tab:blue',
        ax=ax
    )
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.set_title('Recency (days)', loc='center', fontsize=50)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

with col2:
    top_frequency = rfm_summary.sort_values(by='order_count', ascending=False).head(7)
    fig, ax = plt.subplots(figsize=(10, 6))

    sns.barplot(
        data=top_frequency,
        x='hour',
        y='order_count', 
        color='tab:blue',
        ax=ax
    )
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.set_title('Frequency', loc='center', fontsize=50)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

with col3:
    top_monetary = rfm_summary.sort_values(by='revenue', ascending=False).head(7)
    fig, ax = plt.subplots(figsize=(10, 6))

    sns.barplot(
        data=top_monetary, 
        x='hour', 
        y='revenue', 
        color='tab:blue',
        ax=ax
    )
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.set_title('Monetary', loc='center', fontsize=50)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

current_year = date.today().year
st.caption(f'Copyright (c) Herly {current_year}')
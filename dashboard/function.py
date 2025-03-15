# Menyiapkan dataframe yang diperlukan
def create_month_recap(df):
    plot_month = df['month'].astype(str)
    plot_year = df['year'].astype(str)
    df['year_month'] = plot_month + ' ' + plot_year
    df['total_sum'] = df.groupby('year_month')['total'].transform('sum')
    return df[['year_month', 'total_sum']]

def create_season_recap(df):
    season_recap = df.groupby(by='season')[['registered', 'casual']].sum().reset_index()
    return season_recap

def create_weather_recap(df):
    weather_recap = df.groupby(by='weather').agg({
    'total': 'mean'
    }).reset_index()
    return weather_recap

def create_workingday_hour_recap(df):
    filter_workingday = df[(df['workingday'] == 1)]
    workingday_hour_recap = filter_workingday.groupby(by='hour').agg({
    'total': 'sum'
    }).reset_index()
    return workingday_hour_recap

def create_holiday_hour_recap(df):
    filter_holiday = df[(df['holiday'] == 1)|(df['workingday'] == 0)]
    holiday_hour_recap = filter_holiday.groupby(by='hour').agg({
    'total': 'sum'
    }).reset_index()
    return holiday_hour_recap

def create_rfm_recap(df):
    rfm_df = df.groupby(by='hour', as_index=False).agg({
    'date': 'max',
    'instant': 'nunique',
    'total': 'sum'
    })
    rfm_df.columns = ['hour', 'last_order_date', 'order_count', 'revenue'] # mengganti nama kolom

    # perhitungan recency per hari
    rfm_df['last_order_date'] = rfm_df['last_order_date'].dt.date
    recent_date = df['date'].dt.date.max()
    rfm_df['recency'] = rfm_df['last_order_date'].apply(lambda x: (recent_date - x).days)

    rfm_df.drop('last_order_date', axis=1, inplace=True)  # Drop kolom 'last_order_date'
    return rfm_df

def create_daily_recap(df):
    daily_recap = df.groupby(by='date').agg({
        'total': 'sum'
    }).reset_index()
    return daily_recap

def create_registered_recap(df):
    registered_recap = df.groupby(by='date').agg({
        'registered': 'sum'
    }).reset_index()
    return registered_recap

def create_casual_recap(df):
    casual_recap = df.groupby(by='date').agg({
        'casual': 'sum'
    }).reset_index()
    return casual_recap

def create_temp_recap(df):
    temp_recap = df.groupby(by='date').agg({
        'temp': 'mean'
    }).reset_index()
    return temp_recap

def create_hum_recap(df):
    hum_recap = df.groupby(by='date').agg({
        'hum': 'mean'
    }).reset_index()
    return hum_recap
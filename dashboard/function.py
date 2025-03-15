# Menyiapkan dataframe yang diperlukan
def create_month_recap(df):
    plot_month = df['month'].astype(str)
    plot_year = df['year'].astype(str)
    df['year_month'] = plot_month + ' ' + plot_year
    df['total_sum'] = df.groupby('year_month')['total_rent'].transform('sum')
    return df[['year_month', 'total_sum']]

def create_season_recap(df):
    season_recap = df.groupby(by='season')[['registered', 'unregistered']].sum().reset_index()
    return season_recap

def create_weather_recap(df):
    weather_recap = df.groupby(by='weather').agg({
    'total_rent': 'mean'
    }).reset_index()
    return weather_recap

def create_workingday_hour_recap(df):
    filter_workingday = df[(df['workingday'] == 1)]
    workingday_hour_recap = filter_workingday.groupby(by='hour').agg({
    'total_rent': 'sum'
    }).reset_index()
    return workingday_hour_recap

def create_holiday_hour_recap(df):
    filter_holiday = df[(df['holiday'] == 1)|(df['workingday'] == 0)]
    holiday_hour_recap = filter_holiday.groupby(by='hour').agg({
    'total_rent': 'sum'
    }).reset_index()
    return holiday_hour_recap

def season_category(df):
    plot_season = df.groupby(by="season").agg({
    'total_rent': 'mean'
    })
    return plot_season

def weather_category(df):
    plot_weather = df.groupby(by='weather').agg({
    'total_rent': 'mean'
    }).reset_index()
    return plot_weather

def categorize_time(hour):
    if 0 <= hour < 6:
        return 'Early Morning'
    elif 7 <= hour < 12:
        return 'Morning'
    elif 13 <= hour < 18:
        return 'Afternoon'
    else:
        return 'Night'

def time_category(df):
    plot_time = df.hour.apply(categorize_time)
    return plot_time

def create_daily_recap(df):
    daily_recap = df.groupby(by='date').agg({
        'total_rent': 'sum'
    }).reset_index()
    return daily_recap

def create_registered_recap(df):
    registered_recap = df.groupby(by='date').agg({
        'registered': 'sum'
    }).reset_index()
    return registered_recap

def create_unregistered_recap(df):
    casual_recap = df.groupby(by='date').agg({
        'unregistered': 'sum'
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
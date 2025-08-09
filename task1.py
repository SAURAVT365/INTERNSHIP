"""
Task 1 - API Integration and Data Visualization
Internship: CODTECH
Author: Your Name
Date: YYYY-MM-DD

Description:
This script fetches weather forecast data from the OpenWeatherMap API
and visualizes temperature and humidity trends using Matplotlib & Seaborn.
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------- USER SETTINGS ----------------------
API_KEY = "4f70b5b0f9528de411fbc5f0b62d06a5"  # Replace with your API Key from OpenWeatherMap
CITY = "Mumbai"           # Change the city name as needed
# ------------------------------------------------------------

# API endpoint for 5-day forecast
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch data from API
print(f"Fetching weather data for {CITY}...")
response = requests.get(URL)
if response.status_code != 200:
    print("Error fetching data. Check your API key and city name.")
    exit()

data = response.json()

# Extract weather details
forecast_list = data["list"]
weather_data = []
for forecast in forecast_list:
    dt = forecast["dt_txt"]  # Date & Time
    temp = forecast["main"]["temp"]  # Temperature in °C
    humidity = forecast["main"]["humidity"]  # Humidity in %
    weather_data.append({"Date": dt, "Temperature (°C)": temp, "Humidity (%)": humidity})

# Convert to DataFrame
df = pd.DataFrame(weather_data)

# ---------------------- DATA VISUALIZATION ----------------------
sns.set_theme(style="whitegrid")

# Plot Temperature Trend
plt.figure(figsize=(12, 5))
sns.lineplot(x="Date", y="Temperature (°C)", data=df, marker="o", color="orange")
plt.xticks(rotation=45)
plt.title(f"Temperature Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()

# Plot Humidity Trend
plt.figure(figsize=(12, 5))
sns.lineplot(x="Date", y="Humidity (%)", data=df, marker="o", color="blue")
plt.xticks(rotation=45)
plt.title(f"Humidity Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Humidity (%)")
plt.tight_layout()
plt.show()

# Save Data to CSV
csv_filename = f"{CITY}_weather_forecast.csv"
df.to_csv(csv_filename, index=False)
print(f"Weather data saved to {csv_filename}")

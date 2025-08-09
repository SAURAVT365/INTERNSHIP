"""
CODTECH Internship - Task 2
Automated Report Generation
Author: Saurav Tiwari
Date: 2025-08-05

Description:
Reads weather forecast data from a CSV file,
creates visualizations, and generates a PDF report.
"""

import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
import os

# ---------------------- SETTINGS ----------------------
CSV_FILE = "Mumbai_weather_forecast.csv"  # Output from Task 1
PDF_FILE = "Weather_Report.pdf"
# ------------------------------------------------------

# ---------------------- LOAD DATA ----------------------
if not os.path.exists(CSV_FILE):
    raise FileNotFoundError(f"{CSV_FILE} not found! Please run Task 1 first.")

df = pd.read_csv(CSV_FILE)

# ---------------------- CREATE VISUALIZATIONS ----------------------
plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Temperature (°C)"], marker="o", color="orange")
plt.xticks(rotation=45, ha="right")
plt.title("Temperature Forecast")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
temp_chart = "temp_chart.png"
plt.savefig(temp_chart)
plt.close()

plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Humidity (%)"], marker="o", color="blue")
plt.xticks(rotation=45, ha="right")
plt.title("Humidity Forecast")
plt.xlabel("Date & Time")
plt.ylabel("Humidity (%)")
plt.tight_layout()
hum_chart = "hum_chart.png"
plt.savefig(hum_chart)
plt.close()

# ---------------------- CREATE PDF ----------------------
styles = getSampleStyleSheet()
doc = SimpleDocTemplate(PDF_FILE, pagesize=A4)

elements = []

# Title
elements.append(Paragraph("Weather Forecast Report", styles["Title"]))
elements.append(Spacer(1, 12))

# Summary
avg_temp = df["Temperature (°C)"].mean()
avg_hum = df["Humidity (%)"].mean()
summary_text = f"""
This report presents the 5-day weather forecast for <b>Mumbai</b>.<br/>
Average Temperature: <b>{avg_temp:.2f} °C</b><br/>
Average Humidity: <b>{avg_hum:.2f} %</b>
"""
elements.append(Paragraph(summary_text, styles["Normal"]))
elements.append(Spacer(1, 12))

# Add temperature chart
elements.append(Paragraph("Temperature Forecast", styles["Heading2"]))
elements.append(Image(temp_chart, width=400, height=200))
elements.append(Spacer(1, 12))

# Add humidity chart
elements.append(Paragraph("Humidity Forecast", styles["Heading2"]))
elements.append(Image(hum_chart, width=400, height=200))
elements.append(Spacer(1, 12))

# Save PDF
doc.build(elements)

print(f"✅ PDF report generated: {PDF_FILE}")

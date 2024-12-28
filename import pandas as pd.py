import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (replace 'accident_dataset.csv' with your file path)
df = pd.read_csv('accident_dataset.csv')

# Preview the data
print(df.head())
print(df.info())

# Handle missing values
df.dropna(inplace=True)  # Drop rows with missing values (or use fillna if needed)

# Convert time column to datetime format
df['Time'] = pd.to_datetime(df['Time'], errors='coerce')

# Extract hour from the time column for time-of-day analysis
df['Hour'] = df['Time'].dt.hour

# Normalize weather, road conditions, etc.
df['Weather'] = df['Weather'].str.lower()  # Ensure consistent case
df['Road_Condition'] = df['Road_Condition'].str.lower()

# Remove any outliers (if applicable)
# Example: Remove rows with invalid GPS coordinates
df = df[(df['Latitude'] > -90) & (df['Latitude'] < 90)]

# Group by hour and count accidents
hourly_accidents = df.groupby('Hour').size()

# Plot accidents by time of day
plt.figure(figsize=(10, 6))
hourly_accidents.plot(kind='bar', color='orange')
plt.title('Accidents by Hour of the Day')
plt.xlabel('Hour')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=0)
plt.show()

# Group by weather and count accidents
weather_accidents = df['Weather'].value_counts()

# Plot accidents by weather
plt.figure(figsize=(8, 6))
weather_accidents.plot(kind='bar', color='red')
plt.title('Accidents by Weather Condition')
plt.xlabel('Weather')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

# Group by road condition and count accidents
Road_Condition = df['Road_Condition'].value_counts()

# Plot accidents by road conditions
plt.figure(figsize=(8, 6))
Road_Condition.plot(kind='bar', color='yellow')
plt.title('Accidents by Road Condition')
plt.xlabel('Road Condition')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

# Create a scatter plot for accident locations
plt.figure(figsize=(12, 8))
plt.scatter(df['Longitude'], df['Latitude'], alpha=0.5, c='red', s=30)
plt.title('Traffic Accident Locations')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()

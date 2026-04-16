import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate date range (2 years daily data)
dates = pd.date_range(start="2020-01-01", end="2021-12-31")

# Create seasonal temperature pattern
# (sin wave to simulate seasons)
days = np.arange(len(dates))
temperature = 20 + 10 * np.sin(2 * np.pi * days / 365) + np.random.normal(0, 2, len(dates))

# Rainfall (random + seasonal spikes)
rainfall = np.random.exponential(scale=2, size=len(dates))
rainfall += 5 * np.sin(2 * np.pi * days / 365)

# Humidity (correlated with rainfall)
humidity = 50 + (rainfall * 3) + np.random.normal(0, 5, len(dates))

# Add anomalies (extreme weather events)
anomaly_indices = np.random.choice(len(dates), size=10, replace=False)
temperature[anomaly_indices] += np.random.choice([8, -8], size=10)

# Create DataFrame
df = pd.DataFrame({
    "Date": dates,
    "Temperature": temperature,
    "Rainfall": rainfall,
    "Humidity": humidity
})

# Save dataset
df.to_csv("data/climate_data.csv", index=False)

print("✅ Climate dataset generated successfully!")
print(df.head())
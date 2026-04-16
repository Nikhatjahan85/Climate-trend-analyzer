from src.data_loader import load_data
from src.preprocessing import preprocess
from src.analysis import plot_temperature, plot_rainfall
from src.anomaly import detect_anomaly, plot_anomalies
from src.forecast import forecast_temperature

# Load data
df = load_data("data/raw/climate_data.csv")

# Preprocess
df = preprocess(df)

# Plot graphs
plot_temperature(df)
plot_rainfall(df)

# Detect anomaly
df = detect_anomaly(df)
print("\nAnomaly Data:\n", df[['Date','Temperature','Anomaly']])
plot_anomalies(df)


# Forecast
predictions = forecast_temperature(df)
print("\nFuture Temperature Predictions:", predictions)
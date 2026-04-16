import matplotlib.pyplot as plt

def detect_anomaly(df):
    mean = df['Temperature'].mean()
    std = df['Temperature'].std()

    df['Anomaly'] = (df['Temperature'] > mean + 2*std) | (df['Temperature'] < mean - 2*std)

    return df


def plot_anomalies(df):
    plt.figure(figsize=(10,5))

    plt.plot(df['Date'], df['Temperature'], label='Temperature')

    # Highlight anomalies
    anomalies = df[df['Anomaly'] == True]
    plt.scatter(anomalies['Date'], anomalies['Temperature'], color='red', label='Anomaly')

    plt.title("Temperature Anomalies")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.legend()
    plt.grid()

    plt.savefig("outputs/plots/anomaly_plot.png")
    plt.show()
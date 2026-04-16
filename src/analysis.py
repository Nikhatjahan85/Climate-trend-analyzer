import matplotlib.pyplot as plt

def plot_temperature(df):
    plt.figure(figsize=(10,5))
    plt.plot(df['Date'], df['Temperature'], label='Temperature')
    plt.title("Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.legend()
    plt.grid()
    plt.savefig("outputs/plots/temperature_trend.png")
    plt.show()


def plot_rainfall(df):
    plt.figure(figsize=(10,5))
    plt.plot(df['Date'], df['Rainfall'], label='Rainfall', color='green')
    plt.title("Rainfall Trend")
    plt.xlabel("Date")
    plt.ylabel("Rainfall")
    plt.legend()
    plt.grid()
    plt.savefig("outputs/plots/rainfall_trend.png")
    plt.show()
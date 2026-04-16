from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_temperature(df):
    df['Day'] = np.arange(len(df))

    X = df[['Day']]
    y = df['Temperature']

    model = LinearRegression()
    model.fit(X, y)

    future_days = np.array([[len(df)+i] for i in range(5)])
    predictions = model.predict(future_days)

    return predictions
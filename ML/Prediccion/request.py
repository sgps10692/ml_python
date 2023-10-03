import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import explained_variance_score
from sklearn.model_selection import train_test_split

weather_data = pd.read_csv('udca.csv')

weather_data_ordered = weather_data.sort_values(by='Fecha')

# Reset index to restore its order
weather_data_ordered.reset_index(drop=True)

# %% [5] Data Analysis and Interpretation


# Compute correlations

# TO DO: Get the correlation for different combinations of variables.
#       Contrast them with the weather_correlations dataframe


# %% [6] Data Modeling and Prediction

# Get data subsets for the model
x_train, x_test, y_train, y_test = train_test_split(
    weather_data_ordered['PREACU2MIN'], weather_data_ordered['HUMSUEPROF1MTS'],
    test_size=0.25)

# Run regression
regression = linear_model.LinearRegression()
regression.fit(x_train.values.reshape(-1, 1), y_train.values.reshape(-1, 1))

# Print coefficients
print(regression.intercept_, regression.coef_)  # beta_0, beta_1


# %% [7] Predictive Model Testing and Evaluation
# Plot predicted model with test data
y_predict = regression.predict([[5]])

print('ghdcjgdhdsgh', y_predict)

# TODO: Using the model, predict the temperature for a given level of humidity

# Evaluate model numerically
explained_variance_score(y_test, y_predict)
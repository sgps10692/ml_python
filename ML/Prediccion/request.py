import requests
import json
import time
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import explained_variance_score
from sklearn.model_selection import train_test_split

# Cargar el archivo CSV con los datos
weather_data = pd.read_csv('udca.csv')

# Ordenar los datos por la columna 'Fecha'
weather_data_ordered = weather_data.sort_values(by='Fecha')

# Restablecer el índice para restaurar su orden
weather_data_ordered.reset_index(drop=True)


# Obtener los datos necesarios para el modelo
x_train, x_test, y_train, y_test = train_test_split(
    weather_data_ordered['PREACU2MIN'], weather_data_ordered['HUMSUEPROF1MTS'],
    test_size=0.25)

# Entrenar el modelo de regresión lineal
regression = linear_model.LinearRegression()
regression.fit(x_train.values.reshape(-1, 1), y_train.values.reshape(-1, 1))

# Imprimir los coeficientes del modelo
print("Intercept:", regression.intercept_)
print("Coeficiente:", regression.coef_)

# Realizar predicciones con el modelo
y_predict = regression.predict(x_test.values.reshape(-1, 1))

print('Predicciones:', y_predict)

# Evaluar el modelo
variance_score = explained_variance_score(y_test, y_predict)
print('Explained Variance Score:', variance_score)

# Datos comunes a todas las solicitudes
parameter_variable_id = 13
location_id = 1

# Cabeceras si es necesario
cabeceras = {
    'Content-Type': 'application/json',
}

# Convierte los datos comunes en una cadena JSON una vez
result_data = {
    'parameter_variable_id': parameter_variable_id,
    'location_id': location_id,
}
url = "http://127.0.0.1:8000/api/meteorological-values"

dataJson  = json.dumps(result_data)

# Realizar las solicitudes POST para cada predicción en y_predict
for prediction in y_predict:
    result_data['value'] = int(prediction[0])  # El resultado de la predicción
    
    # Realizar la solicitud POST
    response = requests.post(url, json=result_data, headers=cabeceras)

    if response.status_code == 200:
        print('Resultado guardado exitosamente.')
    else:
        print(f'Error al guardar el resultado. Código de estado: {response.status_code}')

        # Intenta acceder al contenido de la respuesta para obtener más detalles
        try:
            error_message = response.json()
            print('Detalles del error:', error_message)
        except ValueError:
            # Si la respuesta no es JSON, simplemente imprime el contenido de la respuesta
            print('')

    # Agrega un retraso de, por ejemplo, 1 segundo entre solicitudes
    time.sleep(1)
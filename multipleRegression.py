'''
We can predict the CO2 emission of a car based on the size of the engine, but with multiple regression
 we can throw in more variables, like the weight of the car, to make the prediction more accurate.

'''
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

def hacerPrediccion(df):

    X = df[['Weight', 'Volume']]
    y = df['CO2']
    
    plt.scatter(X['Weight'], y)
    plt.scatter(X['Volume'], y)
    plt.xlabel("Weight and Volume")
    plt.ylabel("CO2")
    #plt.show()
    #From the sklearn module we will use the LinearRegression() method to create a linear regression object.
    
    regr = linear_model.LinearRegression()
    
    #This object has a method called fit() that takes the independent and dependent values as parameters 
    #and fills the regression object with data that describes the relationship
    
    
    regr.fit(X, y)
    
    #predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
    predictedCO2 = regr.predict([[2300, 1300]])
    
    print(predictedCO2)
    
    #We have predicted that a car with 1.3 liter engine, and a weight of 2300 kg, 
    #will release approximately 107 grams of CO2 for every kilometer it drives.
    
    print(regr.coef_)
    
    #The coefficient is a factor that describes the relationship with an unknown variable
    
    
    #What if we increase the weight with 1000kg?
    
    predictedCO2 = regr.predict([[3300, 1300]])
    
    print(predictedCO2)
    
    #Which shows that the coefficient of 0.00755095 is correct:
    
    #107.2087328 + (1000 * 0.00755095) = 114.75968
    
    predictedCO2 = regr.predict([[1000, 790]])
    print(predictedCO2)
    
    return predictedCO2


def getPrediction(location):
    
    if location == 1:
        df = pd.read_csv("data.csv") 
        
    elif location ==2:
        df = pd.read_csv("data2.csv")
        
    result = hacerPrediccion(df)
    return result


location = int(input("ingrese una ubicacion:"))


resultadoprediccion = str(getPrediction(location))

character_to_remove = "["
result_string = resultadoprediccion.replace(character_to_remove, "")
character_to_remove = "]"
result_string = result_string.replace(character_to_remove, "")

print("resultado de la prediccion", result_string)




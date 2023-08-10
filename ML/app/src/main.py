from fastapi import FastAPI
from helada import *

 
app = FastAPI()
 
@app.get("/")
def hello(num1: int, num2: int, location: str):
    
    result = prediccion(num1, num2)

    return {
        
    }

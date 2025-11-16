from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

# CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Enum для операций
class Operation(str, Enum):
    add = "add"
    subtract = "subtract"
    multiply = "multiply"
    divide = "divide"

# Модель запроса
class CalcRequest(BaseModel):
    a: float
    b: float
    operation: Operation  # используем Enum вместо plain str

@app.post("/calculate")
def calculate(data: CalcRequest):
    if data.operation == Operation.add:
        result = data.a + data.b
    elif data.operation == Operation.subtract:
        result = data.a - data.b
    elif data.operation == Operation.multiply:
        result = data.a * data.b
    elif data.operation == Operation.divide:
        if data.b == 0:
            return {"error": "Division by zero!"}
        result = data.a / data.b
    return {"result": result}

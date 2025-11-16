from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS — разрешаем запросы с любого фронтенда
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Модель для запроса калькулятора
class CalcRequest(BaseModel):
    a: float
    b: float
    operation: str  # "add", "subtract", "multiply", "divide"

@app.post("/calculate")
def calculate(data: CalcRequest):
    if data.operation == "add":
        result = data.a + data.b
    elif data.operation == "subtract":
        result = data.a - data.b
    elif data.operation == "multiply":
        result = data.a * data.b
    elif data.operation == "divide":
        if data.b == 0:
            return {"error": "Division by zero!"}
        result = data.a / data.b
    else:
        return {"error": "Unknown operation!"}
    return {"result": result}
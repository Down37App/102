from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Разрешаем доступ с фронтенда
origins = [
    "http://localhost:5173",  # если Svelte работает локально
    "https://your-svelte-domain.com",  # если фронтенд задеплоен
    "*",  # временно разрешить все источники (только для теста)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # кто может делать запросы
    allow_credentials=True,     # разрешаем куки и авторизацию
    allow_methods=["*"],        # какие HTTP-методы разрешены
    allow_headers=["*"],        # какие заголовки разрешены
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}
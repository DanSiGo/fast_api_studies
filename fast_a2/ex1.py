from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/hello/{name}")
def hello(name: str):
    return f'Ola, {name}! Bem-vindo ao FastAPI'

uvicorn.run(app, port=8000)
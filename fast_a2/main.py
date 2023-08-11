from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def boas_vindas():
    return {"message":"Hello, world!"}

@app.get("/{name}")
def hello_name(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/items/{item_id}")
def id_product(item_id: int):
    return {"ID Item": item_id}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
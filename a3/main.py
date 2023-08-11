from fastapi import FastAPI
import uvicorn

app = FastAPI()

data = {
    1: {'name': 'Alice', 'age': 30},
    2: {'name': 'Bob', 'age': 20},
    3: {'name': 'Charlie', 'age': 10}
}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    return data[user_id]

@app.post("/users/")
def create_user(user_name: str, user_age: int):
    data[len(data) + 1] = {'name': user_name, 'age': user_age}
    return data

@app.put("/users/{user_id}")
def update_user(user_id: int, user_name: str, user_age: int):
    if user_id not in data:
        return 'User not found'
    data[user_id] = {'name': user_name, 'age': user_age}
    return data

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in data:
            return 'User not found'
    del data[user_id]
    return f'User {user_id} deleted', data



# if __name__ == "__main__":
#     uvicorn.run(app, port=8000)

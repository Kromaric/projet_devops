from fastapi import FastAPI, HTTPException
from typing import List
from app.models import Item, User
app = FastAPI()


items = []
users = []

# ---------------------
# Endpoints Items
# ---------------------


@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API Items avec FastAPI 🚀"}


@app.get("/items", response_model=List[Item])
def list_items():
    return items


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for i, existing_item in enumerate(items):
        if existing_item.id == item_id:
            items[i] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for i, item in enumerate(items):
        if item.id == item_id:
            del items[i]
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
# ---------------------
# Endpoints Users
# ---------------------


@app.get("/users", response_model=List[User])
def list_users():
    return users


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.post("/users", response_model=User)
def create_user(user: User):
    users.append(user)
    return user


@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    for i, existing_user in enumerate(users):
        if existing_user.id == user_id:
            users[i] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for i, user in enumerate(users):
        if user.id == user_id:
            del users[i]
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

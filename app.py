from fastapi import FastAPI

app = FastAPI()

wishlist = []

@app.get('/wishlist/')
def all_wishlist():
    return wishlist


@app.post('/wishlist/')
def create_wish(id:int, wish:str):
    wish = {
        "id": id,
        "wish": wish
    }
    wishlist.append(wish)
    return wishlist

@app.get('/wishlist/{id}')
def get_wish(id: int):
    for wish in wishlist:
        if wish["id"] == id:
            return wish
        else:
            return {"message": "Такого id нема!"}
        
@app.patch('/wishlist/{id}')
def update_wishlist(id:int, new_id:int, new_wish:str):
    for wish in wishlist:
        wish[id] = new_wish
    return wishlist
    

@app.delete('/wishlist/{id}')
def delete(id:int):
    wishlist.pop(id)
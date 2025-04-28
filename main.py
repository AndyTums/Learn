from fastapi import FastAPI
from typing import Annotated

app = FastAPI()


@app.get("/helpssssdasdasdsass/")
def helps():
    return {"message": "zXZXasdasdasZX"}


@app.get("/items/{items_id}/dddddd/")
def helps(items_id: Annotated[int, ...]):
    return {"message": "zXZXasdasdasZadasdsaX"}


@app.get("/items/{items_id}/")
def helps(items_id: Annotated[int, ...]):
    return {"message": "zXZXasdasdasZadasdsaX"}

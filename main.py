from typing import Optional
import io
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "add import io"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/faces_recognition/")
async def faces_recognition(image_upload: UploadFile = File(...)):
    return {"faces": "PackTest"}

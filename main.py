from typing import Optional

#from PIL import Image, ImageDraw

import io
from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "numpy 1234","pending":"123","waiting contact":"456","waiting decision":"789","close":"5"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/faces_recognition/")
async def faces_recognition(image_upload: UploadFile = File(...), text : str = None):
    return {"faces": "PackTest","text": text}

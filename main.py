from typing import Optional

#from PIL import Image, ImageDraw

import io
from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()


@app.get("/")
async def root():
    return {"lb_sum_red": "1234","lb_sum_orange":"123","lb_sum_green_light":"456","lb_sum_green_dark":"789","lb_sum_blue":"5"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/faces_recognition/")
async def faces_recognition(image_upload: UploadFile = File(...), text : str = None):
    return {"faces": "PackTest","text": text}

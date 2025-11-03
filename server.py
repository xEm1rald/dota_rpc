from fastapi import FastAPI, Request, Response
from loguru import logger


app = FastAPI()
last_data: dict = {}


@app.post("/")
async def get_info(request: Request):
    global last_data
    last_data = await request.json()
    return Response(status_code=200)


def get_data():
    return last_data
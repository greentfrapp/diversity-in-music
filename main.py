import pkg_resources
from typing import Optional, List
import types
import json

from fastapi import FastAPI, Query, Request, Response, status
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse
from pydantic import BaseModel

from gpt3 import GPT3


app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

andrew = GPT3()


@app.get("/recommend")
async def recommend(prompt: str):
    with open("assets/preset_song.txt", 'r') as file:
        template = file.read()
    with open(f"assets/preset_song.json", 'r') as file:
        config = json.load(file)
    response = andrew.query(
        template.format(prompt=prompt),
        stop=config['stop'],
        temperature=config['temperature'],
        max_tokens=config['maxTokens'],
        stream=False
    )
    print(response)
    return JSONResponse(response)


app.mount("/", StaticFiles(directory="dist", html=True), name="dist")

from fastapi import FastAPI
from router import fetch_data
from fastapi.middleware.cors import CORSMiddleware

origins=[
    'http://localhost:3000',
]

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(fetch_data.router)

     
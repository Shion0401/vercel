from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [#通信するReactのURL
    "http://localhost:3001",
    "https://dashboard.heroku.com/apps/serene-bastion-94289",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")#デフォルトのURLにGetリクエストが来たら返す内容
def Hello():
    return {"Hello":"World!"}

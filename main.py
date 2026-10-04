from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://travelbetter.co.uk",
        "https://www.travelbetter.co.uk",
        "https://tools.travelbetter.co.uk"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Hello from TravelBetter Python!"}

@app.get("/double")
def double_number(number: float):
    result = number * 2

    return {
        "number": number,
        "result": result
    }

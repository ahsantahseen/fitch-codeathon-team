
# To run use uvicorn main:app --reload
# or uvicorn main:app --reload --port 8000

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load dataset once at startup
PATH_TO_CSV = "../data/train.csv"
df = pd.read_csv(PATH_TO_CSV)

@app.get("/")
def root():
    return {"message": "FastAPI backend is running!"}

@app.get("/entity_ids")
def get_entity_ids():
    ids = df["entity_id"].tolist()
    return {"entity_ids": ids}

@app.get("/company/{entity_id}")
def get_company(entity_id: int):
    # Returns the row corresponding to the given entity_id
    row = df[df["entity_id"] == entity_id]
    if row.empty:
        return {"error": "Entity not found"}
    return row.to_dict(orient="records")[0]

@app.get("/comparisons/{entity_id}")
def get_comparisons(entity_id: int, n: int = 5):
    """
    Returns n random records from the dataset excluding the current entity_id.
    Default is 5 comparisons.
    """
    other_records = df[df["entity_id"] != entity_id]
    sample = other_records.sample(n=min(n, len(other_records)))  # handle small datasets
    return {"comparisons": sample.to_dict(orient="records")}
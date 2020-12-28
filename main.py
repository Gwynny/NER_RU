import uvicorn
from fastapi import FastAPI
from api import ner_api


app = FastAPI()
app.include_router(ner_api.ner, prefix="/api/v1/ner")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

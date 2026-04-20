from fastapi import FastAPI

app = FastAPI(title="Tuniq API")

@app.get("/")
def root():
    return {"message": "Tuniq API is running 🎵"}
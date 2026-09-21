from fastapi import FastAPI

app = FastAPI(title="Project #1")

@app.get("/")
def health_check():
    return {"status": "ok", "message": "API is running!"}

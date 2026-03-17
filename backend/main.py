from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Smart Weight API is running"}

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

@app.get("/teste")
async def root():
    return {"greeting": "teste!", "message": "teste to FastAPI!"}

from fastapi import FastAPI

app = FastAPI(title="Exemplo API FastAPI", version="1.0")

# Endpoint raiz
@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

# Endpoint de teste
@app.get("/teste")
async def teste():
    return {"greeting": "Teste!", "message": "Teste do FastAPI funcionando!"}

# Endpoint de status
@app.get("/status")
async def status():
    return {"status": "ok", "uptime": "24h"}  # exemplo de retorno

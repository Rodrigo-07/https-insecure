from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class LoginRequest(BaseModel):
    username: str
    password: str


@app.post("/login")
def login(data: LoginRequest):
    # Aqui é só um exemplo bem simples, sem banco nem nada
    if data.username == "admin" and data.password == "1234":
        return {"message": "Login efetuado com sucesso!", "token": "fake-jwt-token"}
    else:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

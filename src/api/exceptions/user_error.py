from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

def login_error_exception():
    raise HTTPException(status_code=404, detail="Email/Senha incorretos!")
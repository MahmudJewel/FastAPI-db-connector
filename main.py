from fastapi import FastAPI, Depends, Form, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy import Boolean, Column, Float, String, Integer

app = FastAPI()



@app.get('/')
async def home():
    return {"message": "Welcome to home"}


#!/usr/bin/env python3
from fastapi import APIRouter
from models.eventos import Evento
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

# GET Request
@router.get("/")
async def get_eventos():
    eventos = list_serial(collection_name.find())

    return eventos

# POST Request
@router.post("/")
async def post_evento(evento: Evento):
    collection_name.insert_one(dict(evento))

# PUT Request
@router.put("/{id}")
async def put_evento(id: str, evento: Evento):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(evento)})

# DELETE Request
@router.delete("/{id}")
async def delete_evento(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})

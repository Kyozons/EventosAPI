#!/usr/bin/env python3
from pydantic import BaseModel
from typing import Optional

class Evento(BaseModel):
    title: str
    start: str
    end: Optional[str]
    allDay: bool

#!/usr/bin/env python3
def individual_serial(evento) -> dict:
    return {
        "id": str(evento["_id"]),
        "title": evento["title"],
        "start": evento["start"],
        "end": evento["end"],
        "allDay": evento["allDay"],
    }

def list_serial(eventos) -> list:
    return [individual_serial(evento) for evento in eventos]

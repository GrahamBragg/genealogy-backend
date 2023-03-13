from typing import Union

from beanie import Document
from pydantic import BaseModel
from gedcomx.models import (
    Date,
    EventRole,
    EventType,
    PlaceReference,
    Event as GedcomEvent,
)


class Event(Document, GedcomEvent):
    class Config:
        schema_extra = {
            "example": {
                "type": "http://gedcomx.org/Birth",
                "date": {"original": "1970-01-01"},
                "place": {"original": "Canberra"},
            }
        }


class UpdateEventModel(BaseModel):
    type: Union[None, EventType]
    date: Union[None, Date]
    place: Union[None, PlaceReference]
    roles: Union[None, list[EventRole]]

    class Collection:
        name = "event"

    class Config:
        schema_extra = {
            "example": {
                "type": "http://gedcomx.org/Birth",
                "date": {"original": "1970-01-01"},
                "place": {"original": "Canberra"},
            }
        }

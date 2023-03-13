from typing import Union

from beanie import Document
from pydantic import BaseModel
from gedcomx.models import (
    Fact,
    RelationshipType,
    Relationship as GedcomRelationship,
    ResourceReference,
    GedURI,
)


class Relationship(Document, GedcomRelationship):
    class Config:
        schema_extra = {
            "example": {
                "type": "http://gedcomx.org/Couple",
                "person1": {"resource": "640a6faf0d958999563afcf8"},
                "person2": {"resource": "640a6fdb0d958999563afcf9"},
                "facts": [
                    {
                        "type": "http://gedcomx.org/Marriage",
                        "date": {"original": "1970-01-01"},
                        "place": {"original": "Canberra"},
                        "confidence": "http://gedcomx.org/High",
                        "sources": [{"description": "Marriage Certificate"}],
                    }
                ],
            }
        }


class UpdateRelationshipModel(BaseModel):
    type: Union[None, RelationshipType]
    person1: Union[ResourceReference, GedURI]
    person2: Union[ResourceReference, GedURI]
    facts: Union[None, list[Fact]]

    class Collection:
        name = "relationship"

    class Config:
        schema_extra = {
            "example": {
                "type": "http://gedcomx.org/Couple",
                "person1": {"resource": "640a6faf0d958999563afcf8"},
                "person2": {"resource": "640a6fdb0d958999563afcf9"},
                "facts": [
                    {
                        "type": "http://gedcomx.org/Marriage",
                        "date": {"original": "1970-01-01"},
                        "place": {"original": "Canberra"},
                        "confidence": "http://gedcomx.org/High",
                        "sources": [{"description": "Marriage Certificate"}],
                    }
                ],
            }
        }

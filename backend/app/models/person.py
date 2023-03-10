from typing import Union

from beanie import Document
from pydantic import BaseModel
from gedcomx.models import Fact, Gender, Name, Person as GedcomPerson


class Person(Document, GedcomPerson):
    class Config:
        schema_extra = {
            "example": {
                "names": [
                    {
                        "type": "http://gedcomx.org/BirthName",
                        "nameForms": [
                            {
                                "fullText": "John Abraham Mark Smith",
                                "parts": [
                                    {
                                        "type": "http://gedcomx.org/Given",
                                        "value": "John",
                                    },
                                    {
                                        "type": "http://gedcomx.org/Given",
                                        "value": "Abraham",
                                    },
                                    {
                                        "type": "http://gedcomx.org/Given",
                                        "value": "Mark",
                                    },
                                    {
                                        "type": "http://gedcomx.org/Surname",
                                        "value": "Smith",
                                    },
                                ],
                            }
                        ],
                        "confidence": "http://gedcomx.org/Medium",
                    }
                ],
                "facts": [
                    {
                        "type": "http://gedcomx.org/Birth",
                        "date": {"original": "1970-01-01"},
                        "place": {"original": "Canberra"},
                        "confidence": "http://gedcomx.org/High",
                        "sources": [{"description": "Birth Certificate"}],
                    }
                ],
                "gender": {"type": "http://gedcomx.org/Male"},
            }
        }


class UpdatePersonModel(BaseModel):
    private: Union[None, bool]
    gender: Union[None, Gender]
    names: Union[None, list[Name]]
    facts: Union[None, list[Fact]]

    class Collection:
        name = "person"

    class Config:
        schema_extra = {
            "example": {
                "names": [
                    {
                        "type": "http://gedcomx.org/BirthName",
                        "nameForms": [
                            {
                                "fullText": "John Abraham Mark Smith",
                                "parts": [
                                    {
                                        "type": "http://gedcomx.org/Given",
                                        "value": "John",
                                    },
                                    {
                                        "type": "http://gedcomx.org/Given",
                                        "value": "Abraham",
                                    },
                                    {
                                        "type": "http://gedcomx.org/Given",
                                        "value": "Mark",
                                    },
                                    {
                                        "type": "http://gedcomx.org/Surname",
                                        "value": "Smith",
                                    },
                                ],
                            }
                        ],
                        "confidence": "http://gedcomx.org/High",
                    }
                ],
                "facts": [
                    {
                        "type": "http://gedcomx.org/Birth",
                        "date": {"original": "1970-01-01"},
                        "place": {"original": "Canberra"},
                        "confidence": "http://gedcomx.org/High",
                        "sources": [{"description": "Birth Certificate"}],
                    }
                ],
                "gender": {"type": "http://gedcomx.org/Male"},
            }
        }

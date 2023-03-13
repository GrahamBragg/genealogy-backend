from datetime import datetime
from typing import Union
from beanie import Document
from pydantic import BaseModel
from gedcomx.models import (
    Attribution,
    Identifier,
    Note,
    SourceDescription as GedcomSourceDescription,
    SourceCitation,
    SourceReference,
    TextValue,
)


class SourceDescription(Document, GedcomSourceDescription):
    class Config:
        schema_extra = {
            "example": {
                "citations": {"lang": "en-AU", "value": "A sample citation."},
                "about": "https://www.wikipedia.org/",
                "notes": [
                    {
                        "lang": "en-AU",
                        "subject": "A sample note!",
                        "text": "Simple example note",
                    }
                ],
            }
        }


class UpdateSourceDescriptionModel(BaseModel):
    resourceType: Union[None, str]
    citations: Union[None, list[SourceCitation]]
    mediaType: Union[None, str]
    about: Union[None, str]
    mediator: Union[None, str]
    publisher: Union[None, str]
    authors: Union[None, list[str]]
    sources: Union[None, list[str]]
    analysis: Union[None, str]
    componentOf: Union[None, SourceReference]
    titles: Union[None, list[TextValue]]
    notes: Union[None, list[Note]]
    attribution: Union[None, Attribution]
    identifiers: Union[None, list[Identifier]]
    created: Union[None, datetime]
    modified: Union[None, datetime]
    published: Union[None, datetime]
    repository: Union[None, str]

    class Collection:
        name = "source_description"

    class Config:
        schema_extra = {
            "example": {
                "citations": {"lang": "en-AU", "value": "A sample citation."},
                "about": "https://www.wikipedia.org/",
                "notes": [
                    {
                        "lang": "en-AU",
                        "subject": "A sample note!",
                        "text": "Simple example note",
                    }
                ],
            }
        }

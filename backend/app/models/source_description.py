from datetime import datetime
from typing import Union
from beanie import Document
from pydantic import BaseModel
from gedcomx.models import (
    Attribution,
    Coverage,
    GedURI,
    Identifier,
    Note,
    ResourceReference,
    ResourceType,
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
    resourceType: Union[None, ResourceType]
    citations: Union[None, SourceCitation, list[SourceCitation]]
    mediaType: Union[None, str]
    about: Union[ResourceReference, GedURI, None]
    mediator: Union[ResourceReference, GedURI, None]
    publisher: Union[ResourceReference, GedURI, None]
    authors: Union[None, list[Union[ResourceReference, GedURI]]]
    sources: Union[None, list[SourceReference]]
    analysis: Union[ResourceReference, GedURI, None]
    componentOf: Union[None, SourceReference]
    titles: Union[None, list[TextValue]]
    notes: Union[None, list[Note]]
    attribution: Union[None, Attribution]
    rights: Union[None, list[GedURI]]
    coverage: Union[None, list[Coverage]]
    descriptions: Union[None, list[TextValue]]
    identifiers: Union[None, list[Identifier]]
    created: Union[None, datetime]
    modified: Union[None, datetime]
    published: Union[None, datetime]
    repository: Union[ResourceReference, GedURI, None]

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

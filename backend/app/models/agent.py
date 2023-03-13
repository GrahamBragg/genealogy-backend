from typing import Union

from beanie import Document
from pydantic import BaseModel
from gedcomx.models import (
    Address,
    Agent as GedcomAgent,
    Email,
    GedURI,
    HttpUrl,
    Identifier,
    OnlineAccount,
    ResourceReference,
    TextValue
)


class Agent(Document, GedcomAgent):
    class Config:
        schema_extra = {
            "example": {
                "identifiers": [
                    {
                        "value": "URI",
                        "type": "http://gedcomx.org/Primary"
                    }
                ],
                "names": [
                    {
                        "lang": "en-AU",
                        "value": "The person"
                    }
                ],
                "person": "OPTIONAL. MUST resolve to an instance of http://gedcomx.org/v1/Person.",
            }
        }


class UpdateAgentModel(BaseModel):
    identifiers: Union[None, list[Identifier]]
    names: Union[None, list[TextValue]]
    homepage: Union[ResourceReference, HttpUrl, None]
    openid: Union[ResourceReference, HttpUrl, None]
    accounts: Union[None, OnlineAccount]
    emails: Union[None, list[Union[ResourceReference, Email]]]
    phones: Union[None, list[Union[ResourceReference, str]]]
    addresses: Union[None, list[Address]]
    person: Union[ResourceReference, GedURI, None]

    class Collection:
        name = "agent"

    class Config:
        schema_extra = {
            "example": {
                "identifiers": [
                    {
                        "value": "URI",
                        "type": "http://gedcomx.org/Primary"
                    }
                ],
                "names": [
                    {
                        "lang": "en-AU",
                        "value": "The person"
                    }
                ],
                "person": "OPTIONAL. MUST resolve to an instance of http://gedcomx.org/v1/Person.",
            }
        }

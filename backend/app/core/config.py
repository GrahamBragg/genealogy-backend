import secrets
from typing import List, Optional, Union
from app.models.agent import Agent
from app.models.event import Event
from app.models.person import Person
from app.models.relationship import Relationship
from app.models.source_description import SourceDescription

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str

    DATABASE_URL: Optional[str] = None

    class Config:
        env_file = ".env"
        case_sensitive = True
        orm_mode = True


async def initiate_database():
    client = AsyncIOMotorClient(Settings().DATABASE_URL)
    await init_beanie(
        database=client.get_default_database(),
        document_models=[Agent, Event, Person,
                         Relationship, SourceDescription],
    )


settings = Settings()

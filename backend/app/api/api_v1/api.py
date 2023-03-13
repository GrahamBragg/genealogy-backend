from fastapi import APIRouter

from app.api.api_v1.endpoints import root, event, person, relationship, source_description

api_router = APIRouter()
api_router.include_router(root.router, tags=["root"])
api_router.include_router(event.router, prefix="/events", tags=["events"])
api_router.include_router(person.router, prefix="/persons", tags=["persons"])
api_router.include_router(
    relationship.router, prefix="/relationships", tags=["relationships"]
)
api_router.include_router(
    source_description.router, prefix="/sourcedescriptions", tags=["source_descriptions"]
)


@api_router.get("/")
async def root():
    return {"message": "Hello World"}

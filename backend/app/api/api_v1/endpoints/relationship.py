from http.client import HTTPException
from fastapi import APIRouter, Body

from app.data.relationship import *
from app.models.relationship import *

router = APIRouter()


@router.get("/check")
async def check():
    return {"message": "Relationship Router Here!"}


@router.get(
    "/",
    response_description="Relationships retrieved",
    response_model=List[Relationship],
)
async def get_relationships():
    relationships = await retrieve_relationships()
    return relationships


@router.get(
    "/{id}",
    response_description="Relationship data retrieved",
    response_model=Relationship,
)
async def get_relationship_data(id: PydanticObjectId):
    relationship = await retrieve_relationship(id)
    if relationship:
        return relationship
    raise HTTPException(
        status_code=404, detail="Relationship with id {0} not found".format(id)
    )


@router.post(
    "/",
    response_description="Relationship data added into the database",
    response_model=Relationship,
)
async def add_relationship_data(Relationship: Relationship = Body(...)):
    new_relationship = await add_relationship(Relationship)
    return new_relationship


@router.delete(
    "/{id}", response_description="Relationship data deleted from the database"
)
async def delete_relationship_data(id: PydanticObjectId):
    deleted_relationship = await delete_relationship(id)
    if deleted_relationship:
        return deleted_relationship
    raise HTTPException(
        status_code=404, detail="Relationship with id {0} not found".format(id)
    )


@router.put("/{id}", response_model=Relationship)
async def update_relationship(
    id: PydanticObjectId, req: UpdateRelationshipModel = Body(...)
):
    updated_relationship = await update_relationship_data(id, req.dict())
    if updated_relationship:
        return updated_relationship
    raise HTTPException(
        status_code=404, detail="Relationship with id {0} not found".format(id)
    )

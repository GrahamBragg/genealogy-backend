from http.client import HTTPException
from fastapi import APIRouter, Body

from app.data.source_description import *
from app.models.source_description import *

router = APIRouter()


@router.get("/check")
async def check():
    return {"message": "Source Description Router Here!"}


@router.get(
    "/",
    response_description="Source Descriptions retrieved",
    response_model=List[SourceDescription],
)
async def get_source_descriptions():
    source_descriptions = await retrieve_source_descriptions()
    return source_descriptions


@router.get(
    "/{id}",
    response_description="Source Description data retrieved",
    response_model=SourceDescription,
)
async def get_source_description_data(id: PydanticObjectId):
    source_description = await retrieve_source_description(id)
    if source_description:
        return source_description
    raise HTTPException(
        status_code=404, detail="Source Description with id {0} not found".format(id)
    )


@router.post(
    "/",
    response_description="Source Description data added into the database",
    response_model=SourceDescription,
)
async def add_source_description_data(SourceDescription: SourceDescription = Body(...)):
    new_source_description = await add_source_description(SourceDescription)
    return new_source_description


@router.delete(
    "/{id}", response_description="Source Description data deleted from the database"
)
async def delete_source_description_data(id: PydanticObjectId):
    deleted_source_description = await delete_source_description(id)
    if deleted_source_description:
        return deleted_source_description
    raise HTTPException(
        status_code=404, detail="Source Description with id {0} not found".format(id)
    )


@router.put("/{id}", response_model=SourceDescription)
async def update_source_description(
    id: PydanticObjectId, req: UpdateSourceDescriptionModel = Body(...)
):
    updated_source_description = await update_source_description_data(id, req.dict())
    if updated_source_description:
        return updated_source_description
    raise HTTPException(
        status_code=404, detail="Source Description with id {0} not found".format(id)
    )

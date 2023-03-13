from http.client import HTTPException
from fastapi import APIRouter, Body

from app.data.event import *
from app.models.event import *

router = APIRouter()


@router.get("/check")
async def check():
    return {"message": "Event Router Here!"}


@router.get("/", response_description="Events retrieved", response_model=List[Event])
async def get_events():
    events = await retrieve_events()
    return events


@router.get("/{id}", response_description="Event data retrieved", response_model=Event)
async def get_event_data(id: PydanticObjectId):
    event = await retrieve_event(id)
    if event:
        return event
    raise HTTPException(
        status_code=404, detail="Event with id {0} not found".format(id)
    )


@router.post(
    "/", response_description="Event data added into the database", response_model=Event
)
async def add_event_data(event: Event = Body(...)):
    new_event = await add_event(event)
    return new_event


@router.delete("/{id}", response_description="Event data deleted from the database")
async def delete_event_data(id: PydanticObjectId):
    deleted_event = await delete_event(id)
    if deleted_event:
        return deleted_event
    raise HTTPException(
        status_code=404, detail="Event with id {0} not found".format(id)
    )


@router.put("/{id}", response_model=Event)
async def update_event(id: PydanticObjectId, req: UpdateEventModel = Body(...)):
    updated_event = await update_event_data(id, req.dict())
    if updated_event:
        return updated_event
    raise HTTPException(
        status_code=404, detail="Event with id {0} not found".format(id)
    )

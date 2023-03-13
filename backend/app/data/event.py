from typing import List, Union

from beanie import PydanticObjectId

from app.models.event import Event

event_collection = Event


async def retrieve_events() -> List[Event]:
    events = await event_collection.all().to_list()
    return events


async def add_event(new_event: Event) -> Event:
    event = await new_event.create()
    return event


async def retrieve_event(id: PydanticObjectId) -> Event:
    event = await event_collection.get(id)
    if event:
        return event


async def delete_event(id: PydanticObjectId) -> bool:
    event = await event_collection.get(id)
    if event:
        await event.delete()
        return True


async def update_event_data(id: PydanticObjectId, data: dict) -> Union[bool, Event]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    event = await event_collection.get(id)
    if event:
        await event.update(update_query)
        return event
    return False

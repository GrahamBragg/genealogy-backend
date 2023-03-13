from typing import List, Union

from beanie import PydanticObjectId

from app.models.source_description import SourceDescription

source_description_collection = SourceDescription


async def retrieve_source_descriptions() -> List[SourceDescription]:
    source_descriptions = await source_description_collection.all().to_list()
    return source_descriptions


async def add_source_description(
    new_source_description: SourceDescription,
) -> SourceDescription:
    source_description = await new_source_description.create()
    return source_description


async def retrieve_source_description(id: PydanticObjectId) -> SourceDescription:
    source_description = await source_description_collection.get(id)
    if source_description:
        return source_description


async def delete_source_description(id: PydanticObjectId) -> bool:
    source_description = await source_description_collection.get(id)
    if source_description:
        await source_description.delete()
        return True


async def update_source_description_data(
    id: PydanticObjectId, data: dict
) -> Union[bool, SourceDescription]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    source_description = await source_description_collection.get(id)
    if source_description:
        await source_description.update(update_query)
        return source_description
    return False

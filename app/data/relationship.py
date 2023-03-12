from typing import List, Union

from beanie import PydanticObjectId

from app.models.relationship import Relationship

relationship_collection = Relationship


async def retrieve_relationships() -> List[Relationship]:
    Relationships = await relationship_collection.all().to_list()
    return Relationships


async def add_relationship(new_relationship: Relationship) -> Relationship:
    Relationship = await new_relationship.create()
    return Relationship


async def retrieve_relationship(id: PydanticObjectId) -> Relationship:
    Relationship = await relationship_collection.get(id)
    if Relationship:
        return Relationship


async def delete_relationship(id: PydanticObjectId) -> bool:
    Relationship = await relationship_collection.get(id)
    if Relationship:
        await Relationship.delete()
        return True


async def update_relationship_data(
    id: PydanticObjectId, data: dict
) -> Union[bool, Relationship]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    Relationship = await relationship_collection.get(id)
    if Relationship:
        await Relationship.update(update_query)
        return Relationship
    return False

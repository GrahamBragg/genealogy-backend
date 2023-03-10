from typing import List, Union

from beanie import PydanticObjectId

from app.models.person import Person

person_collection = Person


async def retrieve_persons() -> List[Person]:
    persons = await person_collection.all().to_list()
    return persons


async def add_person(new_person: Person) -> Person:
    person = await new_person.create()
    return person


async def retrieve_person(id: PydanticObjectId) -> Person:
    person = await person_collection.get(id)
    if person:
        return person


async def delete_person(id: PydanticObjectId) -> bool:
    person = await person_collection.get(id)
    if person:
        await person.delete()
        return True


async def update_person_data(id: PydanticObjectId, data: dict) -> Union[bool, Person]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    person = await person_collection.get(id)
    if person:
        await person.update(update_query)
        return person
    return False

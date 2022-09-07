from fastapi import APIRouter, Body

from ..database.database import *
from ..models.person import *

router = APIRouter()

@router.get("/", response_description="Persons retrieved", response_model=List[Person])
async def get_persons():
    persons = await retrieve_persons()
    return persons


@router.get("/{id}", response_description="Person data retrieved", response_model=Person)
async def get_person_data(id: PydanticObjectId):
    person = await retrieve_person(id)
    if person:
        return person
    raise HTTPException(status_code=404, detail="Person with id {0} not found".format(id))


@router.post("/", response_description="Person data added into the database", response_model=Person)
async def add_person_data(person: Person = Body(...)):
    new_person = await add_person(person)
    return new_person


@router.delete("/{id}", response_description="Person data deleted from the database")
async def delete_person_data(id: PydanticObjectId):
    deleted_person = await delete_person(id)
    if deleted_person:
        return deleted_person
    raise HTTPException(status_code=404, detail="Person with id {0} not found".format(id))


@router.put("{id}", response_model=Person)
async def update_person(id: PydanticObjectId, req: UpdatePersonModel = Body(...)):
    updated_person = await update_person_data(id, req.dict())
    if updated_person:
        return updated_person
    raise HTTPException(status_code=404, detail="Person with id {0} not found".format(id))

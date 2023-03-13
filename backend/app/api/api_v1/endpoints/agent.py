from http.client import HTTPException
from fastapi import APIRouter, Body

from app.data.agent import *
from app.models.agent import *

router = APIRouter()


@router.get("/check")
async def check():
    return {"message": "Agent Router Here!"}


@router.get("/", response_description="Agents retrieved", response_model=List[Agent])
async def get_agents():
    agents = await retrieve_agents()
    return agents


@router.get("/{id}", response_description="Agent data retrieved", response_model=Agent)
async def get_agent_data(id: PydanticObjectId):
    agent = await retrieve_agent(id)
    if agent:
        return agent
    raise HTTPException(
        status_code=404, detail="Agent with id {0} not found".format(id)
    )


@router.post(
    "/", response_description="Agent data added into the database", response_model=Agent
)
async def add_agent_data(agent: Agent = Body(...)):
    new_agent = await add_agent(agent)
    return new_agent


@router.delete("/{id}", response_description="Agent data deleted from the database")
async def delete_agent_data(id: PydanticObjectId):
    deleted_agent = await delete_agent(id)
    if deleted_agent:
        return deleted_agent
    raise HTTPException(
        status_code=404, detail="Agent with id {0} not found".format(id)
    )


@router.put("/{id}", response_model=Agent)
async def update_agent(id: PydanticObjectId, req: UpdateAgentModel = Body(...)):
    updated_agent = await update_agent_data(id, req.dict())
    if updated_agent:
        return updated_agent
    raise HTTPException(
        status_code=404, detail="Agent with id {0} not found".format(id)
    )

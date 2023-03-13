from typing import List, Union

from beanie import PydanticObjectId

from app.models.agent import Agent

agent_collection = Agent


async def retrieve_agents() -> List[Agent]:
    agents = await agent_collection.all().to_list()
    return agents


async def add_agent(new_agent: Agent) -> Agent:
    agent = await new_agent.create()
    return agent


async def retrieve_agent(id: PydanticObjectId) -> Agent:
    agent = await agent_collection.get(id)
    if agent:
        return agent


async def delete_agent(id: PydanticObjectId) -> bool:
    agent = await agent_collection.get(id)
    if agent:
        await agent.delete()
        return True


async def update_agent_data(id: PydanticObjectId, data: dict) -> Union[bool, Agent]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {
        "$set": {field: value for field, value in des_body.items()}}
    agent = await agent_collection.get(id)
    if agent:
        await agent.update(update_query)
        return agent
    return False

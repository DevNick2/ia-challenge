from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import dotenv_values
import os

from agents.image_generator import ImageGeneratorAgent

from agno.os import AgentOS

environment = os.environ.get('PYTHON_ENV')

env = dotenv_values(f'.env.{environment}')

app: FastAPI =FastAPI(title="Templo IA Challenge", description="Desafio técnico Templo.")

class Body(BaseModel):
    message: str

agent_os = AgentOS(
    os_id="templo_challenge_os",
    description="Templo challenge OS",
    agents=[ImageGeneratorAgent],
    fastapi_app=app,
    replace_routes=False
)

app = agent_os.get_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=False, access_log=True, log_level='debug')
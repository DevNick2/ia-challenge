from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import dotenv_values
import os

from textwrap import dedent

from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.models.openai import OpenAIChat
from agno.os import AgentOS
from agno.tools.dalle import DalleTools

environment = os.environ.get('PYTHON_ENV')

env = dotenv_values(f'.env.{environment}')

app: FastAPI =FastAPI(title="IA Challenge", description="Desafio técnico Templo.")

assistant = Agent(
    name="Assistente",
    model=OpenAIChat(id="gpt-5-mini"),
    tools=[DalleTools()],
    description="You are an AI agent that can create images using DALL-E.",
    instructions=[
        "When the user asks you to create an image, use the DALL-E tool to create an image.",
        "The DALL-E tool will return an image URL.",
        "Return the image URL in your response in the following format: `![image description](image URL)`",
    ],
    markdown=True,
)


class Body(BaseModel):
    message: str

agent_os = AgentOS(
    os_id="first-os",
    description="First OS",
    agents=[assistant],
    fastapi_app=app,
    replace_routes=False
)

app = agent_os.get_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=False, access_log=True, log_level='debug')
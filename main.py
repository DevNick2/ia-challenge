from contextlib import asynccontextmanager

from fastapi import FastAPI
from agno.os import AgentOS

from agents.image_generator import ImageGeneratorAgent
from agents.hook import HookAgent

from utils.environment import env

@asynccontextmanager
async def lifespan(app: FastAPI):
    hookAgent, AgentShutdown = await HookAgent()

    agent_os = AgentOS(
        os_id="templo_challenge_os",
        description="Templo challenge OS",
        agents=[ImageGeneratorAgent, hookAgent],
        fastapi_app=app,
        replace_routes=False,
    )

    app = agent_os.get_app()
    yield

app: FastAPI = FastAPI(
    title="Templo IA Challenge",
    description="Desafio técnico Templo.",
    lifespan=lifespan
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=3000,
        reload=(env == "development"),
        access_log=True,
        log_level='debug',
        reload_delay=0.5,
        reload_excludes=[".gitignore", ".python-version", "*.md", ".dockerignore"]
    )
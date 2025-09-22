from contextlib import asynccontextmanager

from fastapi import FastAPI
from agno.os import AgentOS
from agno.os.interfaces.agui import AGUI

from agents.image_generator import ImageGeneratorAgent
from agents.hook import HookAgent

from utils.environment import env

@asynccontextmanager
async def lifespan(app: FastAPI):
    hookAgent, AgentShutdown = await HookAgent()
    imageGeneratorAgent = await ImageGeneratorAgent()

    agent_os = AgentOS(
        os_id="templo_challenge_os",
        description="Templo challenge OS",
        agents=[imageGeneratorAgent, hookAgent],
        interfaces=[AGUI(agent=hookAgent)],
        fastapi_app=app,
        replace_routes=False,
    )

    new_app = agent_os.get_app()
    app.router.routes.extend(new_app.router.routes)

    try:
        yield
    finally:
        if AgentShutdown is not None:
            await AgentShutdown()

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
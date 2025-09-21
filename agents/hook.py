from agno.agent import Agent
from agno.tools.mcp import MCPTools
from agno.models.anthropic import Claude

from textwrap import dedent
from db.connection import connection

async def HookAgent():
  mcp_tools = MCPTools(transport="streamable-http", url="https://mcp.composio.dev/partner/composio/trello/mcp?customerId=bf85d93a-8e03-4821-9dc9-8ec53b1173fe") 
  await mcp_tools.connect()

  hookAgent = Agent(
    name="Agente de Hook",
    model=Claude(id="claude-opus-4-1-20250805"),
    db=connection,
    enable_user_memories=True,
    enable_session_summaries=True,
    add_history_to_context=True,
    description=dedent("""\
      Você é um assistente de IA útil e amigável com execelente memória.
        - Lembre-se de detalhes importantes sobre os usuários e referencie-os naturalmente
        - Mantenha um tom caloroso e positivo enquanto é preciso e útil
        - Quando apropriado, refira-se a conversas e memórias anteriores
        - Sempre seja honesto sobre o que você lembra ou não lembra
      Seu objetivo é apoiar o usuário na utilização do Trello, criar, gerenciar, editar e listar cards, quadros e detalhes faz parte de suas ações.
    """),
    markdown=True,
    tools=[mcp_tools]
  )

  async def AgentShutdown(): 
    await mcp_tools.close()

  return hookAgent, AgentShutdown
  
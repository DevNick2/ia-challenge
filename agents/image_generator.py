from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.dalle import DalleTools

ImageGeneratorAgent = Agent(
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

from dotenv import load_dotenv
load_dotenv()

import asyncio
import os
from ddgs import DDGS
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

# Set up the OpenAI model client
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini") 

def search_weather_news(city: str) -> str:
    """
    Searches the web for today's weather news for a given city.
    Use this tool exclusively to find current weather conditions and forecasts, 
    not for general trivia or history about the city.
    """
    return str(DDGS().news(query=f"{city} weather today", max_results=5))

city = input("Which city? ")

agent = AssistantAgent(
    name="weather_news",
    model_client=model_client,
    tools=[search_weather_news],
    system_message="You are a weather news assistant. Use the provided tool to fetch weather news for the requested city. You must reply with exactly 3 short lines summarizing the weather news.",
    reflect_on_tool_use=True
)

async def main():
    await Console(agent.run_stream(task=f"Find today's weather news for {city}."))
    await model_client.close()

if __name__ == "__main__":
    asyncio.run(main())
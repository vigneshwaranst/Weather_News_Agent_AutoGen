"# Weather_News_Agent_AutoGen" 
# AutoGen Weather News Agent

This repository contains an AutoGen-powered AI agent designed to fetch and summarize today's weather news for any given city. The agent utilizes a custom tool to search the web using the keyless DuckDuckGo search package (`ddgs`) and processes the results through an OpenAI language model (`gpt-4o-mini`) to deliver a concise summary in exactly three short lines.

## Features

* **Custom Python Tools:** Demonstrates how an AutoGen agent reads a Python function's name, type hints, and docstring to decide when to call it as a tool.
* **Keyless Web Search:** Integrates the `ddgs` package to perform live web searches without requiring a dedicated search API key.
* **Intelligent Reflection:** Uses `reflect_on_tool_use=True` so the agent synthesizes a natural language answer from the search results instead of dumping raw search output.
* **Constrained Formatting:** Employs a system message to enforce a strict output requirement, ensuring the final reply is exactly 3 short lines.

## Prerequisites

* Python installed on your system.
* An active OpenAI API key.
* A virtual environment configured with the required AutoGen packages from Day 1.

## Setup and Installation

1. Clone this repository and navigate to the project directory.
2. Activate your virtual environment.
3. Install the required DuckDuckGo search package:
   `pip install -U ddgs`
4. Export your OpenAI API key as an environment variable. 
   * *Linux/macOS:* `export OPENAI_API_KEY="your-api-key-here"`
   * *Windows (Command Prompt):* `set OPENAI_API_KEY="your-api-key-here"`

## Usage

Run the single project file `weather_news.py`:

`python weather_news.py`

The script will ask you for a city with an input prompt. Enter your desired location and press Enter.

## Example Output

> Which city? Chennai
> -- ToolCallRequestEvent (weather_news)
> search_weather_news(city='Chennai')
> -- TextMessage (weather_news)
> Heavy showers across Chennai today, with more expected by evening.
> <second line>
> <third line>

## Core Technologies

* **Python:** The programming language used to build the agent and tool.
* **AutoGen:** The framework used to orchestrate the AI agent (`AssistantAgent`) and handle tool calling.
* **DDGS:** The free, keyless package used to query DuckDuckGo news.
* **OpenAI API:** Powers the `gpt-4o-mini` model used by the agent to interpret instructions and format the final response.
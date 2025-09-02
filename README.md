# AI Research Agent

A simple AI-powered research assistant built with LangChain and OpenAI's GPT-4o model. This agent helps you research topics by searching the web, querying Wikipedia, and organizing findings into structured research papers.

## Features

- **Web Search**: Uses DuckDuckGo to search the internet for current information
- **Wikipedia Integration**: Queries Wikipedia for detailed information on topics
- **Structured Output**: Generates research papers with title, summary, sources, and tools used
- **File Saving**: Saves research output to text files for future reference

## Prerequisites

- Python 3.8 or higher
- OpenAI API key

## Installation

1. Clone this repository:
```bash
git clone https://github.com/bijayabc/research-ai-agent
cd AI-Agent
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your OpenAI API key:
   - Create a `.env` file in the project root
   - Add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the research agent:
```bash
python main.py
```

When prompted, enter your research query. The agent will:
1. Search the web and Wikipedia for relevant information
2. Process and synthesize the findings
3. Generate a structured research paper with:
   - Title
   - Summary
   - Sources
   - Tools used

The research output will be displayed in the terminal and can be saved to a file.

## Project Structure

- `main.py` - Main application file with the research agent
- `tools.py` - Custom tools for web search, Wikipedia, and file saving
- `requirements.txt` - Python dependencies
- `venv/` - Virtual environment directory

## Dependencies

- `langchain` - Framework for building LLM applications
- `langchain-openai` - OpenAI integration for LangChain
- `langchain-community` - Community tools and utilities
- `python-dotenv` - Environment variable management
- `pydantic` - Data validation and parsing
- `wikipedia` - Wikipedia API wrapper
- `ddgs` - DuckDuckGo search

## Example

```
What can I help you research today? 
----> artificial intelligence in healthcare and save the information to a file

[Agent processes the query using web search and Wikipedia]
[Generates structured research paper with findings, saves information to a file]
```

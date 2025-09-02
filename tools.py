from langchain_community.tools import DuckDuckGoSearchRun, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool

ddg_search = DuckDuckGoSearchRun()
ddg_tool = Tool(
    name='search',
    func= ddg_search.run,
    description="Tool to search the web"
)

def save_to_txt(data, filename: str = 'Research Output.txt'):
    with open(filename, 'a') as f:
        f.write(data + "\n\n")

    return f'Data saved successfully to {filename}'

save_tool = Tool(
    name='save',
    func=save_to_txt,
    description='Function to save text to a file'
)

wiki_api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)
wiki_tool = WikipediaQueryRun(api_wrapper=wiki_api_wrapper)
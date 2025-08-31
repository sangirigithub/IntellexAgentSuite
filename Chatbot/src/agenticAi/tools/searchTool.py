from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    '''
    Return list of all the Tools used with the Chatbot Application
    '''
    app_tools = [TavilySearchResults(max_results=2)]

    return app_tools

def create_tools_node(app_tools):
    '''
    Create and return Tool Node for the Graph
    '''
    return ToolNode(app_tools)



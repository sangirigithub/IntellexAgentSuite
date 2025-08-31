from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition, ToolNode

from src.agenticAi.state.agentState import State
from src.agenticAi.nodes.chatbotLiteNode import ChatbotLiteNode
from src.agenticAi.tools.search_tool import get_tools, create_tools_node
from src.agenticAi.nodes.chatbotWithToolsNode import ChatbotWithToolsNode

class GraphBuilder:
    ## When GraphBuilder gets initialized, LLM Model should get loaded and entire StateGraph should also get loaded
    ## i.e. llm/model + graph_builder/State

    def __init__(self, llm):
        self.llm = llm
        self.graph_builder = StateGraph(State)

    def chatbot_lite_build_graph(self):
        '''
        Builds a Basic ChatBot graph using LangGraph.
        This method initializes a chatbot node using the 'ChatBotLiteNode' class
        and integrates into the graph. ChatBot Node is set as both Entry and Exit point of the Graph.
        '''
        ## Define Chatbot Node
        self.chatbot_lite_node = ChatbotLiteNode(self.llm)
        
        ## Graph set-up ## Add Nodes       
        self.graph_builder.add_node('chatbot', self.chatbot_lite_node.process)

        ## Define Conditional and Direct Edges
        self.graph_builder.add_edge(START, 'chatbot')
        self.graph_builder.add_edge('chatbot', END)
        
    def chatbot_with_tools_build_graph(self):
        '''
        Builds an advanced Chatbot with Tool integration.
        This method creates Chatbot Graph that inlcudes both a Chatbot Node and a Tool Node.
        It defines Tools, initializes the Chatbot with Tools capabilities, and sets up conditional and direct Edges
        between Nodes. Chatbot Node is set as Entry point of the Graph.
        '''
        ## Define Tool and Tool Node
        self.tools = get_tools()
        self.tool_node = create_tools_node(self.tools)

        ## Define LLM
        # llm = self.llm

        ## Define Chatbot Node
        self.chatbot_with_tools_node_tmp = ChatbotWithToolsNode(self.llm)
        self.chatbot_with_tools_node = self.chatbot_with_tools_node_tmp.create_chatbot_with_tool(self.tools)

        ## Graph set-up  ## Add Nodes
        self.graph_builder.add_node('chatbot', self.chatbot_with_tools_node)
        self.graph_builder.add_node('tools', self.tool_node)
        
        ## Define Conditional and Direct Edges
        self.graph_builder.add_edge(START, 'chatbot')
        self.graph_builder.add_conditional_edges('chatbot', tools_condition)
        self.graph_builder.add_edge('tools', 'chatbot')
        # self.graph_builder.add_edge('chatbot', END)

    def setup_graph(self, use_case:str):
        '''
        Sets up Graph for the selected Use case
        '''        
        if use_case == 'Chatbot Lite':
            self.chatbot_lite_build_graph()
        elif use_case == 'ChatBot with Tools':
            self.chatbot_with_tools_build_graph()
        else:
            raise ValueError(f"Unsupported Use-case: {use_case}")    

        # print("graphBuilder --- Nodes:", self.graph_builder.nodes)
        # print("graphBuilder --- Edges:", self.graph_builder.edges)

        compiledGraph = self.graph_builder.compile()    

        return compiledGraph
    
    




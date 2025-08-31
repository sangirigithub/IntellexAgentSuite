from langgraph.graph import StateGraph, START, END
from src.agenticAi.state.agentState import State
from src.agenticAi.nodes.chatbotLiteNode import ChatbotLiteNode

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
        and integrates into the graph. ChatBot Node is set as both entry and exit point of the graph.
        '''
        self.chatbot_lite_node = ChatbotLiteNode(self.llm)
        ## Graph set-up        
        self.graph_builder.add_node('chatbot', self.chatbot_lite_node.process)

        # Continue with edges and compile
        self.graph_builder.add_edge(START, 'chatbot')
        self.graph_builder.add_edge('chatbot', END)
        

    def setup_graph(self, use_case:str):
        '''
        Sets up Graph for the selected use case
        '''        
        if use_case == 'Chatbot Lite':
            self.chatbot_lite_build_graph()
        else:
            raise ValueError(f"Unsupported Use-case: {use_case}")    

        # print("graphBuilder --- Nodes:", self.graph_builder.nodes)
        # print("graphBuilder --- Edges:", self.graph_builder.edges)

        compiledGraph = self.graph_builder.compile()    

        return compiledGraph
    
    




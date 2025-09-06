from langgraph.graph import StateGraph, START, END
from src.llms.groq import GroqLLM
from src.state.agentState import BlogState
from src.nodes.blogGenNode import BlogNode

class GraphBuilder:
    def __init__(self,llm):
        self.llm=llm
        self.graph=StateGraph(BlogState)

    def build_topic_graph(self):
        '''
        Build a Agent Graph to generate Blogs based on Topic
        '''
        self.blog_node = BlogNode(self.llm)
        # print(self.llm)

        ## Nodes
        self.graph.add_node("title_creation", self.blog_node.title_creation)
        self.graph.add_node("content_generation", self.blog_node.content_generation)

        ## Edges
        self.graph.add_edge(START,"title_creation")
        self.graph.add_edge("title_creation","content_generation")
        self.graph.add_edge("content_generation",END)

        return self.graph    

    def setup_graph(self,usecase):
        
        if usecase == "topic":
            self.build_topic_graph()
        # if usecase=="language":
        #     print("Language block")
        #     self.build_language_graph()

        return self.graph.compile()
    

## LangSmith LangGraph Studio
llm = GroqLLM().get_llm()

## Get Graph
graph_builder = GraphBuilder(llm)
graph = graph_builder.build_topic_graph().compile()    

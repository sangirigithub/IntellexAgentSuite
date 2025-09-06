from src.state.agentState import BlogState, Blog
from langchain_core.messages import SystemMessage, HumanMessage

class BlogNode:
    """
    Class to represent Blog Node
    """

    def __init__(self,llm):
        self.llm=llm

    
    def title_creation(self, state:BlogState):
        """
        create the title for the blog
        """

        if "topic" in state and state["topic"]:
            prompt="""
                   You are an expert Blog Content Writer. Use Markdown formatting and Generate
                   a Blog Title for {topic}. This Title should be creative and SEO friendly.
                   """
            
            system_message = prompt.format(topic=state["topic"])
            print('system_message: ', system_message)

            response = self.llm.invoke(system_message)
            print('response: ', response)

            return {"blog":{"title":response.content}}
        
    def content_generation(self,state:BlogState):

        if "topic" in state and state["topic"]:
            system_prompt = """
                    You are an Expert Blog Content Writer. Use Markdown formatting and
                    Generate a detailed Blog Content with detailed breakdown for the {topic}
            """

            system_message = system_prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)

            return {"blog": {"title": state['blog']['title'], "content": response.content}}    
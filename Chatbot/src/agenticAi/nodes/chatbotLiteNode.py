from src.agenticAi.state.agentState import State

class ChatbotLiteNode:
    """
    Chatbot Lite - Implementation
    """
    def __init__(self, llm):
        self.llm = llm

    def process(self, state:State)->dict:
        """
        Processes the input State and generates a Chatbot response.
        """
        # ## Extract Last User Message
        # user_input = next((msg.content for msg in state['messages'] if isinstance(msg, HumanMessage)), '')
        
        ## Generate Model Response using LLM:
        llm_response = self.llm.invoke(state['messages'])
        # print('Node --- ', llm_response)
        
        return {'messages': llm_response}        
        # return {'messages': state["messages"] + [AIMessage(content=llm_response)]}
    
    
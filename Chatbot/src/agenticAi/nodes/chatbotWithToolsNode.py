from src.agenticAi.state.agentState import State

class ChatbotWithToolsNode:
    '''
    Chatbot application powered with Tool Integration.
    '''
    def __init__(self, llm):
        self.llm = llm

    def process(self, state:State) -> dict:
        '''
        Processes the input State and generates a response with Tool Integration
        '''
        user_input = state['messages'][-1] if state['messages'] else ''

        llm_response = self.llm.invoke([{'role':'user', 'content':user_input}])

        ## Simulate Tool specific logic
        tools_response = f"Tool Integration for '{user_input}'"
        
        return {'messages': [llm_response, tools_response]}

    def create_chatbot_with_tool(self, tools):
        '''
        Returns a Chatbot Node Function.
        '''
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            '''
            Chatbot Logic for processing the input State and returning a response.
            '''
            return {'messages': [llm_with_tools.invoke(state['messages'])]}
        
        return chatbot_node
    
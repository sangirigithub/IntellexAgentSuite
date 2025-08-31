import streamlit as st

class DisplayResponseUI:
    def __init__(self, use_case, graph, user_message):
        self.use_case = use_case
        self.graph = graph
        self.user_message = user_message

    def display_response_ui(self):
        use_case = self.use_case
        graph = self.graph
        user_message = self.user_message

        if use_case == 'Chatbot Lite':            

            try:
                for event in graph.stream({'messages': ('user', user_message)}):                    
                    # print('event.values(): ', event.values())
                    for value in event.values():
                        # print('display_response --- value-messages-content: ', value['messages'].content)

                        with st.chat_message('user'):
                            st.write('User: ', user_message)
                        
                        with st.chat_message('assistant'):
                            st.write('Assistant:', value['messages'].content)                       
            except Exception as e:
                st.error(f'Error Occured during Display {e}')             


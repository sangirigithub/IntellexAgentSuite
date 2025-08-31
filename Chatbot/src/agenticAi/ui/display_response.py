import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

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
            # Prepare State and invoke the Graph
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
                st.error(f'display_response.py --- Error Occured during displaying {e}')             

        elif use_case == 'ChatBot with Tools':  
            # Prepare State and invoke the Graph
            try:
                initial_state = {'messages':[user_message]}
                response = graph.invoke(initial_state)

                for msg in response['messages']:
                    if type(msg) == HumanMessage:
                        with st.chat_message('user'):
                            st.write(msg.content)
                    elif type(msg) == ToolMessage:
                        with st.chat_message('ai'):
                            st.write('Tool Call Starts ... ')
                            st.write(msg.content)
                            st.write('Tool Call Ends ... ')
                    elif type(msg) == AIMessage and msg.content:
                        with st.chat_message('assistant'):
                            st.write(msg.content)
            except Exception as e:
                st.error(f'display_response.py --- Error Occured during displaying {e}') 

        elif use_case == 'AI News':
            frequency = self.user_message

            with st.spinner('Fetching & Summarizing AI News... ⌛'):
                response = graph.invoke({'messages':frequency})
                try:
                    # Read saved Markdown file
                    AI_News_Path = f'./AiNews/{frequency.lower()}_summary.md'
                    with open(AI_News_Path, 'r') as newsFile:
                        markdown_content = newsFile.read()

                    # Display the markdwn content in UI
                    st.markdown(markdown_content, unsafe_allow_html=True)

                except FileNotFoundError:
                    st.error(f'display_response.py --- News Not Generated or File Not Found: {AI_News_Path}')    
                except Exception as e:
                    st.error(f'display_response.py --- An Error Occured: {str(e)}')    

          


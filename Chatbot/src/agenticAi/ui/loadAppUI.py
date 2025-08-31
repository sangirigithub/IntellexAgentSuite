import os
import streamlit as st

from src.agenticAi.ui.uiConfig import UIConfig

class LoadUI():
    def __init__(self):
        self.config = UIConfig()
        self.user_controls = {}

    def load_ui(self):
        st.set_page_config(page_title="🤖 " + str(self.config.get_page_title()), layout='wide')
        # st.header("🤖 " + str(self.config.get_page_title()))
                
        col1, col2 = st.columns([1, 16])
        with col1:
            st.image(r'./src/agenticAi/ui/AiAgent.png', width=40)
            
        with col2:            
            st.header(self.config.get_page_title())
            
        with st.sidebar:
            try:
                ## Get options from UIConfig
                framework_options = self.config.get_framework_options()
                usecase_options = self.config.get_usecase_options()

                ### 1. Framework Selection
                self.user_controls['selected_framework'] = st.selectbox('Select Framework', framework_options)                

                ### 2. Model Selection - Groq
                if self.user_controls['selected_framework'] == 'Groq':
                    ## LLM Selection
                    model_options = self.config.get_groq_model_options()                    
                    self.user_controls['selected_groq_model'] = st.selectbox('Select LLM', model_options)

                    ### 3. API Key Input
                    self.user_controls['GROQ_API_KEY'] = st.session_state['GROQ_API_KEY'] = st.text_input('LLM API Key', type='password', key='api_key_groq')

                    # Groq API Key/Create a New one
                    if not self.user_controls['GROQ_API_KEY']:
                        # st.warning(r"⚠️ Please Enter your API Key to Proceed. \n For Groq access, please refer https://console.groq.com.keys")
                        st.markdown(
                            "<span style='font-size:10px; color:#F39C12;'>⚠️ Please Enter your Groq API Key to Proceed.<br>Groq - https://console.groq.com/keys</span>",
                            unsafe_allow_html=True
                            )

                ### 2. Model Selection - HuggingFace
                if self.user_controls['selected_framework'] == 'HuggingFace':
                    ## LLM Selection
                    model_options = self.config.get_hf_model_options()
                    self.user_controls['selected_hf_model'] = st.selectbox('Select LLM', model_options)    

                    ### 3. API Key Input
                    self.user_controls['HF_API_KEY'] = st.session_state['HF_API_KEY'] = st.text_input('LLM API Key', type='password', key='api_key_hf')

                    # HuggingFace API Key/Create a New one
                    if not self.user_controls['HF_API_KEY']:
                        # st.warning(r"⚠️ Please Enter your API Key to Proceed. \n For HuggingFace access, please refer https://huggingface.co/settings/tokens")
                        st.markdown(
                            "<span style='font-size:10px; color:#F39C12;'>⚠️ Please Enter your HuggingFace API Key to Proceed.<br>HuggingFace - https://huggingface.co/settings/tokens</span>",
                            unsafe_allow_html=True 
                            )        
                    
                ### 4. UseCase Selection
                self.user_controls['selected_usecase'] = st.selectbox('Select UseCase', usecase_options)
                if self.user_controls['selected_usecase'] == 'ChatBot with Tools':
                   os.environ['TAVILY_API_KEY'] = self.user_controls['TAVILY_API_KEY'] = st.session_state['TAVILY_API_KEY'] = st.text_input('TAVILY API KEY', type='password')

                    ### 5. Tavily Web Search API Key/Create a New one
                   if not self.user_controls['TAVILY_API_KEY']:                            
                            st.markdown(
                            "<span style='font-size:10px; color:#F39C12;'>⚠️ Please Enter your Tavily API Key to Proceed.<br>Tavily - https://app.tavily.com/home</span>",
                            unsafe_allow_html=True 
                            ) 

                return self.user_controls
            
            except Exception as e:
                print(f'loadAppUI.py --- An Error Occured: {e}')  
                return None

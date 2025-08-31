import os
import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

class HuggingFaceLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):    
        try:
            hf_api_key = self.user_controls_input['HF_API_KEY']
            
            selected_hf_model = self.user_controls_input['selected_hf_model']

            if hf_api_key == '' and os.environ['HF_API_KEY'] == '':
                st.error('Please Enter HuggingFace API Key:')
                return None

            hf_endpoint = HuggingFaceEndpoint(
            repo_id=selected_hf_model,
            huggingfacehub_api_token=hf_api_key,
            task="text-generation"  # or any appropriate task for your model
            )
            llm_hf = ChatHuggingFace(llm=hf_endpoint)    
            print('Model Initialized is HuggingFace!')
            return llm_hf

        except Exception as e:
            raise ValueError(f'huggingFaceLLM --- Error Occured with Exception: {e}')
            return 






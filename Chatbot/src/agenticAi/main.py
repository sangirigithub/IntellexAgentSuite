import streamlit as st
from src.agenticAi.ui.loadAppUI import LoadUI
from src.agenticAi.llms.groqLLM import GroqLLM
from src.agenticAi.llms.huggingFaceLLM import HuggingFaceLLM
from src.agenticAi.graph.graphBuilder import GraphBuilder
from src.agenticAi.ui.display_response import DisplayResponseUI

def load_agenticAi_app():
    '''
    This function Loads and Runs LangGraph AgenticAi Application using Streamlit UI.
    It initializes the UI, handles User Input, configures Framework and LLM Model,
    sets up Graph based on selected Use Case and then displays the Model Response as output.
    It also implements exception handling for application robustness.
    '''

    ## Load UI
    ui = LoadUI()
    user_inputs = ui.load_ui()
   
    if not user_inputs:
        print('main.py --- Error Failed to Load User Input from the UI. Please fill details on the UI.')
        st.error('main.py --- Error Failed to Load User Input from the UI. Please fill details on the UI.')
        return 
    
    # Text Input for user_message
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.frequency
    else:
        user_message = st.chat_input('Please Enter your Question!')

    if user_message:
        try:
            ## Configure LLM
            if user_inputs.get('selected_framework') == 'Groq':
                llm_config = GroqLLM(user_controls_input=user_inputs)
            if user_inputs.get('selected_framework') == 'HuggingFace':
                llm_config = HuggingFaceLLM(user_controls_input=user_inputs)

            llm = llm_config.get_llm_model()

            if not llm:
                st.error('main.py --- Error: LLm Model could not be initialized!')
                return
            
            ## Initialize and set-up the Graph based on Selected UseCase
            use_case = user_inputs.get('selected_usecase')

            if not use_case:
                st.error('main.py --- Error: Please select Use Case!')
                return
            
            ## Graph builder
            graphBuilder = GraphBuilder(llm)            
            compiledGraph = graphBuilder.setup_graph(use_case)
            ## This function is the deciding factor to call methods based on 
            ## the UseCase being selected

            # DisplayResponseUI(use_case, graph_builder.graph_builder, user_message).display_response_ui()
            DisplayResponseUI(use_case, compiledGraph, user_message).display_response_ui()
            
        except Exception as e:
            st.error(f'main.py --- Error Occured with Exception: {e}')
            return
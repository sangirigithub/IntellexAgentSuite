import src.agenticAi.config as cf
from configparser import ConfigParser

class UIConfig:
    def __init__(self, config_file=cf.uiConfigini_path):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_page_title(self):
        return self.config['DEFAULT'].get('PAGE_TITLE')
        
    def get_framework_options(self):
        return self.config['DEFAULT'].get('FRAMEWORK_OPTIONS').split(', ')
    
    def get_groq_model_options(self):
        return self.config['DEFAULT'].get('GROQ_MODEL_OPTIONS').split(', ')
    
    def get_hf_model_options(self):
        return self.config['DEFAULT'].get('HF_MODEL_OPTIONS').split(', ')
    
    def get_usecase_options(self):
        return self.config['DEFAULT'].get('USECASE_OPTIONS').split(', ')
    

    

    


# Factory to create LLM instances

from gradebotguru.llm_interface.openai import OpenAILLM

def create_llm(provider_name):
    # Placeholder for LLM creation logic
    if provider_name == 'openai':
        return OpenAILLM()
    else:
        raise ValueError("Unsupported LLM provider")

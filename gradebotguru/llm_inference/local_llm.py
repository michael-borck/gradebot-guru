# Implementation for local LLM

from base_llm import BaseLLM

class LocalLLM(BaseLLM):
    def send_prompt(self, prompt):
        # Send the prompt to the local LLM
        # Return the response from the local LLM

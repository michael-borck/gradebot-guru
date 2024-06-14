# OpenAI specific implementation for LLM interface

from llm_interface.base_llm import BaseLLM

class OpenAILLM(BaseLLM):
    def send_prompt(self, prompt):
        # 1. Send the prompt to the OpenAI API
        # 2. Handle the response and any potential errors
        # 3. Return the response from OpenAI
        pass

    def parse_response(self, response):
        # 1. Extract grade and feedback from the OpenAI response
        # 2. Handle potential inconsistencies or errors in the response
        return grade, feedback

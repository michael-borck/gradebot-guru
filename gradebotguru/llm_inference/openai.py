# OpenAI specific implementation for LLM interface

from gradebotguru.llm_interface.base_llm import BaseLLM

class OpenAILLM(BaseLLM):
    def send_prompt(self, prompt):
        # Placeholder for sending prompt to OpenAI API
        return "openai response"

    def parse_response(self, response):
        # Placeholder for parsing response from OpenAI
        return "openai grade", "openai feedback"

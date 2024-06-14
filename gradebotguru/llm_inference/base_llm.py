# Base class/interface for LLMs

class BaseLLM:
    def send_prompt(self, prompt):
        # Placeholder for sending prompt to LLM
        return "response"

    def parse_response(self, response):
        # Placeholder for parsing response from LLM
        return "grade", "feedback"

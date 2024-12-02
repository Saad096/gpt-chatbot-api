import openai
from config import get_openai_api_key

class ChatGPTBotAPI:
    def __init__(self, api_key=None):
        """Initialize the ChatGPT bot API with the given API key."""
        self.api_key = api_key or get_openai_api_key()
        self.prompts = [] 
        self.initialize_gpt3()

    def initialize_gpt3(self):
        """Initialize OpenAI API with the provided API key."""
        openai.api_key = self.api_key

    def create_prompt(self, prompt: str) -> int:
        """Store a user-provided prompt."""
        self.prompts.append(prompt)
        return len(self.prompts) - 1  # Return the index of the new prompt

    def get_response(self, prompt_index: int) -> str:
        """Generate a response for the prompt at the given index."""
        if 0 <= prompt_index < len(self.prompts):
            prompt = self.prompts[prompt_index]
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=150
            )
            return response.choices[0].text.strip()
        else:
            return "Invalid prompt index."

    def update_prompt(self, prompt_index: int, new_prompt: str) -> str:
        """Update an existing prompt with a new prompt."""
        if 0 <= prompt_index < len(self.prompts):
            self.prompts[prompt_index] = new_prompt
            return "Prompt updated successfully."
        else:
            return "Invalid prompt index."

    def list_prompts(self) -> list:
        """Return the list of all stored prompts."""
        return self.prompts

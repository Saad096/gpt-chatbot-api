# app.py
from flask import Flask, request, jsonify
from chatgpt_bot import ChatGPTBotAPI

app = Flask(__name__)

# Initialize ChatGPTBotAPI with your OpenAI API key
bot = ChatGPTBotAPI()

@app.route('/')
def home():
    """Return a simple welcome message with available endpoints."""
    return jsonify({
        "message": "Welcome to the ChatGPT Bot API!",
        "endpoints": {
            "Create Prompt": "/prompts (POST)",
            "Get Response": "/prompts/<prompt_index> (GET)",
            "Update Prompt": "/prompts/<prompt_index> (PUT)",
            "List Prompts": "/prompts (GET)"
        }
    })

@app.route('/prompts', methods=['POST'])
def create_prompt():
    """Create a new prompt and store it."""
    data = request.json
    if "prompt" not in data:
        return jsonify({"error": "Prompt is required"}), 400
    index = bot.create_prompt(data["prompt"])
    return jsonify({"message": "Prompt created", "index": index}), 201

@app.route('/prompts/<int:prompt_index>', methods=['GET'])
def get_response(prompt_index):
    """Get the response from the ChatGPT bot for the given prompt index."""
    response = bot.get_response(prompt_index)
    return jsonify({"response": response})

@app.route('/prompts/<int:prompt_index>', methods=['PUT'])
def update_prompt(prompt_index):
    """Update an existing prompt with a new one."""
    data = request.json
    if "new_prompt" not in data:
        return jsonify({"error": "New prompt is required"}), 400
    message = bot.update_prompt(prompt_index, data["new_prompt"])
    return jsonify({"message": message})

@app.route('/prompts', methods=['GET'])
def list_prompts():
    """Return the list of stored prompts."""
    return jsonify({"prompts": bot.list_prompts()})

if __name__ == '__main__':
    app.run(debug=True)

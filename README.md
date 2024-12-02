# ChatGPT Bot API

This project implements a simple ChatGPT Bot API using Flask, allowing users to interact with the OpenAI API for managing user prompts and generating responses. It supports *CRUD operations* to create, read, update, and delete prompts.

## Features

- Initialize GPT-3: Sets up the OpenAI API for usage.
- Store Prompts: Save user prompts for later use.
- Generate Responses: Retrieve responses from OpenAI's GPT-3 for stored prompts.
- Update Prompts: Modify existing prompts with new content.
- Delete Prompts: Remove stored prompts when no longer needed.

## Directory Structure

├── app.py                     
├── chatgpt_bot.py             
├── config.py                  
└── README.md                  

## Prerequisites

### Software Requirements
- Python 3.10
- An OpenAI API key

## Installation and Setup

### Step 1: Clone the repository
```bash
git clone https://github.com/Saad096/Assessment.git
cd Assessment
```


### Step 2: Create a virtual environment
```bash
python -m venv env
source env/bin/activate  
```
python -m venv env
source env/bin/activate  

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```


### Step 4: Configure API Key
1. Create a `.env` file in the project root.
2. Add your OpenAI API key:
```json
OPENAI_API_KEY="your_openai_api_key"
```
   


## Usage

### Step 1: Start the Flask Application

```bash
python3 app.py
```



The API will be available at `http://127.0.0.1:5000`.


## API Endpoints

### 1. Initialize GPT-3
- URL: `/initialize`
- Method: `GET`
- Description: Initializes the OpenAI API with the provided API key.
- Response:

  {
    "message": "GPT-3 initialized with provided API key."
  }


### 2. Create a Prompt
- URL: `/prompts`
- Method: `POST`
- Request Body:
```json
{
  "prompt": "Hello, ChatGPT!"
}
```
  
```json
Response:
  {
    "message": "Prompt added successfully",
    "index": 0
  }
```

### 3. Get GPT-3 Response for a Prompt
- URL: `/prompts/<prompt_index>`
- Method: `GET`
- Response:
```json
{
    "prompt": "Hello, ChatGPT!",
    "response": "Hi! How can I assist you today?"
}
```
  


### 4. Update a Prompt
- URL: `/prompts/<prompt_index>`
- Method: `PUT`

- Request Body:
```json
{
    "new_prompt": "Updated prompt text"
}
```
  
- Response:

```json
{
    "message": "Prompt updated successfully"
}

```
  
### 5. Delete a Prompt
- URL: `/prompts/<prompt_index>`
- Method: `DELETE`
- Response:
```json
{
    "message": "Prompt deleted successfully"
}
```
  


## Testing the API

Use tools like Postman, CURL, or a browser-based API client to test the endpoints. Example using `curl`:
```bash
curl -X POST http://127.0.0.1:5000/prompts -H "Content-Type: application/json" -d '{"prompt": "Hello, ChatGPT!"}'
```


## License

This project is licensed under the MIT License.


## Acknowledgments

- OpenAI GPT-3 for powering the chatbot responses.
- Flask framework for the API implementation.
import openai
import os
from dotenv import load_dotenv
import hashlib

# Load environment variables from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Token usage tracking
used_tokens = 0
MAX_TOKEN_BUDGET = 10_000  # Set a token budget for cost control

# Caching mechanism
cache = {}

def get_cached_response(prompt):
    """
    Retrieve a cached GPT response for a given prompt.
    """
    prompt_hash = hashlib.sha256(prompt.encode()).hexdigest()
    if prompt_hash in cache:
        return cache[prompt_hash]
    return None

def save_cached_response(prompt, response):
    """
    Save a GPT response to the cache.
    """
    prompt_hash = hashlib.sha256(prompt.encode()).hexdigest()
    cache[prompt_hash] = response

def generate_test_cases_with_gpt3(user_story, max_cases=3):
    """
    Generate detailed test cases using GPT-3.5-turbo based on the provided user story.
    """
    global used_tokens

    # Define the prompt
    prompt = f"""
    You are a test case generation assistant. Generate up to {max_cases} detailed test cases for the following user story.
    Each test case should include:
    - Step: [Action]
    - Expected Result: [Outcome]

    User Story: {user_story}
    """

    # Check cache
    cached_response = get_cached_response(prompt)
    if cached_response:
        return cached_response

    # Check token budget
    if used_tokens >= MAX_TOKEN_BUDGET:
        return "Token budget exceeded. Please optimize your usage or increase the budget."

    try:
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a test case generation assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,  # Limit tokens for cost control
            temperature=0.2  # Deterministic output
        )

        # Extract response
        test_cases = response['choices'][0]['message']['content']

        # Update token usage
        used_tokens += response['usage']['total_tokens']

        # Cache the response
        save_cached_response(prompt, test_cases)

        return test_cases

    except openai.error.OpenAIError as e:
        return f"Error generating test cases: {e}"

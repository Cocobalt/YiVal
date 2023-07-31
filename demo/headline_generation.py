import os

import openai

from yival.logger.token_logger import TokenLogger
from yival.wrappers.string_wrapper import StringWrapper


def headline_generation_for_business(tech_startup_business: str) -> str:
    logger = TokenLogger()
    logger.reset()
    # Ensure you have your OpenAI API key set up
    openai.api_key = os.getenv("OPENAI_API_KEY")
    messages = [{
        "role":
        "system",
        "content":
        "You are a helpful assistant that help company grow."
    }, {
        "role":
        "user",
        "content":
        str(StringWrapper("Generate landing page headline for", name="task")) +
        f'{tech_startup_business}'
    }]
    # Use the chat-based completion
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
    res = response['choices'][0]['message']['content']
    token_usage = response['usage']['total_tokens']
    logger.log(token_usage)
    return res
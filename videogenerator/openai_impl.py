import os
from openai import OpenAI

import logging
from .app.config import Config
config = Config()

# Initialize the logging module
logging.basicConfig(filename='openai_interaction.log', level=logging.INFO)
logging.info('Logging initialized.')
_model = config.OPENAI_MODEL
def getClient():
    return OpenAI(
        # This is the default and can be omitted
        api_key=config.OPENAI_API_KEY,
        )
def get_json (prompt):
    msgs = [{"role": "user", "content": prompt}]
    return getCode(msgs)



def getCode(msgs):
    # Logging input
    logging.info(f"Sending request to OpenAI with messages: {msgs}")
    model = _model
    client = getClient()
    response = client.chat.completions.create(
        model=model, messages=msgs, temperature=0.5)
    # , max_tokens=150, top_p=1, frequency_penalty=0.0, presence_penalty=0.0, stop=["\n", " Human:", " AI:"]
    # Logging output
    logging.info(
        f"Received response from OpenAI: {response.choices[0].message.content}")
    return response.choices[0].message.content


def prep_history(history, context, prompt, response):
    """
    Format history like:
    [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
    """
    prompt_ = response_ = None
    print("prop history: ", history)

    if history is None:
        history = []
    if context is not None and context != "":
        if isinstance(context, str):
            msg = {"role": "user", "content": context}
            history.append(msg)
        elif isinstance(context, list):
            for item in context:
                msg = {"role": "user", "content": item}
                history.append(msg)
    if prompt is not None and prompt != "":
        msg = {"role": "user", "content": prompt}
        history.append(msg)
    if response is not None and response != "":
        msg = {"role": "assistant", "content": response}
        history.append(msg)
    return history

def test ():
    # Test the getCode method
    print("Testing getCode method")
    msgs = [
        {"role": "user", "content": "Provide create table script (mysql) for creating the user table with the following columns: id, name, email, password, created_at, updated_at"},
    ]
    return getCode(msgs)

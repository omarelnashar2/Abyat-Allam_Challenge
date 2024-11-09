from openai import OpenAI
from constants import available_models, body_allam_original, body_allam_tuned
import requests
import os

client = OpenAI()

def get_res(prompt, body, url):
    """
    Sends a request to a specified API endpoint with the given prompt and body, 
    then retrieves and returns the generated response from the model.

    Args:
        prompt (str): The input text or prompt that will be sent to the model for processing.
        body (dict): The body of the request, which contains the model's input format.
        url (str): The API endpoint URL to send the request to.

    Returns:
        str: The generated text from the model, extracted from the response JSON.

    Raises:
        Exception: If the API response status code is not 200, an exception is raised with the error message.


    """
    body["input"]=prompt
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ['ALLAM_ACCESS_TOKEN']} "
    }

    response = requests.post(
        url,
        headers=headers,
        json=body
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))
    result = response.json()["results"][0]["generated_text"]
    return result


def get_llm_response(prompt, model):
    """
    Retrieves the response from a language model based on the provided prompt and selected model.

    Depending on the model chosen, it sends the prompt to 
    (Allam) or to OpenAI's GPT-4 model for processing.

    Args:
        prompt (str): The input text or prompt that will be sent to the language model.
        model (str): The model identifier (e.g., "Allam", "Fine-tuned", "GPT-4o-mini") that determines 
                        which model is used for generating the response.

    Returns:
        str: The generated text from the language model.

    """
    print("model:", model)
    print("prompt:", prompt)

    if model == available_models[0]:   # original Allam
        res = get_res(prompt, body_allam_original, os.environ['ALLAM_ORIGINAL_URL'])
    elif model == available_models[1]: # Fine-tuned
        res = get_res(prompt, body_allam_tuned, os.environ['ALLAM_FINTUNED_URL'])
    elif model == available_models[2]: # GPT4o
        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            n=1,
            stop=None,
            temperature=0.7
        ).choices[0].message.content.strip()
    else:
        res = ""

    return res

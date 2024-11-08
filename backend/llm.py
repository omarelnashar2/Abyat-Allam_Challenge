from openai import OpenAI
from constants import available_models, body_allam_original, body_allam_tuned
import requests
import os

client = OpenAI()

def get_res(prompt, body, url):

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

import requests
import os
def correct_transcription(transcript):
    url = "https://internshala.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer 22ec84421ec24230a3638d1b51e3a7dc",  # Use your API Key directly
    }
    data = {
        "messages": [{"role": "user", "content": transcript}],
        "model": "gpt-4o",
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        raise Exception(f"Error from OpenAI API: {response.text}")
    return response.json()["choices"][0]["message"]["content"]
import requests

def euri_completion(messages, temperature=0.3, max_tokens=1000):
    url = "https://api.euron.one/api/v1/euri/alpha/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer Your-Euri-API-key"
    }
    
    payload = {
        "messages": messages,
        "model": "gpt-4.1-nano",
        "max_tokens": max_tokens,
        "temperature": temperature
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"]
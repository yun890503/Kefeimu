import requests

def ask_chatgpt(prompt, engine="gpt-3.5-turbo-instruct", temperature=0.7, max_tokens=150):
    api_url = f"https://api.openai.com/v1/engines/{engine}/completions"
    

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    data = {
        "prompt": prompt,
        "temperature": temperature,
        "max_tokens": max_tokens
    }

    response = requests.post(api_url, headers=headers, json=data)
    response_json = response.json()

    if response.status_code == 200:
        # Extract and return the text response.
        return response_json["choices"][0]["text"].strip()
    else:
        # In case of an error, print the error message.
        print(f"Error: {response_json.get('error', {}).get('message', 'Unknown error')}")
        return None

# Example usage of the function
prompt = "使用者輸入的文字"
print(ask_chatgpt(prompt))

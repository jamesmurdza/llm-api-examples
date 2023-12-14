# LLM API call examples

This repository contains a list of working code examples for calling various LLM APIs.

[README.md](README.md) is the source of truth and contains all examples in `curl` format.

[README-python.md](README-python.md) contains the same examples in Python, and is generated automatically using GPT-3.5 whenever README.md is updated.

## Table of Contents

- [OpenAI](#openai)
- [Anthropic](#anthropic)
- [Mistral](#mistral)
- [Google](#google)

## OpenAI

🔑 Get API key [here](https://platform.openai.com/account/api-keys).

### Chat
```python
import requests
import os

response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer " + os.environ["OPENAI_API_KEY"]
    },
    json={
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"}
        ]
    }
)
```

### Embeddings
```python
import requests
import os

response = requests.post(
    "https://api.openai.com/v1/embeddings",
    headers={
        "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
        "Content-Type": "application/json",
    },
    json={
        "input": "The food was delicious and the wine...",
        "model": "text-embedding-ada-002",
        "encoding_format": "float"
    }
)
```

## Anthropic

🔑 Get API key [here](https://console.anthropic.com/account/keys).

### Chat
```python
import requests
import os

response = requests.post(
    "https://api.anthropic.com/v1/complete",
    headers={
        'accept': 'application/json',
        'anthropic-version': '2023-06-01',
        'content-type': 'application/json',
        'x-api-key': os.environ.get('ANTHROPIC_API_KEY')
    },
    json={
        "model": "claude-2.1",
        "prompt": "\n\nHuman: Hello, world!\n\nAssistant:",
        "max_tokens_to_sample": 256
    }
)
```

## Mistral

🔑 Get API key [here](https://console.mistral.ai/users/api-keys/).

### Chat
```python
import requests
import os

response = requests.post(
    "https://api.mistral.ai/v1/chat/completions",
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {os.environ['MISTRAL_API_KEY']}"
    },
    json={
        "model": "mistral-tiny",
        "messages": [{"role": "user", "content": "Who is the most renowned French writer?"}]
    }
)
```

### Embeddings
```python
import requests
import os

response = requests.post(
    "https://api.mistral.ai/v1/embeddings",
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer " + os.environ.get("MISTRAL_API_KEY")
    },
    json={
        "model": "mistral-embed",
        "input": ["Embed this sentence.", "As well as this one."]
    }
)
```

## Google

🔑 Get API key [here](https://makersuite.google.com/app/apikey).

### Chat
```python
import requests
import os

response = requests.post(
    "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + os.environ['GOOGLE_API_KEY'],
    headers={'Content-Type': 'application/json'},
    json={
        "contents": [
            {
                "parts": [
                    {
                        "text": "Write a story about a magic backpack."
                    }
                ]
            }
        ]
    }
)
```

### Embeddings
```python
import requests
import os

response = requests.post(
    "https://generativelanguage.googleapis.com/v1beta/models/embedding-001:generateContent?key=" + os.environ["GOOGLE_API_KEY"],
    headers={"Content-Type": "application/json"},
    json={
        "contents": [
            {
                "parts": [
                    {
                        "text": "This is a sentence."
                    }
                ]
            }
        ]
    }
)
```

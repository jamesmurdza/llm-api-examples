## Table of Contents

- [OpenAI](#openai)
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
        "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}"
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
        "Content-Type": "application/json"
    },
    json={
        "input": "The food was delicious and the wine...",
        "model": "text-embedding-ada-002",
        "encoding_format": "float"
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
        "Authorization": "Bearer " + os.environ["MISTRAL_API_KEY"]
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
        "Authorization": f"Bearer {os.environ['MISTRAL_API_KEY']}"
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
    "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + os.environ["GOOGLE_API_KEY"],
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
    "https://generativelanguage.googleapis.com/v1beta/models/embedding-001:generateContent?key=" + os.environ.get('GOOGLE_API_KEY'),
    headers={'Content-Type': 'application/json'},
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

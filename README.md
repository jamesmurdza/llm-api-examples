# LLM API call examples

This repository contains a list of working code examples for calling various LLM APIs.

[README.md](README.md) is the source of truth and contains all examples in `curl` format.

[README-python.md](README-python.md) contains the same examples in Python, and is generated automatically using GPT-3.5 whenever README.md is updated.

[README-js.md](README-js.md) contains the same examples in JavaScript, and is generated automatically using GPT-3.5 whenever README.md is updated.

See also: [List of cloud hosts for inference and fine-tuning](https://github.com/jamesmurdza/awesome-inference-hosts)

## Table of Contents

- [OpenAI](#openai)
- [Anthropic](#anthropic)
- [Cohere](#cohere)
- [Mistral](#mistral)
- [Google](#google)
- [Groq](#groq)

## OpenAI

🔑 Get API key [here](https://platform.openai.com/account/api-keys).

📃 API [docs](https://platform.openai.com/docs/).

### Chat
```bash
curl "https://api.openai.com/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Hello!"
      }
    ]
  }'
```

### Embeddings
```bash
curl "https://api.openai.com/v1/embeddings" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": "The food was delicious and the wine...",
    "model": "text-embedding-ada-002",
    "encoding_format": "float"
  }'
```

## Anthropic

🔑 Get API key [here](https://console.anthropic.com/account/keys).

📃 API [docs](https://docs.anthropic.com/).

### Chat
```bash
curl "https://api.anthropic.com/v1/complete" \
  -H 'accept: application/json' \
  -H 'anthropic-version: 2023-06-01' \
  -H 'content-type: application/json' \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -d '{
    "model": "claude-2.1",
    "prompt": "\n\nHuman: Hello, world!\n\nAssistant:",
    "max_tokens_to_sample": 256
  }'
```

## Cohere

🔑 Get API key [here](https://dashboard.cohere.com/api-keys).

📃 API [docs](https://docs.cohere.com/).

### Chat
```bash
curl "https://api.cohere.ai/v1/chat" \
  -H 'accept: application/json' \
  -H 'content-type: application/json' \
  -H "Authorization: Bearer $COHERE_API_KEY" \
  -d '{
    "chat_history": [
      {"role": "USER", "message": "Who discovered gravity?"},
      {"role": "CHATBOT", "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton"}
    ],
    "message": "What year was he born?",
    "connectors": [{"id": "web-search"}]
  }'
```

### Embeddings
```bash
curl "https://api.cohere.ai/v1/embed" \
  -H 'accept: application/json' \
  -H 'content-type: application/json' \
  -H "Authorization: Bearer $COHERE_API_KEY" \
  -d '{
      "texts": [
        "hello",
        "goodbye"
      ],
      "truncate": "END"
  }'
```

## Mistral

🔑 Get API key [here](https://console.mistral.ai/users/api-keys/).

📃 API [docs](https://docs.mistral.ai/api/).

### Chat
```bash
curl "https://api.mistral.ai/v1/chat/completions" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H "Authorization: Bearer $MISTRAL_API_KEY" \
  -d '{
    "model": "mistral-tiny",
    "messages": [{"role": "user", "content": "Who is the most renowned French writer?"}]
  }'
```

### Embeddings
```bash
curl "https://api.mistral.ai/v1/embeddings" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H "Authorization: Bearer $MISTRAL_API_KEY" \
  -d '{
    "model": "mistral-embed",
    "input": ["Embed this sentence.", "As well as this one."]
  }'
```

## Google

🔑 Get API key [here](https://makersuite.google.com/app/apikey).

📃 API [docs](https://ai.google.dev/api/rest).

### Chat
```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$GOOGLE_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Write a story about a magic backpack."
          }
        ]
      }
    ]
  }'
```

### Embeddings
```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/embedding-001:generateContent?key=$GOOGLE_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "This is a sentence."
          }
        ]
      }
    ]
  }'
```

## Groq

🔑 Get API key [here](https://console.groq.com/keys).

📃 API [docs](https://console.groq.com/docs/).

### Chat
```bash
curl "https://api.groq.com/openai/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $GROQ_API_KEY" \
  -d '{
    "model": "mixtral-8x7b-32768",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Hello!"
      }
    ]
  }'
```

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

## OpenAI

🔑 Get API key [here](https://platform.openai.com/account/api-keys).

📃 API [docs](https://platform.openai.com/docs/).

### Chat
```javascript
const fetch = require("node-fetch");
const response = await fetch("https://api.openai.com/v1/chat/completions", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${process.env.OPENAI_API_KEY}`
    },
    body: JSON.stringify({
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
    })
}).then((response) => response.json());
```

### Embeddings
```javascript
const fetch = require("node-fetch");
const response = await fetch("https://api.openai.com/v1/embeddings", {
    headers: {
        "Authorization": `Bearer ${process.env.OPENAI_API_KEY}`,
        "Content-Type": "application/json"
    },
    method: "POST",
    body: JSON.stringify({
        "input": "The food was delicious and the wine...",
        "model": "text-embedding-ada-002",
        "encoding_format": "float"
    })
}).then((response) => response.json());
```

## Anthropic

🔑 Get API key [here](https://console.anthropic.com/account/keys).

📃 API [docs](https://docs.anthropic.com/).

### Chat
```javascript
const fetch = require("node-fetch");
const response = await fetch("https://api.anthropic.com/v1/complete", {
    method: "POST",
    headers: {
        "accept": "application/json",
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
        "x-api-key": process.env.ANTHROPIC_API_KEY
    },
    body: JSON.stringify({
        "model": "claude-2.1",
        "prompt": "\\n\\nHuman: Hello, world!\\n\\nAssistant:",
        "max_tokens_to_sample": 256
    })
}).then((response) => response.json());
```

## Cohere

🔑 Get API key [here](https://dashboard.cohere.com/api-keys).

📃 API [docs](https://docs.cohere.com/).

### Chat
```javascript
const fetch = require("node-fetch");
const response = await fetch("https://api.cohere.ai/v1/chat", {
    method: "POST",
    headers: {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": `Bearer ${process.env.COHERE_API_KEY}`
    },
    body: JSON.stringify({
        "chat_history": [
            {"role": "USER", "message": "Who discovered gravity?"},
            {"role": "CHATBOT", "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton"}
        ],
        "message": "What year was he born?",
        "connectors": [{"id": "web-search"}]
    })
}).then((response) => response.json());
```

### Embeddings
```javascript
const fetch = require("node-fetch");
const response = await fetch("https://api.cohere.ai/v1/embed", {
    method: "POST",
    headers: {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": `Bearer ${process.env.COHERE_API_KEY}`
    },
    body: JSON.stringify({
        "texts": [
            "hello",
            "goodbye"
        ],
        "truncate": "END"
    })
}).then((response) => response.json());
```

## Mistral

🔑 Get API key [here](https://console.mistral.ai/users/api-keys/).

📃 API [docs](https://docs.mistral.ai/api/).

### Chat
```javascript
const fetch = require("node-fetch");
const response = await fetch("https://api.mistral.ai/v1/chat/completions", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": `Bearer ${process.env.MISTRAL_API_KEY}`
    },
    body: JSON.stringify({
        "model": "mistral-tiny",
        "messages": [{"role": "user", "content": "Who is the most renowned French writer?"}]
    })
}).then((response) => response.json());
```

### Embeddings
```javascript
const fetch = require("node-fetch");
const response = await fetch("https://api.mistral.ai/v1/embeddings", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": `Bearer ${process.env.MISTRAL_API_KEY}`
    },
    body: JSON.stringify({
        "model": "mistral-embed",
        "input": ["Embed this sentence.", "As well as this one."]
    })
}).then((response) => response.json());
```

## Google

🔑 Get API key [here](https://makersuite.google.com/app/apikey).

📃 API [docs](https://ai.google.dev/api/rest).

### Chat
```javascript
const fetch = require("node-fetch");
const response = await fetch("https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + process.env.GOOGLE_API_KEY, {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        "contents": [
            {
                "parts": [
                    {
                        "text": "Write a story about a magic backpack."
                    }
                ]
            }
        ]
    })
}).then((response) => response.json());
```

### Embeddings
```javascript
const fetch = require("node-fetch");
const response = await fetch("https://generativelanguage.googleapis.com/v1beta/models/embedding-001:generateContent?key=" + process.env.GOOGLE_API_KEY, {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        "contents": [
            {
                "parts": [
                    {
                        "text": "This is a sentence."
                    }
                ]
            }
        ]
    })
}).then((response) => response.json());
```

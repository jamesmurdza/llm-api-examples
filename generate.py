import re
import os
from openai import OpenAI

# Function to replace bash code blocks with python code blocks
def replace_bash_with_python(match):
    bash_code = match.group(1)
    
    # Initialize the OpenAI client
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY")
    )

    # Call OpenAI API to translate Bash to Python
    prompt = f'''\
{bash_code}
convert this block of code as concisely as possible to
```python
import requests
import os

response = requests.post(
    "https://...",
    headers={
        ...
    },
    ...
)
```
use os.environ to get API keys
don't use intermediate variables
always use code fences ```python and ``` around code blocks in the output
'''
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="gpt-3.5-turbo"
    )

    python_code = response.choices[0].message.content.strip()
    return python_code

# Read the content of README.md
with open("README.md", "r") as readme_file:
    readme_content = readme_file.read()

# Define the regular expression pattern to match bash code blocks
pattern = r"```bash\n(.*?)```"

# Use re.sub() to find and replace bash code blocks with python code blocks
pythonized_content = re.sub(pattern, replace_bash_with_python, readme_content, flags=re.DOTALL)

# Write the updated content back to README.md
with open("README-python.md", "w") as readme_file:
    readme_file.write(pythonized_content)

print("Bash code blocks replaced with Python code blocks in README.md")
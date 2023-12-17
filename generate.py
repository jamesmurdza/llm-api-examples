import re
from codechain.generation import ModifyCodeChain
from langchain.chat_models import ChatOpenAI

bash_to_python_prompt = '''\
convert this block of code as concisely as possible to
```python
import requests
import os

response = requests.post(
    "https://...",
    headers={{
        ...
    }},
    ...
)
```
use os.environ to get API keys
don't use intermediate variables
'''

# Function to replace bash code blocks with python code blocks
def replace_bash_with_python(match):
    bash_code = match.group(1)

    # Call OpenAI API to translate Bash to Python
    generator = ModifyCodeChain.from_instruction(
        bash_to_python_prompt,
        ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)
    )
    result = '```python\n' + generator.run(bash_code) + '\n```'
    return result

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
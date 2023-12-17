import re
from codechain.generation import ModifyCodeChain
from langchain.chat_models import ChatOpenAI

bash_to_python_prompt = """\
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
always use double quotes
"""

prompts = {"python": bash_to_python_prompt}

def transpile_readme(readme_content, to_language):
    # Function to replace bash code blocks with python code blocks
    def transpile_block(match):
        bash_code = match.group(1)
        generator = ModifyCodeChain.from_instruction(
            prompts[to_language], ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)
        )
        result = f"```{to_language}\n{generator.run(bash_code)}\n```"
        print(result)
        return result

    # Use re.sub() to find and replace bash code blocks with python code blocks
    return re.sub(
        r"```bash\n(.*?)```", transpile_block, readme_content, flags=re.DOTALL
    )

# Read the content of README.md
with open("README.md", "r") as readme_file:
    readme_content = readme_file.read()

# Write the updated content back to README.md
with open("README-python.md", "w") as readme_file:
    readme_file.write(transpile_readme(readme_content, "python"))
    print("Wrote README-python.md")
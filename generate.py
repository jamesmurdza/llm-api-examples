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

bash_to_javascript_prompt = """\
convert this block of code as concisely as possible to
```javascript
const fetch = require("node-fetch");
const response = await fetch("https://...",{{
    ...
    body: ...
}}).then((response) => response.json());
```
use process.env to get API keys
don't use intermediate variables
always use double quotes
"""

prompts = {
    "python": bash_to_python_prompt,
    "javascript": bash_to_javascript_prompt,
}

def transpile_readme(readme_content, to_language):
    # Function to replace bash code blocks with python code blocks
    def transpile_block(match):
        bash_code = match.group(1)
        generator = ModifyCodeChain.from_instruction(
            prompts[to_language], ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)
        )
        return f"```{to_language}\n{generator.run(bash_code)}\n```"

    # Use re.sub() to find and replace bash code blocks with python code blocks
    return re.sub(
        r"```bash\n(.*?)```", transpile_block, readme_content, flags=re.DOTALL
    )

# Read the content of README.md
with open("README.md", "r") as readme_file:
    readme_content = readme_file.read()

# Write the transpiled README-python.md and README-javascript.md
with open("README-python.md", "w") as readme_file:
    readme_file.write(transpile_readme(readme_content, "python"))
    print("Wrote README-python.md")
with open("README-js.md", "w") as readme_file:
    readme_file.write(transpile_readme(readme_content, "javascript"))
    print("Wrote README-js.md")
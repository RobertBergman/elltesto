from dotenv import load_dotenv

load_dotenv()

import ell
import re

def save_code_to_file(input_string):
    # Regular expression pattern to match the code block
    pattern = r"```python\n(.*?)```"
    print(input_string)
    # Find the code block in the input string
    match = re.search(pattern, input_string, re.DOTALL)

    if match:
        # Extract the code from the matched group
        code = match.group(1)

        try:
            # Write the code to 'result.py'
            with open('result.py', 'w') as file:
                file.write(code)
            print("Code successfully saved to 'result.py'")
        except IOError as e:
            print(f"An error occurred while saving the file: {e}")
    else:
        print("No valid Python code block found in the input string.")


@ell.simple(model="gpt-4o")
def hello(name: str):
    """You are a helpful assistant.""" # System prompt
    return f"generate that code for a game called {name}!" # User prompt

greeting = hello("snake")

save_code_to_file(greeting)
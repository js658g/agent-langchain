from langchain.tools import Tool
from langchain.utilities import PythonREPL
import os

# Create a Python REPL tool
repl_tool = Tool(
    name="python_repl",
    description="A Python shell. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`",
    func=PythonREPL().run,
)

# Example usage within an agent:
# (This is simplified, agents typically have more complex logic)
def execute_code(code_prompt):
    """
    Executes Python code using the Python REPL tool.
    """
    return repl_tool.func(code_prompt)

# Example input prompt
prompt = "Calculate the sum of 10 and 15"

# Execute the code
result = execute_code(prompt)

print(f"Result: {result}")

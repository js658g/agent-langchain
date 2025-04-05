from dotenv import load_dotenv, find_dotenv
import openai
import os
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_experimental.tools import PythonREPLTool
import scanpy as sc

load_dotenv(find_dotenv())
openai.api_key = os.environ["OPENAI_API_KEY"]

agent_executor = create_python_agent(
    llm=ChatOpenAI(temperature=0, model="gpt-4-1106-preview"),
    tool=PythonREPLTool(),
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    agent_executor_kwargs={"handle_parsing_errors": True},
)
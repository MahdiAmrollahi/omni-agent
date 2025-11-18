from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_agent
from langchain_core.prompts import MessagesPlaceholder
from dotenv import load_dotenv
from .messages import SYSTEM_MESSAGE

import os

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=os.getenv("GEMINI_API_KEY"))
template = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_MESSAGE),
    MessagesPlaceholder(variable_name="history",optional=True) 
])

def agent_create(tools,template=template):
    return template | model.bind_tools(tools)



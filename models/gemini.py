from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import hub
from langchain.agents import Tool, create_react_agent

import os
from langchain_core.prompts import BasePromptTemplate
from langchain_core.prompts import PromptTemplate

os.environ["LANGCHAIN_API_KEY"] = "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"


llm = ChatGoogleGenerativeAI(model="gemini-pro",
      google_api_key="AIzaSyA7PUMgam6YHY0bxgDAWp6rTY3HIJpgrkQ",
      convert_system_message_to_human = True,
      verbose = True,
)

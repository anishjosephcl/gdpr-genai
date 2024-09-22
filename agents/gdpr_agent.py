import json
from models.gemini import llm
from pydantic import BaseModel, ValidationError



def gdpr_agent(state):
  rules = state["rules"]
  request = state["messages"]
  res = llm.invoke(f"""
  You are an checking if the user inputs contains personal data that should be protected under the GDPR. 
  A set of rules are provided to you to do the check.
  Only use the rules provided to you.
  Your output should if the input us compliant or non-compliant. Provide a reason for not being compliant.
 
  Here is the user input:
  {request}
  ---
  Here are the rules:
  {rules}
  """)
  print("The result is",res.content)
  

  return {"finalresult":[res.content]}
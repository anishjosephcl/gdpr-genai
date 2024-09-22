from database.query import extract_rules
def rule_agent(state):
    # Call the extract_rules function
    result = extract_rules()
    print("The result is ",result)
    # Return the state variable
    return {"rules": result,"user_id": "Anish"}
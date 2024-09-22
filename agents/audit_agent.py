from database.audit import insert_into_audit_table
import datetime
import random

def audit_agent(state):
    result = "Not audited"
    issue_detected = parse_list(state["finalresult"])
    if len(issue_detected) > 0:
        issue = issue_detected[0]
        id = random.randint(1, 1000)
        user_id = state["userid"]
        
        timestamp = datetime.datetime.now()
        result = insert_into_audit_table(id, user_id, timestamp, issue)
        print("The result is ",result)
    # Return the state variable
    return {"auditstatus": result}
def parse_list(lst):
    extracted_values = []
    for item in lst:
        values = item.split(",")
        if len(values) > 1 and values[1].strip() != "":
            extracted_values.append(values[1].strip())
    return extracted_values
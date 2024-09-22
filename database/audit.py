import sqlite3

def insert_into_audit_table(id, user_id, timestamp, issue_detected):
    # Connect to the database
    conn = sqlite3.connect('gdpr_rules.db')
    cursor = conn.cursor()

    # Create a tuple with the values to be inserted
    row = (id, user_id, timestamp, issue_detected)

    # Insert the row into the audit table
    cursor.execute("INSERT INTO audit (id, user_id, timestamp, issue_detected) VALUES (?, ?, ?, ?)", (id, user_id, timestamp, issue_detected))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
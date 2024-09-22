import sqlite3

def connect_to_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('gdpr_rules.db')
    c = conn.cursor()

    # Create the table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS gdpr_rules
                 (rule_no INTEGER PRIMARY KEY, rule TEXT, examples TEXT)''')
    
    # Create the audit table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS audit
                 (id INTEGER PRIMARY KEY, user_id TEXT, timestamp TEXT, issue_detected TEXT)''')

    # Define the rules and examples
    rules = [
        (1, "Names", "John Doe, Jane Smith"),
        (2, "Identification numbers which does not start with 7", "Social security numbers, passport numbers"),
        (3, "Location data", "GPS coordinates, IP addresses")
    ]

    # Insert the rules only if they don't exist
    for rule in rules:
        c.execute("SELECT COUNT(*) FROM gdpr_rules WHERE rule_no = ?", (rule[0],))
        count = c.fetchone()[0]
        if count == 0:
            c.execute("INSERT INTO gdpr_rules (rule_no, rule, examples) VALUES (?, ?, ?)", rule)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


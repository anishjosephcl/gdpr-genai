import sqlite3

def extract_rules():
    # Connect to the database
    conn = sqlite3.connect('gdpr_rules.db')
    cursor = conn.cursor()

    try:
        # Execute the query to extract records from gdpr_rules table
        cursor.execute('SELECT * FROM gdpr_rules')
        rules = cursor.fetchall()

        # Process the extracted records
        for rule in rules:
            # Do something with each record
            print(rule)
        return rules
    except sqlite3.Error as e:
        print(f"Error extracting records: {e}")
        # Return the extracted records
        return rules
    finally:
        # Close the database connection
        conn.close()
        return rules
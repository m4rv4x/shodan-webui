import sqlite3

# Set up SQLite database
conn = sqlite3.connect('shodan_results.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS results
             (ip_address text, port text, data text)''')
conn.commit()


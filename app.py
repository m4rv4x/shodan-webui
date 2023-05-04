from flask import Flask, render_template, request
import shodan
import sqlite3

app = Flask(__name__)

# Set up Shodan API
SHODAN_API_KEY = "My_Shodan_Api_Key"
api = shodan.Shodan(SHODAN_API_KEY)

# Set up SQLite database
conn = sqlite3.connect('shodan_results.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS results
             (ip_address text, port text, data text)''')
conn.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        try:
            # Use Shodan API to search for query
            results = api.search(query)

            # Save results to SQLite database
            for result in results['matches']:
                ip_address = result['ip_str']
                port = str(result['port'])
                data = str(result['data'])
                c.execute("INSERT INTO results VALUES (?, ?, ?)", (ip_address, port, data))
                conn.commit()

            # Get count of results
            count = len(results['matches'])

            # Render template with results and count
            return render_template('index.html', results=results['matches'], count=count)
        except shodan.APIError as e:
            return render_template('index.html', error=str(e))
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

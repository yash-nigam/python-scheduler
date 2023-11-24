bash
Copy code
pip install Flask Flask-APScheduler
Now, create the Python program (app.py):

python
Copy code
from flask import Flask, jsonify
from flask_apscheduler import APScheduler
import sqlite3  # assuming you are using SQLite for simplicity

app = Flask(__name__)
scheduler = APScheduler()

# Configure the database (replace with your database configuration)
DATABASE = 'test.db'

def count_data():
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM test')
        result = cursor.fetchone()[0]
        print(f"Count of data in 'test' table: {result}")
        conn.close()
    except Exception as e:
        print(f"Error counting data: {e}")

# Schedule the job to run every 10 minutes
scheduler.add_job(id='count_job', func=count_data, trigger='interval', minutes=10)

# Start the scheduler
scheduler.start()

# Health endpoint
@app.route('/health')
def health():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(debug=True)

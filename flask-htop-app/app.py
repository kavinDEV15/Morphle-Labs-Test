from flask import Flask, render_template
import os
import time
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    
    full_name = "Kavin Dev R"  
    username = "codebase"
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    
    
    try:
        top_output = subprocess.check_output('top -b -n 1 | head -20', shell=True).decode('utf-8')
    except subprocess.CalledProcessError as e:
        top_output = f"Error fetching top data: {e}"
    
    return render_template('htop.html', full_name=full_name, username=username, server_time=server_time, top_output=top_output)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

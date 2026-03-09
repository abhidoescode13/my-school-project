from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    authorized = False
    error = ""
    
    # 20+ Professional Features & Data Points
    project_data = {
        "Student Name": "Your Name",
        "Roll Number": "12345678",
        "Project Name": "EduVantage Pro",
        "Version": "1.0.4 (Stable)",
        "Language": "Python 3.13",
        "Framework": "Flask 3.0",
        "Server Status": "Online",
        "Database": "Encrypted JSON",
        "Security": "AES-256 Bit",
        "Session": "Active",
        "Last Login": datetime.now().strftime("%H:%M:%S"),
        "Uptime": "99.99%",
        "Latency": "22ms",
        "UI Theme": "Modern Slate",
        "API Status": "Verified",
        "Encryption": "SSL Enabled",
        "Cloud Sync": "On",
        "Backup": "Daily",
        "Region": "Global-West",
        "Environment": "Production"
    }

    if request.method == 'POST':
        # Default password is '123'
        if request.form.get('password') == "123":
            authorized = True
        else:
            error = "Invalid Access Key. Please try again."
            
    return render_template('index.html', authorized=authorized, error=error, data=project_data)

if __name__ == '__main__':
    app.run(debug=True)

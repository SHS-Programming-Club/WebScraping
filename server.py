# app.py

from flask import Flask, render_template, request, jsonify
import hashlib

app = Flask(__name__)

# Serve the HTML page with the password form
@app.route('/')
def index():
    return render_template('index.html')

# Check password route
@app.route('/check-password', methods=['POST'])
def check_password():
    entered_password = request.form.get('password')
    
    if hashlib.sha256(entered_password.encode()).hexdigest() == 'c75cb66ae28d8ebc6eded002c28a8ba0d06d3a78c6b5cbf9b2ade051f0775ac4':
        result = 'Correct password!'
    else:
        result = 'Incorrect password!'
    
    return jsonify({'result': result})

@app.route('/validate-password', methods=['POST'])
def validate_password():
    entered_password = request.form.get('password')
    
    if hashlib.sha256(entered_password.encode()).hexdigest() == 'db55da3fc3098e9c42311c6013304ff36b19ef73d12ea932054b5ad51df4f49d':
        result = 'Password validated!'
    else:
        result = 'Password not validated!'
    
    return jsonify({'result': result})

@app.route('/verify-password', methods=['POST'])
def verify_password():
    entered_password = request.form.get('password')
    
    if hashlib.sha256(entered_password.encode()).hexdigest() == '6f6a4e56098cfd9af29e3ae549503b370211a4e94421457fe4cfd39a38a1fa08':
        result = 'Password verified!'
    else:
        result = 'Password not verified!'
    
    return jsonify({'result': result})

@app.route('/is-password', methods=['POST'])
def is_password():
    entered_password = request.form.get('password')
    
    if hashlib.sha256(entered_password.encode()).hexdigest() == '6557739a67283a8de383fc5c0997fbec7c5721a46f28f3235fc9607598d9016b':
        result = 'Password verified!'
    else:
        result = 'Password not verified!'
    
    return jsonify({'result': result})

@app.route('/probably-password', methods=['POST'])
def probably_password():
    entered_password = request.form.get('password')
    
    if hashlib.sha256(entered_password.encode()).hexdigest() == '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9':
        result = 'Password verified!'
    else:
        result = 'Password not verified!'
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
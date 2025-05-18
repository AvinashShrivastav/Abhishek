from flask import Flask, request, jsonify, send_file, send_from_directory
from flask_cors import CORS
from ai import ask_abhi_ai
import os
import traceback

app = Flask(__name__, static_url_path='')
CORS(app)  # Enable CORS for all routes

@app.route('/static/<path:path>')
def send_static(path):
    print(f"Serving static file: {path}")
    return send_from_directory('static', path)

@app.route('/assets/<path:path>')
def send_assets(path):
    print(f"Serving asset file: {path}")
    return send_from_directory('assets', path)

@app.route('/')
def home():
    print("Serving home page")
    return send_file('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    print("Received /ask request")
    print("Request headers:", dict(request.headers))
    print("Request data:", request.get_data(as_text=True))
    
    try:
        data = request.get_json()
        if not data:
            print("No JSON data received")
            return jsonify({'error': 'No data provided'}), 400
        
        question = data.get('question')
        if not question:
            print("No question in data")
            return jsonify({'error': 'No question provided'}), 400
        
        print(f"Processing question: {question}")
        response = ask_abhi_ai(question)
        if not response:
            print("No response generated")
            return jsonify({'error': 'No response generated'}), 500
            
        print(f"Sending response: {response}")
        return jsonify({'response': response})
    except Exception as e:
        print(f"Error in /ask endpoint: {str(e)}")
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True, port=5000, host='0.0.0.0') 
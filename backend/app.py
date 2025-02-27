from flask import Flask, request, jsonify
from google import genai
from dotenv import load_dotenv
from flask_cors import CORS
import os
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
load_dotenv()
GENAI_KEY = os.getenv("GENAI_KEY")

generic_prompt = """Summarize the following Terms & Conditions document in simple, easy-to-understand language. 
Break down the key points and provide a clear summary for a general consumer, covering the following:
1. Important rights the user may be forfeiting (e.g., opting out of lawsuits, arbitration clauses, or surrendering intellectual property).
2. Potential risks or obligations the user might face (e.g., fees, data usage, subscription terms).
3. Any limitations of liability (e.g., the company’s responsibilities in case of issues).
4. What happens in case of disputes (e.g., mandatory arbitration or jurisdiction for lawsuits).
5. Key privacy and data collection policies (e.g., how user data is handled, shared, or sold).
The text to summarize is:"""

@app.route('/tc-summary-text', methods=['GET'])
def getSummary():
    try:
        text = request.args.get('text')
        client = genai.Client(api_key=GENAI_KEY)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=f'{generic_prompt} {text}'
        )
        return response.text
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/tc-summary-file', methods=['POST'])
def getSummaryFile():
    try:
        file = request.files['file']
        text = file.read().decode('utf-8')
        client = genai.Client(api_key=GENAI_KEY)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=f'{generic_prompt} {text}'
        )
        return response.text
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/tc-summary-url', methods=['GET'])
def getSummaryFromURL():
    try:
        url = request.args.get('url')
        response = requests.get(url)
        text = response.text
        client = genai.Client(api_key=GENAI_KEY)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=f'{generic_prompt} {text}'
        )
        return response.text
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/tc-summary-json', methods=['POST'])
def getSummaryFromJSON():
    try:
        data = request.json
        text = data.get('text')
        client = genai.Client(api_key=GENAI_KEY)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=f'{generic_prompt} {text}'
        )
        return response.text
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return "Service is up and running!", 200

if __name__ == '__main__':
    app.run(debug=True)

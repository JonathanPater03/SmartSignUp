from flask import Flask
from google import genai
from dotenv import load_dotenv

load_dotenv()
GENAI_KEY = os.getenv("GENAI_KEY")
"""
client = genai.Client(api_key=GENAI_KEY)
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works"
)
print(response.text)
"""
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

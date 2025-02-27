#!/bin/bash

# Navigate to the backend and start Flask API
cd backend
source venv/bin/activate  # Activate virtual environment (skip if not using venv)
export FLASK_APP=app.py
flask run &  # Runs Flask in the background

# Navigate to the frontend and start React development server
cd ../smart-sign-up
npm start &  # Runs React frontend

echo "Backend and frontend are now running..."

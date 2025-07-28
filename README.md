# EMO Energy Assessment Project

## Setup Instructions

1.  **Backend:**
    *   Navigate to the `backend` directory.
    *   Create a virtual environment: `python -m venv venv`
    *   Activate the virtual environment: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows)
    *   Install dependencies: `pip install -r requirements.txt`
    *   Run the application: `uvicorn backend.main:app --reload`
2.  **Frontend:**
    *   Navigate to the `frontend` directory.
    *   Install dependencies: `npm install`
    *   Run the application: `npm start`

Access the frontend at `http://localhost:3000` (or the port specified by React).

## Running Tests

1.  Navigate to the `backend` directory.
2.  Run tests using `pytest`.

## API Key
The backend API uses API key authentication.  By default, the key is set to `supersecretkey`.  It can be changed by setting the environment variable `API_KEY`.

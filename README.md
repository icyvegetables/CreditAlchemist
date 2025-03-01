# CodeFest2025

AI-powered debt prioritization system using MongoDB, LangChain, FastAPI

## Getting started

### Setting up VS Code with Python for Backend

1. **Navigate to the Backend Directory**:
   - Open the terminal in VS Code by pressing Ctrl+` or navigating to View > Terminal.
   - Change the directory to the backend folder:

     ```sh
     cd backend
     ```

2. **Create a Virtual Environment**:
   - Run the following command to create a virtual environment:

     ```sh
     python3 -m venv venv
     ```

3. **Activate the Virtual Environment**:
   - On Windows:

     ```sh
     .\venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```sh
     source venv/bin/activate
     ```

4. **Install Libraries from `requirements.txt`**:
   - Ensure your terminal is in the project directory.
   - Run the following command to install all the libraries listed in `requirements.txt`:

     ```sh
     pip install -r requirements.txt
     ```

### To run the Backend Server

1. **Navigate to the Backend Directory** (if not already there):

   ```sh
   cd backend
   ```

2. **Start the FastAPI Server**:
   - Run the following command to start the FastAPI server:

     ```sh
     fastapi dev main.py
     ```

3. **Access the API Documentation**:
   - Open your web browser and navigate to `http://127.0.0.1:8000/docs` to view the interactive API documentation.

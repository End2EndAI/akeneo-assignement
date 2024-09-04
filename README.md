# akeneo-assignement

This project is the assignement for Akeneo. You will find a webapp where you can upload an excel file, with the list of the participants and their blacklist. It will generate a draw for the secret santa.

## Getting Started

### Prerequisites

- Python 3.11 or later
- Docker (if you prefer running in a container)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/End2EndAI/akeneo-assignement.git
   cd akeneo-assignement
   ```

2. **Install Dependencies:**

   ```bash
   conda create -n akeneo_env python=3.11
   pip install -r requirements.txt
   ```

### Running the App

You can run the application in two main ways:

1. **Run with Python locally:**

   ```bash
   python main.py
   ```

   This will start the FastAPI server, and you can access the API at `http://127.0.0.1:8000`.

2. **Deploy the API Using Docker:**

   You can use the Dockerfile from the repo to deploy the API using Docker. 

   ```bash
   docker build -t akeneo-app .
   docker run -p 8000:8000 akeneo-app
   ```

### Testing

Tests for this application are located in the `/test` folder. To run the tests, use:

```bash
pytest
```

### Main Functions

The core functionalities of the app are located in the `/src/functions.py` file.

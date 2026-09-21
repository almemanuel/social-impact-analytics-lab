# Project #1

This is a starter project containing a FastAPI application and a PostgreSQL database, both configured to run via Docker Compose.

## Prerequisites
- [Python 3.11+](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Local Environment Setup (Optional)

To develop locally and have autocomplete in your IDE, it is recommended to create and activate a virtual environment and install the dependencies.

1. **Create the virtual environment:**
   ```bash
   python -m venv .venv
   ```

2. **Activate the virtual environment:**
   - **On PowerShell (Windows):**
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - **On Bash / Git Bash (Windows):**
     ```bash
     source .venv/Scripts/activate
     ```
   - **On Linux / macOS:**
     ```bash
     source .venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

The project is already configured to run the services (API and Database) using Docker. 

To build the image and start the containers in the background, run:

```bash
docker compose up --build -d
```

## Accessing the Application

- **API:** http://localhost:8000
- **Interactive Documentation (Swagger):** http://localhost:8000/docs
- **Database (PostgreSQL):**
  - Host: `localhost`
  - Port: `5433`
  - User: `admin`
  - Password: `adminpassword`
  - Database: `dados_social`

## Stopping the Project

To stop and remove the containers, run:

```bash
docker compose down
```

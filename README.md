# Backend APP for LarpEx

## Installation
(you can also use Docker to run the app)
1. Install Python 3.11
2. Install pip
3. Create venv: `python3 -m venv apiVenv`
4. Activate venv: `source apiVenv/bin/activate` or `apiVenv\Scripts\activate`
5. Install requirements: `pip install -r requirements.txt`

## Configuration
- Set up the database connection in `app/config/database.py`
- Set info about the database in `.env` file
   - `DATABASE_URL` - database URL for postgresql. Example: `postgresql://user:password@localhost:port/dbname`
   - `USE_SQLITE_DB` - set to `True` if you want to use SQLite database for testing

## Run
1. Go to app: `cd app`
2. Run server: `uvicorn main:app`

## Docker
You can use tools: `docket-tool.ps1` or `docker-tool.sh` to build and run the docker container.
1. Build the container: `./docker-tool.ps1 build`
2. Run the container: `./docker-tool.ps1 run`

You can also:
- Check the container status: `./docker-tool.ps1 check`
- Stop the container: `./docker-tool.ps1 stop`
- Remove the container and images: `./docker-tool.ps1 rm`

Alternative way:
- Build the container: `docker build -t larpex-backend .`
- Run the container: `docker run -d -p 8000:8000 larpex-backend`


## OpenAPI
http://localhost:8000/docs

## How to code in this project?
Follow this steps:
1. Create an ORM model in `app/models/` directory.
2. Create a Pydantic schema in `app/schemas/` directory.
3. Create a service in `app/services/` directory.
4. Create a router in `app/routers/` directory.
5. Add the router to the `app/main.py` file.

Check each folder for README with examples.

Use refference from:
- [Project structure](https://levelup.gitconnected.com/structuring-fastapi-project-using-3-tier-design-pattern-4d2e88a55757)
- [Using DB](https://python.plainenglish.io/how-to-build-a-rest-api-endpoint-on-top-of-an-existing-legacy-database-using-fastapi-489f38feab98) 
- [Work with ORM - Pydantic](https://docs.pydantic.dev/latest/concepts/models/)
- official [FastAPI documentation](https://fastapi.tiangolo.com/)

## Project structure
```bash
├─ app/
   ├── config/                  # Backend functionality and configs
   │   ├── config.py            # Configuration settings  
   │   ├── database.py          # Database connection settings
   |   ├── exceptions.py        # Custom exceptions
   ├── models/                  # SQLAlchemy models
   │   ├── base.py        # Base classes, mixins
   │   └── ...                  # Other service models
   ├── routers/                 # API routes
   │   └── ...                  # Other service routers
   ├── schemas/                 # Pydantic models
   │   └── ...                  # Other service schemas
   ├── services/                # Business logic
   │   └── ...                  # Other service classes
   ├── consts.py                # Constants
   └── main.py                  # Application runner
── requirements.txt             # Python dependencies
```


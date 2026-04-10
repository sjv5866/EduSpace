# EduSpace - RIT Capstone Project

GitHub Repository for the RIT Capstone Project. EduSpace is an educational website that teaches users all about tle-projection and satellite simulation

## Backend Tools
- [PostgreSQL](https://www.postgresql.org/): Open Source Relational Database system
- [pgAdmin4](https://github.com/pgadmin-org/pgadmin4): Management dashboard for PostgreSQL
- [Docker](https://www.docker.com/): Container system to run our entire backend environment
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/): Lightweight Python REST API
- [Skyfield](https://rhodesmill.org/skyfield/): Astronomy package for generating precise positions of satellites and celestial bodies

## Prerequisites
1. Install Docker Desktop: https://docs.docker.com/desktop/
2. Install Python 3.10 and above: https://www.python.org/downloads/

## Setup Instructions
1. Create a `.env` file in the root of this repository. Populate the file with the following configuration. Fill in the variables with any name or password of your choice
```
DB_USER=
DB_PASSWORD=
PGADMIN_DEFAULT_EMAIL=
PGADMIN_DEFAULT_PASSWORD=
```
2. In the backend directory, create a new file called `servers.json`. Populate the file with the following code. Replace REPLACEME with the DB_USER value defined in step 1:
```json
{
    "Servers": {
        "1": {
            "Name": "Local",
            "Group": "Servers",
            "Host": "postgres",
            "Port": 5432,
            "MaintenanceDB": "postgres",
            "Username": "REPLACEME",
            "SSLCompression": 0
        }
    }
}
```

3. Create the file `backend/config/db.yml`, then populate the contents with the following. Replace REPLACEME section with DB_USER and DB_PASSWORD values defined in step 1
```yaml
host: postgres
database: cadet
user: REPLACEME
password: REPLACEME
port: 5432
```

4. Go to the backend directory, and start the project with the following command: `docker compose --env-file ../.env up --build -d`. 

## Project Links for Development
- pgAdmin Dashboard (Takes a while to access due to lengthy setup process with pgAdmin container): localhost:5050
- flask-restful endpoint: localhost:5000
    - "/manage/version": pulls postgresql version to determine connectivity with postgres server
    - "/manage/init": simple path to pull test data from tle table
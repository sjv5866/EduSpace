# EduSpace - RIT Capstone Project

GitHub Repository for the RIT Capstone Project. EduSpace is an educational website that teaches users all about tle-projection and satellite simulation

## Backend Tools
- [PostgreSQL](https://www.postgresql.org/): Open Source Relational Database system
- [pgAdmin4](https://github.com/pgadmin-org/pgadmin4): Management dashboard for PostgreSQL
- [Docker](https://www.docker.com/): Container system to run our entire backend environment
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/): Lightweight Python REST API
- [Skyfield](https://rhodesmill.org/skyfield/): Astronomy package for generating precise positions of satellites and celestial bodies

## Frontend Tools
- [React](https://react.dev/): JS Library for Web Apps and User Interfaces
- [Vite](https://vite.dev/): Build tool for React Projects
- [Docker](https://www.docker.com/): Container system to run our frontend environment
- [ThreeJS](https://threejs.org/): 3D Animation Library for JS
- [React Three Fiber](https://r3f.docs.pmnd.rs/getting-started/introduction): React Renderer for Three.js

## Prerequisites
1. Install Docker Desktop: https://docs.docker.com/desktop/
2. Install Python 3.10 and above: https://www.python.org/downloads/
3. Install Node v20.20.2 and above: https://nodejs.org/en/download

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

4. Start the project with the following command: `docker compose --env-file /.env up --build -d`. 

## Project Links for Development
- pgAdmin Dashboard (Takes a while to access due to lengthy setup process with pgAdmin container): localhost:5050
- flask-restful endpoint: localhost:5000
    - "/tles": Grabs list of all TLE data from database
    - "/tles/<sat_name>": Grabs unique TLE information from target satellite
    - "/tles/pos/<sat_name>": Grabs location data from specific TLE. Used by frontend to update component
    - "/version": Checks database version. Tests backend connectivity
- React/Threejs link: localhost:5173 
    - Main URL for earth-satellite simulation
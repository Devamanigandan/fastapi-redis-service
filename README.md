# README #

### Title ###
    FASTAPI-REDIS-CRUD-OPERATIONS

### Description ###
    FastAPI Redis Cache Service CRUD Operations

### Installations ###
    * Installing Redis on macOS
    
        Homebrew
            * brew --version
            * brew install redis

        Starting and stopping Redis in the foreground
            * redis-server

        Starting and stopping Redis in the foreground using launchd
            * brew services start redis (To start)
            * brew services info redis
            * brew services stop redis (To stop)

        Connect to Redis
            * redis-cli

            127.0.0.1:6379> ping
            PONG    

    * Installing FastAPI Redis Application
        First, clone this repo to a directory on your local machine and create a virtual environment
        Git Clone - gh repo clone Devamanigandan/fastapi-redis-service
        Venv command - python3 -m venv <venv name>
        
        After that's done, create and run your shell script file
        Run command - bash run.sh

        All these installations details is for local services.
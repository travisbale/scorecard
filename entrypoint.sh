#!/bin/bash

if [ $1 = 'development' ] || [ $1 = 'test' ]
then
    # Install requirements
    pip install --upgrade pip
    pip install -r requirements/production.txt
fi

if [ $1 != 'test' ]
then
    # Apply database schema migrations
    flask db upgrade
fi

if [ $1 = 'development' ] || [ $1 = 'test' ]
then
    # Run the service
    flask run -h 0.0.0.0
else
    gunicorn -c gunicorn.py 'scorecard:create_app()'
fi

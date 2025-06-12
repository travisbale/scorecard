# Scorecard

[![CI](https://github.com/travisbale/scorecard/actions/workflows/deploy.yml/badge.svg)](https://github.com/travisbale/scorecard/actions/workflows/deploy.yml)

Scorecard is a score keeping API service for golf. Scorecard is able to provide live scoring updates for tournaments, as well as individual rounds of golf, and can support any number of players playing any format of golf.

## Development Setup

Scorecard runs in its own docker container and uses a postgres database. Before spinning up the containers there are a few environment variables that need to be defined in an env/dev.env file. There is a sample .env file in the root of the repository that contains all the required variables.

In order to authenticate with Scorecard, users will have to have a valid JWT issued to their email address. This token will be used to determine the level of access the user should be granted based on the roles and permissions the user has assigned to their token. In order to verify the validity of the tokens Scorecard receives, the public key of the public/private key pair used to sign the tokens must be added to the /keys directory. This will allow Scorecard to verify that the data contained in the token is authentic.

Once that is setup, the environment can be spun up by running `docker-compose up -d`.

## Built with

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
- [marshmallow](https://marshmallow.readthedocs.io/en/stable/index.html)
- [Docker](https://www.docker.com/)

## License

MIT © Travis Bale

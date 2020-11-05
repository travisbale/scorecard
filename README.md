# Scorecard

> "Gambling is illegal at Bushwood sir, and I never slice." ―Judge Smails

Scorecard is a score keeping API service for golf. Scorecard is able to provide live scoring updates for tournaments, as well as individual rounds of golf, and can support any number of players playing any format of golf.

## API Reference

I haven't written a proper Postman collection to document the API, but in the meantime I've listed and partially described the available endpoints below.

#### `GET /golfers`

- Get the list of golfers

#### `POST /golfers`

- Create a new golfer
- Golfers need to be issued a JWT with a corresponding email address if they want to log in to update their scores

#### `GET /golfers/{id}`

- Get a specific golfer

#### `PUT /golfers/{id}`

- Update an existing golfer

#### `DELETE /golfers/{id}`

- Delete a specific golfer

#### `GET /tournaments`

- Get the list of tournaments

#### `POST /tournaments`

- Create a new tournament

#### `GET /tournaments/{id}`

- Get a specific tournament

#### `PUT /tournaments/{id}`

- Update an existing tournament

#### `GET /tournament/{id}/organizers`

- Get the list of tournament organizers
- Tournament organizers have admin privileges to the tournament
- Organizers are just players

#### `POST /tournament/{id}/organizers`

- Add organizers to the tournament

#### `DELETE /tournament/{id}/organizers`

- Remove organizers from the tournament

#### `GET /tournaments/{id}/teams`

- Get a list of teams playing in the tournament

#### `POST /tournaments/{id}/teams`

- Add a new team to the tournament

#### `DELETE /tournaments/{id}/teams`

- Remove the team from the tournament and delete it

#### `GET /tournaments/{id}/teams{id}/golfers`

- Get the list of golfers on the particular team

#### `POST /tournaments/{id}/teams{id}/golfers`

- Add new players to the team

#### `DELETE /tournaments/{id}/teams{id}/golfers`

- Remove players from the team

#### `GET /tournaments/{id}/rounds`

- Get the list of rounds in the tournament

#### `POST /tournaments/{id}/rounds`

- Add a new round to the tournament

#### `GET /tournaments/{id}/rounds/{id}`

- Get a specific round from the tournament

#### `DELETE /tournaments/{id}/rounds/{id}`

- Remove and delete a specific round from the tournament

#### `GET /tournaments/{id}/rounds/{id}/tee-times`

- Get a list of tee times for the tournament round

#### `POST /tournaments/{id}/rounds/{id}/tee-times`

- Add a new tee time to the tournament round

#### `GET /tournaments/{id}/rounds/{id}/tee-times/{id}`

- Get the details for a specific tee time including match results

#### `DELETE /tournaments/{id}/rounds/{id}/tee-times/{id}`

- Delete the tee time

#### `GET /tournaments/{id}/rounds/{id}/tee-times/{id}/golfers`

- Get the list of golfers assigned to the tee time

#### `POST /tournaments/{id}/rounds/{id}/tee-times/{id}/golfers`

- Assign golfers to the tee time

#### `DELETE /tournaments/{id}/rounds/{id}/tee-times/{id}/golfers`

- Unassign golfers from the tee time

#### `GET /tournaments/{id}/rounds/{id}/tee-times/{id}/golfers/{id}/scores`

- Get the golfer's score

#### `POST /tournaments/{id}/rounds/{id}/tee-times/{id}/golfers/{id}/scores`

- Record a new score for the golfer for the round

#### `DELETE /tournaments/{id}/rounds/{id}/tee-times/{id}/golfers/{id}/scores`

- Delete a score for the golfer for the round

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

# Genealogy Backend

The backend API component of the Genealogy Web Application.

This is a Python (Fast API) REST API with a Mongo DB document store.

Models are based on [GEDCOM X](http://www.gedcomx.org/schemas.html).

## TODO
* Add routes, controllers and any additional models for Events - `Graham Bragg`.
* Add routes, controllers and any additional models for Relationships - `Graham Bragg`.
* Develop model for multi-tree paradigm - tenancies for individual families to use with ability to link trees. - `Simon Bragg`
* Add additional logging to API endpoints.
* Add exception handling to API endpoints.
* Add Validation to models and API endpoints.
* Add additional Swagger documentation.
* Add Authentication and Authorisation
  * Authentication via passport modules - Allow Google, Microsoft, Facebook etc.

## Getting Started

### Pre-reading

* [FastAPI](https://fastapi.tiangolo.com/)

### Prerequisites

* VS Code
    * [Dev Containers Extension](https://code.visualstudio.com/docs/devcontainers/containers)

### Installing

#### Docker

See your Operating System's distribution.

#### Clone Project

```sh
git clone https://github.com/GrahamBragg/genealogy-backend.git
code genealogy-backend/
```

#### Install Dependencies

Once the workspace is running in a dev container, open a terminal and run the following command:

```sh
make install
```

#### Create new .env file from .env.example
_Create a local one for dev/debug as well_

```sh
# Working directory backend/
cp .env.sample .env
```

Edit the `.env` file to suit.

Sample:

```ini
DATABASE_URL=mongodb://localhost:27017/db

DOMAIN=localhost

PROJECT_NAME=backend

```

#### Debug

Make sure Mongo DB is accessible at the address in `.env` (probably mongodb://localhost:27017)

```sh
make run
```

##### Docker

```sh
# Docker compose up
make up

# Docker compose down
make down

```

The application will start on the port `8080`.

You should be able to navigate to the URL http://localhost:8080.

E.g. [http://localhost:8080](http://localhost:8080) for default.

This is the root for the API.

Docs are located at:

* [http://localhost:8080/docs](Swagger Docs)
* [http://localhost:8080/redoc](ReDoc Docs)

#### API Test Software

It is recommend to use software such as Insomnia or Postman for testing the API.


## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

//TODO

```
Example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [FastAPI](https://fastapi.tiangolo.com/) - The web framework used
* [Poetry](https://python-poetry.org/docs/)- Dependency Management
* [MongoDB](https://www.mongodb.com/) - Database and document store

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/GrahamBragg/genealogy-backend/tags). 

## Authors

* **Graham Bragg** - *Concept, Design and main developer* - [Graham Bragg](https://github.com/GrahamBragg)
* **Simon Bragg** - *Design and developer* - [Simon Bragg](https://github.com/maiorsi)

See also the list of [contributors](https://github.com/GrahamBragg/genealogy-backend/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Sample JSON

### Create a new Person

```json
{
    "names": [
        {
            "type": "BIRTH_NAME",
            "nameForms": [
                {
                    "fullText": "John Abraham Mark Smith",
                    "parts": [
                        {
                            "type": "GIVEN",
                            "value": "John"
                        },
                        {
                            "type": "GIVEN",
                            "value": "Abraham"
                        },
                        {
                            "type": "GIVEN",
                            "value": "Mark"
                        },
                        {
                            "type": "SURNAME",
                            "value": "Smith"
                        }
                    ]
                }
            ],
            "confidence": "HIGH"
        }
    ],
    "facts": [
        {
            "type": "BIRTH",
            "date": "1970-01-01",
            "place": {
                "original": "Canberra"
            },
            "confidence": "HIGH",
            "sources": [
                {
                    "description": "Birth Certificate"
                }
            ]
        }
    ],
    "gender": "MALE"
}
```

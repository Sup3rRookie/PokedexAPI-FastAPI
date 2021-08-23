# PokedexAPI-FastAPI
One Day Build Project - Exploring this framework.

# PokedexAPI 

One day build project - Implementing full CRUD operation using FastAPI. This API was tested on Swagger UI. Every Requests and Response made by the client are recorded in SQLAlchemy (open-source SQL toolkit and object-relational mapper for the Python) .

Finally, we deploy our app using Docker 🐳 . 


## Installation

Install my-project with npm

```bash
$ pip install fastapi
$ pip install uvicorn
$ pip install fastapi
```

    
## Documentation

[Fastapi](https://fastapi.tiangolo.com/)
[Uvicorn](https://www.uvicorn.org/)
[Sqlalchemy](https://docs.sqlalchemy.org/en/14/orm/tutorial.html)


  
## API Reference

#### Get all pokemons

```http
  GET /pokemon/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `` | `` | Return lists of pokemon in the Database |

#### Get single pokemon

```http
    GET /pokemon/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of the pokemon to fetch |

```http
    PUT /pokemon/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of the pokemon to update |

```http
    POST /pokemon/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| ``      | `` | Create a new Pokemon and save it in the db |


```http
    DELETE /pokemon/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required** Delete a  Pokemon and db update new lists of pokemon |


  
## Deployment

To deploy this project, create a dockerfile to build the image


```bash
FROM python:3.8-slim-buster
EXPOSE 8000

### Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

### Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

### Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "FastAPI.blog.main:app"]
```

Then, we transfer our image to the server. We can use Docker Hub which is a docker repository server.
```bash
-- on local machine
$ docker tag PokedexAPI-FastAPI yourAccount/PokedexAPI-FastAPI
$ docker push yourAccount/PokedexAPI-FastAPI
```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`fastapi`
`uvicorn`
`sqlalchemy`

  
## Feedback

If you have any feedback, please reach out at auliya.izham@gmail.com

  

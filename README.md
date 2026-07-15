# Task API

A simple RESTful CRUD API built with FastAPI. This API manages tasks in memory and supports Create, Read, Update, and Delete (CRUD) operations.

## Features

- Create a task
- View all tasks
- View a task by ID
- Update a task
- Delete a task
- Built-in Swagger UI documentation

## Requirements

- Python 3.10+
- FastAPI
- Uvicorn

## Installation

```bash
pip install -r requirements.txt
```

## Run the API

```bash
uvicorn main:app --reload
```

The API will be available at:

- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information |
| GET | `/health` | Health check |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{id}` | Get a task by ID |
| POST | `/tasks` | Create a task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

## Example cURL

```bash
curl -X GET http://127.0.0.1:8000/tasks
```
##screenshot
<img width="1830" height="951" alt="Screenshot (1649)" src="https://github.com/user-attachments/assets/f86547b0-9721-483e-9d24-9c5ae2f7dffb" />


## Author

Madhu

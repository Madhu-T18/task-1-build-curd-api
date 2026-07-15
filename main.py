from fastapi import FastAPI, HTTPException, Body, Response, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Task API",
    description="A simple CRUD API for managing tasks.",
    version="1.0"
)


tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build CRUD API", "done": False},
    {"id": 3, "title": "Push to GitHub", "done": True},
]


class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None


@app.get("/", summary="API information")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }


@app.get("/health", summary="Health check")
def health():
    return {"status": "ok"}


@app.get("/tasks", summary="List all tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}", summary="Get a task by ID")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail={"error": f"Task {task_id} not found"}
    )


@app.post("/tasks", status_code=201, summary="Create a task")
def create_task(task: TaskCreate):

    if not task.title.strip():
        raise HTTPException(
            status_code=400,
            detail={"error": "Title cannot be empty"}
        )

    new_task = {
        "id": max(task["id"] for task in tasks) + 1 if tasks else 1,
        "title": task.title,
        "done": False
    }

    tasks.append(new_task)

    return new_task


@app.put("/tasks/{task_id}", summary="Update a task")
def update_task(task_id: int, update: TaskUpdate):

    for task in tasks:

        if task["id"] == task_id:

            if update.title is not None:

                if not update.title.strip():
                    raise HTTPException(
                        status_code=400,
                        detail={"error": "Title cannot be empty"}
                    )

                task["title"] = update.title

            if update.done is not None:
                task["done"] = update.done

            return task

    raise HTTPException(
        status_code=404,
        detail={"error": f"Task {task_id} not found"}
    )


@app.delete("/tasks/{task_id}",
            status_code=status.HTTP_204_NO_CONTENT,
            summary="Delete a task")
def delete_task(task_id: int):

    for index, task in enumerate(tasks):

        if task["id"] == task_id:
            tasks.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(
        status_code=404,
        detail={"error": f"Task {task_id} not found"}
    )
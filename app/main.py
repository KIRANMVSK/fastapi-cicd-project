
from fastapi import FastAPI

app = FastAPI(
    title="CI/CD Demo API",
    description="FastAPI application for GitHub Actions CI/CD",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI CI/CD Pipeline",
        "status": "Running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": "Sai",
        "role": "DevOps Engineer"
    }

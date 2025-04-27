from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome_msg():
    return {
        "message": "Welcome to Meet for You"
    }
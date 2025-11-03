from fastapi import FastAPI
from chainlit.utils import mount_chainlit
    
app = FastAPI()


@app.get("/app")
def read_main():
    return {"message": "Welcome to Smartphone buying Agent!"}


mount_chainlit(app=app, target="/tmp/cl_app.py", path="/chainlit")
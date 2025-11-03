from contextlib import asynccontextmanager

from fastapi import FastAPI
from chainlit.utils import mount_chainlit
    
app = FastAPI()


@app.get("/app")
def read_main():
    return {"message": "Welcome to Smartphone buying Agent!"}



with open("chaiblit_config.py") as f:
        content = f.read()
        
with open("/var/task/_vendor/chainlit/config.py", "w") as f:
    f.write(content)

mount_chainlit(app=app, target="/tmp/cl_app.py", path="/chainlit")
from contextlib import asynccontextmanager

from fastapi import FastAPI
from chainlit.utils import mount_chainlit

@asynccontextmanager
async def lifespan(app: FastAPI):
    with open("chaiblit_config.py") as f:
        content = f.read()
        
    with open("/var/task/_vendor/chainlit/config.py", "w") as f:
        f.write(content)

app = FastAPI(lifespan=lifespan)


@app.get("/app")
def read_main():
    return {"message": "Hello World from main app"}

mount_chainlit(app=app, target="/tmp/cl_app.py", path="/chainlit")
from contextlib import asynccontextmanager
import uvicorn
import logging
import time
from multiprocessing import Process
from fastapi import FastAPI
# from ._version import __version__

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Starting up.")
    yield

    logging.info("Shutting down.")


app = FastAPI(lifespan=lifespan)


@app.get("/liveness")
def liveness():
    return "Liveness check completed"


@app.get("/readiness")
def readiness():
    return "Readiness check completed"


# @app.get("/")
# def index():
#     return "{name} {version}".format(name=__package__, version=__version__)


def run_fastapi():
    uvicorn.run(app, host="0.0.0.0", port=8000)


def consumer():
    while True:
        print("Hello!")
        time.sleep(3)


def main():
    consumer_process = Process(target=consumer)
    fastapi_process = Process(target=run_fastapi)

    consumer_process.start()
    fastapi_process.start()

    consumer_process.join()
    fastapi_process.terminate()

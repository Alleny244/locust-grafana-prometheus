# app.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import random
import asyncio
import asyncio.locks

app = FastAPI()

active_requests = 0
lock = asyncio.Lock()


@app.get("/")
def home():
    return "Home"


@app.get("/api/data")
async def data():
    global active_requests
    async with lock:
        active_requests += 1

    delay = random.uniform(0.1, 0.3)

    penalty = active_requests * 0.05
    await asyncio.sleep(delay + penalty)

    async with lock:
        active_requests -= 1

    return JSONResponse(
        content={
            "message": f"Active users: {active_requests}\n",
            "delay": f" Delay: {round(delay + penalty, 2)}s",
        }
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

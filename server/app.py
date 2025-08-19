# app.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
import random
import asyncio
import asyncio.locks

app = FastAPI()

active_requests = 0
lock = asyncio.Lock()


@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Demo App</title>
    </head>
    <body>
        <h1>Load Testing Demo</h1>
        <button onclick="fetchData()">Fetch Data</button>
        <div id="counter" style="margin-top: 10px; font-weight: bold;"></div>
        <div id="output" style="margin-top: 20px; font-size: 18px; color: blue;"></div>

        <script>
            let count = 0;
            async function fetchData() {
                count++;
                document.getElementById("counter").innerText = "Requests made: " + count;

                const res = await fetch("/api/data");
                const data = await res.json();
                document.getElementById("output").innerText =data.message + " " + data.delay
            }
        </script>
    </body>
    </html>
    """


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

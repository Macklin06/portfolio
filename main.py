from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import logging
import json

app = FastAPI()

# Enable CORS (so cross-origin GET requests are allowed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup logging
logging.basicConfig(filename="agent_runs.log", level=logging.INFO)

@app.get("/task")
def run_task(q: str = Query(..., description="Task description")):
    """
    Simulates delegating a coding task to a CLI agent.
    For safety and simplicity, this demo uses a subprocess to run code,
    but in real scenarios you'd call an external CLI agent (e.g. aider, copilot-cli).
    """

    agent = "copilot-cli"

    # Log task
    logging.info(f"Received task: {q}")

    output = ""

    # Simulate the “CLI agent” solving the task
    if "8" in q and "!" in q:
        # Simple factorial demo
        code = "print(1*2*3*4*5*6*7*8)"
        result = subprocess.run(
            ["python3", "-c", code],
            capture_output=True,
            text=True
        )
        output = result.stdout.strip()
    else:
        output = "Agent run complete, but task not recognized."

    # Log output
    logging.info(f"Output: {output}")

    response = {
        "task": q,
        "agent": agent,
        "output": output,
        "email": "24f2001048@ds.study.iitm.ac.in"
    }

    return response
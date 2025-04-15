import os
import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException, Query, Request
from dotenv import load_dotenv
import uvicorn
from api.run import run_tool  # Import the dynamic tool execution function

load_dotenv()

app = FastAPI()

@app.post("/run")
async def execute_tool(request: Request):
    try:
        params = dict(request.query_params)
        tool = params.pop("tool", None)
        message = params.pop("message", "")

        if not tool:
            raise HTTPException(status_code=400, detail="Tool parameter is required")

        command = {
            "command": "run",
            "tool": tool,
            "data": {"message": message, "params": params}
        }
        response = run_tool(command)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
    
    

@app.post("/")
async def health_check():
    return {"status": "running"}

async def run_fastapi_server():
    host = os.getenv("HOST", "localhost")
    config = uvicorn.Config(app, host=host, port=8000, loop="asyncio")
    server = uvicorn.Server(config)
    await server.serve()

import asyncio
from api.server import run_fastapi_server
from api.socket import start_websocket_server

async def run_servers():
    fastapi_task = asyncio.create_task(run_fastapi_server())
    websocket_task = asyncio.create_task(start_websocket_server())
    await asyncio.gather(fastapi_task, websocket_task)

if __name__ == "__main__":
    asyncio.run(run_servers())






# import asyncio
# import websockets
# import json
# import os
# from dotenv import load_dotenv
# from api.run_ import run_tool  # Import the run_tool function

# load_dotenv()

# HOST = os.getenv("HOST", "localhost")
# PORT = int(os.getenv("PORT", 8768))

# async def handle_client(websocket):
    
#     try:
#         while True:  # Keep receiving messages as long as the connection is open
#             command_data = await websocket.recv()

#             command = json.loads(command_data)
#             print(f"Received command: {command}")

#             response = run_tool(command)

#             await websocket.send(json.dumps(response))

#     except websockets.exceptions.ConnectionClosed as e:
#         print(f"Connection closed: {e}")
#     except Exception as e:
#         print(f"Error: {e}")
#         response = {
#             "status": "error",
#             "message": "An error occurred while processing the command."
#         }
#         await websocket.send(json.dumps(response))

# async def start_server():
#     server = await websockets.serve(handle_client, HOST, PORT)
#     print(f"WebSocket server started on ws://{HOST}:{PORT}")
#     return server

# async def main():
#     while True:
#         try:
#             server = await start_server()   

#             await server.wait_closed()
#         except websockets.exceptions.ConnectionClosedError:
#             print("WebSocket connection was unexpectedly closed. Reconnecting...")
#             await asyncio.sleep(2)  
#         except Exception as e:
#             print(f"Unexpected error: {e}")
#             await asyncio.sleep(5)  
# if __name__ == "__main__":
#     asyncio.run(main())



# import os
# import json
# import asyncio
# import importlib
# import websockets
# from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
# from pydantic import BaseModel
# from dotenv import load_dotenv
# import uvicorn

# from api.run_ import run_tool  # Import the dynamic tool execution function

# load_dotenv()

# app = FastAPI()

# # Request schema for HTTP API
# class CommandRequest(BaseModel):
#     tool: str
#     data: dict

# # HTTP Endpoint
# @app.post("/execute")
# async def execute_tool(request: CommandRequest):
#     try:
#         response = run_tool(request.dict())
#         return response
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

# # WebSocket Endpoint (FastAPI WebSocket)
# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     try:
#         while True:
#             command_data = await websocket.receive_text()
#             command = json.loads(command_data)
#             print(f"Received WebSocket command: {command}")

#             response = run_tool(command)
#             await websocket.send_text(json.dumps(response))

#     except WebSocketDisconnect:
#         print("Client disconnected")
#     except Exception as e:
#         print(f"WebSocket Error: {e}")
#         await websocket.send_text(json.dumps({"status": "error", "message": "An error occurred"}))

# @app.get("/")
# async def health_check():
#     return {"status": "running"}

# # Separate WebSocket Server (Using `websockets` library)
# async def start_websocket_server():
#     host = os.getenv("HOST", "localhost")
#     port = int(os.getenv("PORT", 8768))

#     async def websocket_handler(websocket):
#         try:
#             while True:
#                 command_data = await websocket.recv()
#                 command = json.loads(command_data)
#                 print(f"Received WebSocket command: {command}")

#                 response = run_tool(command)
#                 await websocket.send(json.dumps(response))
#         except websockets.exceptions.ConnectionClosed:
#             print("WebSocket connection closed")
#         except Exception as e:
#             print(f"WebSocket Error: {e}")
#             await websocket.send(json.dumps({"status": "error", "message": "An error occurred"}))

#     server = await websockets.serve(websocket_handler, host, port)
#     print(f"WebSocket server started on ws://{host}:{port}")
#     await server.wait_closed()

# # Function to run both FastAPI and WebSocket server
# async def run_servers():
#     # Create Uvicorn server instance
#     config = uvicorn.Config(app, host="0.0.0.0", port=8000, loop="asyncio")
#     server = uvicorn.Server(config)

#     # Run FastAPI and WebSocket in parallel
#     fastapi_task = asyncio.create_task(server.serve())
#     websocket_task = asyncio.create_task(start_websocket_server())

#     await asyncio.gather(fastapi_task, websocket_task)

# if __name__ == "__main__":
#     asyncio.run(run_servers())  # Runs both servers concurrently


# import os
# import json
# import asyncio
# import importlib
# import websockets
# from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
# from pydantic import BaseModel
# from dotenv import load_dotenv
# import uvicorn

# from api.run_ import run_tool  # Import the dynamic tool execution function

# load_dotenv()

# app = FastAPI()

# # Request schema for HTTP API
# class CommandRequest(BaseModel):
#     tool: str
#     data: dict

# # HTTP Endpoint
# @app.post("/execute")
# async def execute_tool(request: CommandRequest):
#     try:
#         response = run_tool(request.dict())
#         return response
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

# # WebSocket Endpoint (FastAPI WebSocket)
# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     try:
#         while True:
#             command_data = await websocket.receive_text()
#             command = json.loads(command_data)
#             print(f"Received WebSocket command: {command}")

#             response = run_tool(command)
#             await websocket.send_text(json.dumps(response))

#     except WebSocketDisconnect:
#         print("Client disconnected")
#     except Exception as e:
#         print(f"WebSocket Error: {e}")
#         await websocket.send_text(json.dumps({"status": "error", "message": "An error occurred"}))

# @app.get("/")
# async def health_check():
#     return {"status": "running"}

# # Separate WebSocket Server (Using `websockets` library)
# async def start_websocket_server():
#     host = os.getenv("HOST", "localhost")
#     port = int(os.getenv("PORT", 8768))

#     async def websocket_handler(websocket):
#         try:
#             while True:
#                 command_data = await websocket.recv()
#                 command = json.loads(command_data)
#                 print(f"Received WebSocket command: {command}")

#                 response = run_tool(command)
#                 await websocket.send(json.dumps(response))
#         except websockets.exceptions.ConnectionClosed:
#             print("WebSocket connection closed")
#         except Exception as e:
#             print(f"WebSocket Error: {e}")
#             await websocket.send(json.dumps({"status": "error", "message": "An error occurred"}))

#     server = await websockets.serve(websocket_handler, host, port)
#     print(f"WebSocket server started on ws://{host}:{port}")
#     await server.wait_closed()

# # Function to run both FastAPI and WebSocket server
# async def run_servers():
#     # Create Uvicorn server instance
#     config = uvicorn.Config(app, host="localhost", port=8000, loop="asyncio")
#     server = uvicorn.Server(config)

#     # Run FastAPI and WebSocket in parallel
#     fastapi_task = asyncio.create_task(server.serve())
#     websocket_task = asyncio.create_task(start_websocket_server())

#     await asyncio.gather(fastapi_task, websocket_task)

# if __name__ == "__main__":
#     asyncio.run(run_servers())


# import os
# import json
# import asyncio
# import importlib
# import websockets
# from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
# from pydantic import BaseModel
# from dotenv import load_dotenv
# import uvicorn

# from api.run_ import run_tool  # Import the dynamic tool execution function

# load_dotenv()

# app = FastAPI()

# # Request schema for HTTP API
# class CommandRequest(BaseModel):
#     tool: str
#     data: dict

# # HTTP Endpoint
# @app.post("/execute")
# async def execute_tool(request: CommandRequest):
#     try:
#         response = run_tool(request.dict())
#         return response
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

# @app.get("/")
# async def health_check():
#     return {"status": "running"}

# # Separate WebSocket Server (Using `websockets` library)
# async def start_websocket_server():
#     host = os.getenv("HOST", "192.168.68.134")
#     port = int(os.getenv("PORT", 8768))

#     async def websocket_handler(websocket):
#         try:
#             while True:
#                 command_data = await websocket.recv()
#                 command = json.loads(command_data)
#                 print(f"Received WebSocket command: {command}")

#                 response = run_tool(command)
#                 await websocket.send(json.dumps(response))
#         except websockets.exceptions.ConnectionClosed:
#             print("WebSocket connection closed")
#         except Exception as e:
#             print(f"WebSocket Error: {e}")
#             await websocket.send(json.dumps({"status": "error", "message": "An error occurred"}))

#     server = await websockets.serve(websocket_handler, host, port)
#     print(f"WebSocket server started on ws://{host}:{port}")
#     await server.wait_closed()

# if __name__ == "__main__":
#     # Run FastAPI server using PM2 (only FastAPI instance)
#     if os.getenv("RUN_FASTAPI", "False").lower() == "true":
#         uvicorn.run(app, host="192.168.68.134", port=8000)

#     # Run WebSocket server using PM2 (only WebSocket instance)
#     else:
#         asyncio.run(start_websocket_server())


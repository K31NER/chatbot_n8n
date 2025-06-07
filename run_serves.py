import asyncio
import uvicorn

async def start_server(app_path, port):
    config = uvicorn.Config(app_path, host="127.0.0.1", port=port, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    await asyncio.gather(
        start_server("main:app", 8080),
        start_server("api_mcp:app", 8000),
    )

if __name__ == "__main__":
    asyncio.run(main())

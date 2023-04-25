## Run all the FastAPI apps with uvicorn
import uvicorn
import asyncio
import sys

async def run_webserver(module:str, portapp:int):
    server_config = uvicorn.Config(module, port=portapp, reload=True)
    server = uvicorn.Server(server_config)
    await server.serve()


async def main():
    done, pending = await asyncio.wait(
        [
            run_webserver("bdd.main:app",8083),
            run_webserver("movies.main:app",8082),
            run_webserver("users.main:app",8084),
            run_webserver("teams.main:app",8081),
        ],
        return_when=asyncio.FIRST_COMPLETED,
    )

    print("done")
    print(done)
    print("pending")
    print(pending)
    for pending_task in pending:
        pending_task.cancel("Another service died, server is shutting down")
        

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit(0)


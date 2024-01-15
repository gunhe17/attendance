import uvicorn

from attendance.http.server import Router, Server, cors, proxy_headers

server = Server("Shelter API Server")
server.middleware(cors())
server.middleware(proxy_headers())

# health
server.router(Router(path="/health", methods=["GET"], endpoint=lambda: "HEALTHY"))

# App
app = server.app()

if __name__ == "__main__":
    server.print()
    uvicorn.run("shelter.bin.server:app", host="0.0.0.0", port=8000, reload=True)

from fastapi import FastAPI
from discovery import registry, heartbeat, search, scheduler

app = FastAPI()

@app.on_event("startup")
def startup_event():
    scheduler.start_background_checker()

@app.post("/register")
def register_service(name: str, host: str, port: int, tags: list[str] = None):
    return registry.register(name, host, port, tags)

@app.post("/deregister")
def deregister_service(name: str):
    return registry.deregister(name)

@app.post("/heartbeat")
def heartbeat_update(name: str):
    return heartbeat.update_heartbeat(name)

@app.get("/discover/{query}")
def discover(query: str):
    return search.lookup(query)

@app.get("/services")
def list_services():
    return registry.all_services()
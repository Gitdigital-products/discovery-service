from fastapi import APIRouter
from src.discovery import registry, search

router = APIRouter()

@router.post("/register")
def register_service(name: str, host: str, port: int, tags: list[str] = None):
    return registry.register(name, host, port, tags)

@router.delete("/deregister/{name}")
def deregister_service(name: str):
    return registry.deregister(name)

@router.get("/discover/{name}")
def discover_service(name: str):
    return registry.get_service(name)

@router.get("/search")
def search_services(q: str):
    return search.lookup(q)
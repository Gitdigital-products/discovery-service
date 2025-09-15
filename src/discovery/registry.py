from typing import Dict, Any
import time

# In-memory registry (replace with DB later if needed)
_services: Dict[str, Dict[str, Any]] = {}

def register(name: str, host: str, port: int, tags: list[str] = None):
    _services[name] = {
        "host": host,
        "port": port,
        "tags": tags or [],
        "last_seen": time.time(),
        "status": "healthy"
    }
    return {"status": "registered", "service": _services[name]}

def deregister(name: str):
    if name in _services:
        del _services[name]
        return {"status": "deregistered", "service": name}
    return {"error": "service not found"}

def get_service(name: str):
    if name not in _services:
        return {"error": "service not found"}
    return _services[name]

def all_services():
    return _services
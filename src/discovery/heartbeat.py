import time
from . import registry

HEARTBEAT_TIMEOUT = 30  # seconds

def update_heartbeat(name: str):
    service = registry.get_service(name)
    if "error" in service:
        return {"error": "service not found"}
    service["last_seen"] = time.time()
    service["status"] = "healthy"
    return {"status": "heartbeat updated", "service": service}

def check_services():
    now = time.time()
    dead = []
    for name, service in registry.all_services().items():
        if now - service["last_seen"] > HEARTBEAT_TIMEOUT:
            service["status"] = "unhealthy"
            dead.append(name)
    return {"checked": len(registry.all_services()), "unhealthy": dead}
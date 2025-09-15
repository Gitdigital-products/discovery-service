from . import registry

def lookup(query: str):
    results = []
    for name, service in registry.all_services().items():
        if query.lower() in name.lower() or any(query.lower() in tag.lower() for tag in service["tags"]):
            results.append({name: service})
    return {"results": results, "count": len(results)}
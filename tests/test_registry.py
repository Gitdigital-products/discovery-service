from src.discovery import registry

def test_register_and_discover():
    result = registry.register("test-service", "127.0.0.1", 8080, ["api", "test"])
    assert result["status"] == "registered"

    discovered = registry.get_service("test-service")
    assert discovered["host"] == "127.0.0.1"
    assert "api" in discovered["tags"]

def test_deregister():
    registry.register("temp-service", "127.0.0.1", 8081)
    result = registry.deregister("temp-service")
    assert result["status"] == "deregistered"
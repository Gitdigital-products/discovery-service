from src.discovery import scheduler

def test_scheduler_start():
    result = scheduler.start_background_checker()
    assert result["status"] == "background checker started"
    assert "interval" in result
import threading
import time
from . import heartbeat

CHECK_INTERVAL = 10  # seconds

def _worker():
    while True:
        result = heartbeat.check_services()
        print(f"[Scheduler] Checked {result['checked']} services. Unhealthy: {result['unhealthy']}")
        time.sleep(CHECK_INTERVAL)

def start_background_checker():
    thread = threading.Thread(target=_worker, daemon=True)
    thread.start()
    return {"status": "background checker started", "interval": CHECK_INTERVAL}
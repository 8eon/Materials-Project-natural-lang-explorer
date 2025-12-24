import os
import time
from mp_api.client import MPRester

# Suppress progress bars from mp-api/tqdm for a cleaner TUI experience
os.environ["MP_API_MUTE_PROGRESS_BARS"] = "True"

class MPBase:
    """Base class to share the Materials Project connection and track usage."""
    def __init__(self, api_key: str):
        self.mpr = MPRester(api_key, mute_progress_bars=True)
        self.call_count = 0
        self.current_action = "Idle"
        self.last_call_time = 0

    def record_call(self, action_name: str):
        """Increments the call counter and updates the current action with a small delay."""
        self.call_count += 1
        self.current_action = action_name
        self.last_call_time = time.time()
        # Small delay to respect Gemini API rate limits (Free Tier)
        time.sleep(1.5)


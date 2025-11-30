"""
Configuration settings for TripCraft AI
"""
import os
import logging
from typing import Dict, Any

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Default configuration
DEFAULT_CONFIG = {
    "retry_attempts": 5,
    "initial_delay": 1.0,
    "max_delay": 30.0,
    "multiplier": 2.0,
    "compaction_interval": 180,
    "overlap_size": 100,
    "max_events": 2000
}

# Model configuration
MODEL_CONFIG = {
    "default_model": "gemini-2.5-flash-lite",
    "temperature": 0.7,
    "max_tokens": 2048
}

# Travel planning defaults
TRAVEL_DEFAULTS = {
    "default_destination": "Tokyo",
    "default_budget": 2000,
    "default_duration": 5,
    "default_style": "mid-range",
    "default_interests": ["culture", "food"]
}

def get_config() -> Dict[str, Any]:
    """Get complete configuration dictionary"""
    return {
        **DEFAULT_CONFIG,
        **MODEL_CONFIG,
        **TRAVEL_DEFAULTS
    }